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
            
        print("\nAppuyez sur Entree pour saisir un nouveau cas...")
        input()

if __name__ == "__main__":
    try:
        asyncio.run(run_interactive())
    except KeyboardInterrupt:
        print("\nFermeture du programme.")
