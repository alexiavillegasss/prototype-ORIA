import asyncio
import os
import sys
import json

# Ajout du chemin pour importer les modules du backend
sys.path.append(os.path.join(os.getcwd(), 'backend', 'src'))

from ai.extraction.extractor import SignalExtractor
from application.scoring_engine import ScoringEngine
from application.orientation_engine import OrientationEngine
from application.territory_manager import TerritoryManager
from application.pdf_generator import PDFGenerator
from ai.extraction.fiche_extractor import FicheDACExtractor
from infrastructure.database import DatabaseManager

async def run_interactive():
    BASE_DIR = os.getcwd()
    SCHEMA_PATH = os.path.join(BASE_DIR, 'config', 'schemas', 'schema_definition.json')
    COMID_PATH = os.path.join(BASE_DIR, 'config', 'rules', 'COMID.json')
    ORIENTATION_RULES_PATH = os.path.join(BASE_DIR, 'config', 'rules', 'orientation_rules.json')
    TERRITORY_PATH = os.path.join(BASE_DIR, 'config', 'referentials', 'referentiel_territoire.json')
    DB_PATH = os.path.join(BASE_DIR, 'oria_database.db')

    print("Initialisation des moteurs IA... (Cela peut prendre quelques secondes)")
    extractor = SignalExtractor(schema_path=SCHEMA_PATH, comid_path=COMID_PATH)
    scoring_engine = ScoringEngine(comid_rules_path=COMID_PATH)
    orientation_engine = OrientationEngine(rules_path=ORIENTATION_RULES_PATH)
    territory_manager = TerritoryManager(territory_rules_path=TERRITORY_PATH)
    db_manager = DatabaseManager(db_path=DB_PATH)
    pdf_generator = PDFGenerator(template_path=os.path.join(BASE_DIR, 'backend', 'src', 'static', 'fiche_dac_vierge.pdf'))
    fiche_extractor = FicheDACExtractor()
    print("Pret ! Moteurs charges.\n")

    while True:
        print("="*60)
        print("Saisissez la description du cas (ou tapez 'quitter' pour arreter) :")
        print("Astuce: vous pouvez taper sur plusieurs lignes. Tapez 'FIN' sur une ligne vide pour lancer l'analyse.")
        print("-" * 60)
        
        lines = []
        while True:
            try:
                line = input()
            except EOFError:
                break
            
            if line.strip().lower() == 'quitter':
                print("Fermeture du terminal interactif. A bientot !")
                return
            if line.strip().upper() == 'FIN':
                break
            lines.append(line)
            
        text = "\n".join(lines).strip()
        
        if not text:
            print("Aucun texte saisi. Reessayez.")
            continue

        print("\n[1/4] Extraction IA en cours...")
        try:
            extracted_data = await extractor.extract(text)
        except Exception as e:
            print(f"Erreur lors de l'extraction : {e}")
            continue
        
        print("\n[2/4] Calcul de la complexite (COMID)...")
        comid_results = scoring_engine.calculate_comid_score(extracted_data)
        print(f"  -> Score : {comid_results['score_total']} / Niveau : {comid_results['label']}")

        print("\n[3/4] Evaluation de l'orientation...")
        orientation_results = orientation_engine.evaluate_orientation(extracted_data, comid_results)

        commune = extracted_data.get('usager.localisation.commune_residence', 'Inconnue')
        print(f"\n[4/4] Recherche de contacts sur le territoire (Commune: {commune})...")
        results_with_contacts = territory_manager.get_contacts_for_structures(orientation_results, commune)

        print("\n" + "="*20 + " RESULTAT " + "="*20)
        if not results_with_contacts:
            print("Aucune structure eligible detectee.")
        for struct in results_with_contacts:
            print(f"\n[ {struct['label']} ] - Priorite : {struct.get('priorite', 'N/A')}")
            print(f"Objectif : {struct.get('objectif', 'N/A')}")
            if struct.get("telephone") or struct.get("adresse"):
                print(f"Contact : {struct.get('telephone', 'N/A')} | {struct.get('adresse', 'N/A')}")
            else:
                print("Contact : Non trouve dans le referentiel territorial")
                
        # Sauvegarde BDD
        try:
            safe_text = extractor.anonymizer.pseudonymize(text)
            details = {
                "orientation_results": orientation_results,
                "orientation_with_contacts": results_with_contacts
            }
            dossier_id = db_manager.save_dossier(
                texte_original=safe_text,
                donnees_extraites=extracted_data,
                score_comid=comid_results["score_total"],
                niveau_comid=comid_results["label"],
                structures_orientations=results_with_contacts,
                details_complet=details
            )
            print(f"\n[✓] Dossier anonymise et sauvegarde en base de donnees avec succes (ID: {dossier_id}).")
        except Exception as e:
            print(f"\n[X] Erreur lors de la sauvegarde : {e}")
            
        # Option to generate PDF
        gen_pdf = input("\nVoulez-vous preparer la Fiche d'Orientation DAC ? (o/n) : ")
        if gen_pdf.strip().lower() == 'o':
            print("Extraction specifique des donnees pour la fiche (cela peut prendre un instant)...")
            try:
                extracted_dac_data = await fiche_extractor.extract_for_dac(text)
                
                current_text = text
                
                # Check for missing critical info
                missing_info = []
                # Helper function to check if a field is truly missing (empty, but not explicitly INCONNU)
                def is_missing(val):
                    return not val or val.strip() == ""

                def is_inconnu(val):
                    return str(val).strip().upper() == "INCONNU"

                if is_missing(extracted_dac_data.get("nom_usage")) and is_missing(extracted_dac_data.get("nom_naissance")):
                    if not (is_inconnu(extracted_dac_data.get("nom_usage")) or is_inconnu(extracted_dac_data.get("nom_naissance"))):
                        missing_info.append("Nom du patient")
                        
                if is_missing(extracted_dac_data.get("date_naissance")) and not is_inconnu(extracted_dac_data.get("date_naissance")):
                    missing_info.append("Date de naissance")
                    
                if is_missing(extracted_dac_data.get("adresse_complete")) and not is_inconnu(extracted_dac_data.get("adresse_complete")):
                    missing_info.append("Adresse complete")
                    
                if is_missing(extracted_dac_data.get("vit_seul")) and not is_inconnu(extracted_dac_data.get("vit_seul")):
                    missing_info.append("Vit seul (Oui/Non)")
                    
                if is_missing(extracted_dac_data.get("apa")) and not is_inconnu(extracted_dac_data.get("apa")):
                    missing_info.append("Bénéficiaire de l'APA (Oui/Non)")
                    
                if extracted_dac_data.get("alertes", {}).get("hospit_recente"):
                    date_h = extracted_dac_data.get("alertes", {}).get("hospit_date")
                    motif_h = extracted_dac_data.get("alertes", {}).get("hospit_motif")
                    if (is_missing(date_h) or is_missing(motif_h)) and not (is_inconnu(date_h) or is_inconnu(motif_h)):
                        missing_info.append("Date exacte et motif de l'hospitalisation")
                        
                cercle = extracted_dac_data.get("cercle_de_soins", [])
                
                has_medecin = any(pro.get("type") == "medecin_traitant" for pro in cercle)
                if not has_medecin:
                    missing_info.append("Médecin traitant (Nom et Téléphone)")
                
                for pro in cercle:
                    nom = pro.get("nom", "")
                    tel = pro.get("tel", "")
                    pro_type = pro.get("type", "intervenant")
                    
                    # Si nom ou tel est manquant et non "INCONNU"
                    nom_missing = is_missing(nom) and not is_inconnu(nom)
                    tel_missing = is_missing(tel) and not is_inconnu(tel)
                    
                    if nom_missing or tel_missing:
                        manque = []
                        if nom_missing: manque.append("Nom")
                        if tel_missing: manque.append("Téléphone")
                        missing_info.append(f"Coordonnées pour {pro_type.upper()} ({' et '.join(manque)})")
                    
                if missing_info:
                    print("\n" + "!"*50)
                    print(" /!\\ INFORMATIONS MANQUANTES POUR UNE PRISE EN CHARGE OPTIMALE :")
                    for info in missing_info:
                        print(f"  - {info}")
                    print("!"*50)
                    print("\nQue souhaitez-vous faire ?")
                    print("[1] Ajouter des precisions (dicter/taper les infos manquantes)")
                    print("[2] Generer le PDF tel quel (vous le completerez a la main)")
                    choix = input("Votre choix (1 ou 2) : ").strip()
                    
                    if choix == '1':
                        print("\n--- Saisie des informations manquantes ---")
                        precisions = ""
                        for info in missing_info:
                            rep = input(f" {info} : ").strip()
                            if rep:
                                precisions += f"\n- Pour {info} : {rep}"
                    elif choix != '2' and len(choix) > 2:
                        precisions = choix
                    else:
                        precisions = None
                        
                    if precisions:
                        print("\nMise a jour du dossier en cours...")
                        current_text += f"\n\n[PRECISIONS APPORTEES PAR L'UTILISATEUR SUITE AUX MANQUEMENTS] :{precisions}"
                        extracted_dac_data = await fiche_extractor.extract_for_dac(current_text)
                
                print("\nGeneration du PDF...")
                pdf_bytes = pdf_generator.generate_dac_pdf(extracted_dac_data)
                
                output_pdf = os.path.join(BASE_DIR, "export_fiche_dac.pdf")
                with open(output_pdf, "wb") as f:
                    f.write(pdf_bytes)
                print(f"[✓] Fiche DAC generee avec succes : {output_pdf}")
            except Exception as e:
                print(f"[X] Erreur lors de la generation du PDF : {e}")

        print("\nAppuyez sur Entree pour saisir un nouveau cas...")
        input()

if __name__ == "__main__":
    try:
        asyncio.run(run_interactive())
    except KeyboardInterrupt:
        print("\nFermeture du programme.")
