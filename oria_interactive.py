import os
import sys
import json
import asyncio

# Ajout des chemins nécessaires pour importer les modules
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
sys.path.append(os.path.join(BASE_DIR, 'backend', 'src'))
sys.path.append(os.path.join(BASE_DIR, 'tests_simulation'))

from ai.extraction.extractor import SignalExtractor
from application.scoring_engine import ScoringEngine
from application.orientation_engine import OrientationEngine
from application.territory_manager import TerritoryManager
from oria_display import afficher_orientations

async def interactive_loop():
    SCHEMA_PATH = os.path.join(BASE_DIR, 'config', 'schemas', 'schema_definition.json')
    COMID_PATH = os.path.join(BASE_DIR, 'config', 'rules', 'COMID.json')
    ORIENTATION_RULES_PATH = os.path.join(BASE_DIR, 'config', 'rules', 'orientation_rules.json')
    TERRITORY_PATH = os.path.join(BASE_DIR, 'config', 'referentials', 'referentiel_territoire.json')

    # Initialisation des instances
    try:
        extractor = SignalExtractor(schema_path=SCHEMA_PATH, comid_path=COMID_PATH)
        scoring_engine = ScoringEngine(comid_rules_path=COMID_PATH)
        orientation_engine = OrientationEngine(rules_path=ORIENTATION_RULES_PATH)
        territory_manager = TerritoryManager(territory_rules_path=TERRITORY_PATH)
    except Exception as e:
        print(f"Erreur d'initialisation des moteurs : {e}")
        return

    print("=" * 70)
    print("                 MOTEUR D'ORIENTATION CLINIQUE ORIA")
    print("                     (Mode Interactif Terminal)")
    print("=" * 70)
    print("Saisissez une description de situation pour obtenir des recommandations d'orientation.")
    print("Pour quitter, tapez 'exit' ou 'quit'.\n")

    while True:
        print("-" * 70)
        print("1. SAISIE DE LA SITUATION (Copiez-collez votre texte)")
        print("(Appuyez sur Entrée deux fois de suite ou tapez 'FIN' sur une ligne vide pour valider) :")
        
        lines = []
        while True:
            try:
                line = input()
            except (KeyboardInterrupt, EOFError):
                print("\nInterruption détectée. Retour au menu.")
                break
            
            if line.strip().upper() == "FIN":
                break
            if not line.strip() and lines and lines[-1] == "":
                # Deux fois entrée consécutive
                lines.pop() # Enlever la ligne vide finale
                break
            lines.append(line)
            if not line.strip() and len(lines) == 1:
                # Si l'utilisateur appuie juste sur entrée sans rien sur la première ligne
                break
                
        text = " ".join(lines).strip()
        if not text:
            print("[Info] Saisie vide. Voulez-vous quitter ? (tapez 'exit' ou réessayez)")
            continue

        if text.lower() in ["exit", "quit"]:
            print("\nMerci d'avoir utilisé ORIA. À bientôt !")
            break

        print("\n2. COMMUNE DE RÉSIDENCE (Optionnel)")
        print("Saisissez la ville de l'usager pour le ciblage territorial (Ex: Ollioules, La Seyne-sur-Mer) :")
        print("*(Appuyez sur Entrée sans rien écrire pour laisser l'IA la détecter automatiquement)*")
        city_input = input("> ").strip()

        print("\nAnalyse clinique par l'IA d'extraction en cours (Ollama)... Veuillez patienter...")
        try:
            # 1. Extraction IA
            extracted_data = await extractor.extract(text)
            
            # Détection automatique de la ville si non fournie
            commune = city_input
            if not commune:
                commune = extracted_data.get("usager.localisation.commune_residence")
            if not commune:
                commune = "La Seyne-sur-Mer" # Fallback par défaut
                print(f"[Info] Aucune ville détectée, utilisation de la ville par défaut : {commune}")
            else:
                if not city_input:
                    print(f"[Info] Ville détectée par l'IA : {commune}")
                else:
                    # Surcharger la ville extraite par la ville saisie par l'utilisateur
                    extracted_data["usager.localisation.commune_residence"] = commune

            # Affichage structuré du Schéma Pivot rempli par l'extraction IA
            print("\n" + "=" * 70)
            print("--- SCHÉMA PIVOT ORIA (Données Cliniques Extraites par l'IA) ---")
            print("=" * 70)
            
            base_fields = {k: v for k, v in extracted_data.items() if not k.startswith("evaluation.comid.")}
            comid_fields = {k.replace("evaluation.comid.", ""): v for k, v in extracted_data.items() if k.startswith("evaluation.comid.")}
            
            print("\n[Variables Administratives & Cliniques] :")
            print(json.dumps(base_fields, indent=2, ensure_ascii=False))
            
            print("\n[Critères COMID Détectés (True)] :")
            detected_comid = [k for k, v in comid_fields.items() if v is True]
            print(json.dumps(detected_comid, indent=2, ensure_ascii=False))
            print("=" * 70 + "\n")

            # 2. Boucle d'affinage clinique interactif
            print("Recherche de précisions cliniques facultatives...")
            
            # Évaluation initiale pour afficher la recommandation préliminaire
            comid_results = scoring_engine.calculate_comid_score(extracted_data)
            orientation_results = orientation_engine.evaluate_orientation(extracted_data, comid_results)
            initial_vainqueur = orientation_results[0]['label'] if orientation_results else "Aucune structure"
            print(f"[Analyse préliminaire] Première orientation identifiée : {initial_vainqueur}")
            
            # Initialisation des flags de questions pour éviter les boucles infinies
            extracted_data["evaluation.comid.apa_asked"] = False
            extracted_data["evaluation.comid.gir_asked"] = False
            extracted_data["evaluation.comid.opposition_soins_asked"] = False

            while True:
                # Recalculer l'orientation pour chaque itération
                current_comid_results = scoring_engine.calculate_comid_score(extracted_data)
                current_orientations = orientation_engine.evaluate_orientation(extracted_data, current_comid_results)
                
                eligible_types = [o['structure_type'] for o in current_orientations if o.get('eligible')]
                vainqueur_actuel_type = current_orientations[0]['structure_type'] if current_orientations else None
                vainqueur_actuel_label = current_orientations[0]['label'] if current_orientations else "Aucune structure"
                
                # Évaluer les conditions d'affinage
                # Condition A : APA inconnu, problématique sociale présente, vainqueur n'est ni Police ni CEV.
                needs_apa_check = (
                    extracted_data.get("usager.situation_actuelle.APA") in ["inconnu", "non_renseigne", None]
                    and vainqueur_actuel_type not in ["POLICE", "CEV"]
                    and any(t in eligible_types for t in ["CLIC", "UTS", "CCAS", "CRT"])
                    and not extracted_data.get("evaluation.comid.apa_asked")
                )
                
                # Condition B : Hésitation CLIC / CRT (maintien à domicile concerné), et GIR non renseigné (None ou inconnu)
                needs_gir_check = (
                    extracted_data.get("usager.situation_actuelle.GIR") is None
                    and any(t in eligible_types for t in ["CLIC", "CRT"])
                    and not extracted_data.get("evaluation.comid.gir_asked")
                )
                
                # Condition C : Rupture ou refus possible, opposition_soins est False, vainqueur n'est ni Police ni CEV, mais motif lié à maintien/aides/secours.
                needs_opposition_check = (
                    not extracted_data.get("evaluation.comid.opposition_soins", False)
                    and vainqueur_actuel_type not in ["POLICE", "CEV"]
                    and extracted_data.get("demande.motif_principal") in ["maintien_a_domicile", "sortie_hospitalisation", "refus_de_soins", "refus_aide_domicile", "aide_alimentaire", "secours_urgence"]
                    and not extracted_data.get("evaluation.comid.opposition_soins_asked")
                )
                
                # Poser la première question admissible
                if needs_apa_check:
                    extracted_data["evaluation.comid.apa_asked"] = True
                    print("\n[Affinage] Question : L'usager bénéficie-t-il déjà de l'APA (Allocation Personnalisée d'Autonomie) ?")
                    ans = input("  > [oui / non / inconnu] : ").strip().lower()
                    if ans in ["oui", "o", "yes", "y"]:
                        extracted_data["usager.situation_actuelle.APA"] = "oui"
                    elif ans in ["non", "n", "no"]:
                        extracted_data["usager.situation_actuelle.APA"] = "non"
                    else:
                        extracted_data["usager.situation_actuelle.APA"] = "inconnu"
                    print(f"  --> [Mise à jour Schéma Pivot] 'usager.situation_actuelle.APA' = '{extracted_data['usager.situation_actuelle.APA']}'")
                    
                elif needs_gir_check:
                    extracted_data["evaluation.comid.gir_asked"] = True
                    print("\n[Affinage] Question : Quel est le niveau de perte d'autonomie (GIR) de l'usager si connu ?")
                    ans = input("  > [Chiffre de 1 à 6, ou appuyez sur Entrée si inconnu] : ").strip()
                    if ans.isdigit() and 1 <= int(ans) <= 6:
                        extracted_data["usager.situation_actuelle.GIR"] = int(ans)
                    else:
                        extracted_data["usager.situation_actuelle.GIR"] = "inconnu"
                    print(f"  --> [Mise à jour Schéma Pivot] 'usager.situation_actuelle.GIR' = '{extracted_data['usager.situation_actuelle.GIR']}'")
                        
                elif needs_opposition_check:
                    extracted_data["evaluation.comid.opposition_soins_asked"] = True
                    print("\n[Affinage] Question : L'usager s'oppose-t-il activement aux soins ou aux aides à domicile proposés ?")
                    print("  *(ex: refuse l'entrée de l'auxiliaire de vie, dit 'je n'ai besoin de rien', refuse les soins)*")
                    ans = input("  > [oui / non] : ").strip().lower()
                    if ans in ["oui", "o", "yes", "y"]:
                        extracted_data["evaluation.comid.opposition_soins"] = True
                    else:
                        extracted_data["evaluation.comid.opposition_soins"] = False
                    print(f"  --> [Mise à jour Schéma Pivot] 'evaluation.comid.opposition_soins' = {extracted_data['evaluation.comid.opposition_soins']}")
                
                else:
                    # Plus aucune question à poser
                    break
                
                # Évaluer si la recommandation principale a changé après la réponse
                new_comid_results = scoring_engine.calculate_comid_score(extracted_data)
                new_orientations = orientation_engine.evaluate_orientation(extracted_data, new_comid_results)
                new_vainqueur_label = new_orientations[0]['label'] if new_orientations else "Aucune structure"
                
                if new_vainqueur_label != vainqueur_actuel_label:
                    print(f"  ==> [AFFINAGE] L'orientation principale a évolué :")
                    print(f"      Avant : {vainqueur_actuel_label}")
                    print(f"      Après : {new_vainqueur_label}")
            
            # Recalcul final après toutes les réponses
            comid_results = scoring_engine.calculate_comid_score(extracted_data)
            orientation_results = orientation_engine.evaluate_orientation(extracted_data, comid_results)
            results_with_contacts = territory_manager.get_contacts_for_structures(orientation_results, commune)

            # 3. Affichage des résultats finaux
            print(f"\n--- RECOMMANDATIONS D'ORIENTATION FINALES POUR LE TERRITOIRE DE : {commune.upper()} ---")
            afficher_orientations(results_with_contacts)
            print("\n" + "=" * 70 + "\n")

        except Exception as e:
            import traceback
            print(f"\n[Erreur] Une erreur s'est produite lors de l'évaluation : {e}")
            traceback.print_exc()

if __name__ == "__main__":
    try:
        asyncio.run(interactive_loop())
    except KeyboardInterrupt:
        print("\nMerci d'avoir utilisé ORIA. À bientôt !")
