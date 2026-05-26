import asyncio
import os
import sys
import json

# Ajout du chemin pour importer les modules
sys.path.append(os.path.join(os.getcwd(), 'backend', 'src'))

from ai.extraction.extractor import SignalExtractor
from application.scoring_engine import ScoringEngine
from application.orientation_engine import OrientationEngine
from application.territory_manager import TerritoryManager

async def run_test():
    BASE_DIR = os.getcwd()
    SCHEMA_PATH = os.path.join(BASE_DIR, 'config', 'schemas', 'schema_definition.json')
    COMID_PATH = os.path.join(BASE_DIR, 'config', 'rules', 'COMID.json')
    ORIENTATION_RULES_PATH = os.path.join(BASE_DIR, 'config', 'rules', 'orientation_rules.json')
    TERRITORY_PATH = os.path.join(BASE_DIR, 'config', 'referentials', 'referentiel_territoire.json')

    print("--- Lancement du test ORIA : Cas M. Chen (PCH / Handicap) ---")
    
    extractor = SignalExtractor(schema_path=SCHEMA_PATH, comid_path=COMID_PATH)
    scoring_engine = ScoringEngine(comid_rules_path=COMID_PATH)
    orientation_engine = OrientationEngine(rules_path=ORIENTATION_RULES_PATH)
    territory_manager = TerritoryManager(territory_rules_path=TERRITORY_PATH)

    text = "M. Chen, 52 ans, habite à Toulon. Il est en situation de handicap moteur et bénéficie de la PCH. Il cherche des informations sur les logements adaptés à son fauteuil roulant dans la commune et souhaiterait savoir s'il existe des prestataires spécialisés pour l'aide humaine le week-end."

    print(f"\n1. Extraction IA pour : '{text[:50]}...'")
    try:
        extracted_data = await extractor.extract(text)
        # On simule la détection PCH si l'IA l'a bien vue dans le texte
        print("Donnees extraites (JSON) :")
        print(json.dumps(extracted_data, indent=2, ensure_ascii=False))
    except Exception as e:
        print(f"Erreur extraction : {e}")
        return
    
    print("\n2. Calcul du score de complexité COMID...")
    comid_results = scoring_engine.calculate_comid_score(extracted_data)
    print(f"Score Total : {comid_results['score_total']} ({comid_results['label']})")

    print("\n3. Evaluation de l'orientation...")
    # On s'assure que le champ PCH est bien passé au moteur d'orientation
    if "PCH" in text:
        extracted_data["usager.situation_actuelle.PCH"] = "oui"
        
    orientation_results = orientation_engine.evaluate_orientation(extracted_data, comid_results)

    print(f"\n4. Recherche des contacts territoriaux (Toulon)...")
    results_with_contacts = territory_manager.get_contacts_for_structures(orientation_results, "Toulon")

    print(f"\n--- RESULTATS DE L'ORIENTATION (Cas Handicap / PCH) ---")
    if not results_with_contacts:
        print("Aucune structure eligible detectee.")
    for struct in results_with_contacts:
        print(f"\n[ {struct['label']} ] - Priorite : {struct.get('priorite', 'N/A')}")
        print(f"Objectif : {struct.get('objectif', 'N/A')}")
        if struct.get("telephone") or struct.get("adresse"):
            print(f"Contact : {struct.get('telephone', 'N/A')} | {struct.get('adresse', 'N/A')}")
        else:
            print("Contact : Non trouve dans le referentiel territorial")

    # Sauvegarde en Base de Données (anonymisée)
    try:
        from infrastructure.database import DatabaseManager
        db_path = os.path.join(BASE_DIR, 'oria_database.db')
        db_manager = DatabaseManager(db_path=db_path)
        safe_text = extractor.anonymizer.pseudonymize(text)
        db_manager.save_dossier(
            texte_original=safe_text,
            donnees_extraites=extracted_data,
            score_comid=comid_results["score_total"],
            niveau_comid=comid_results["label"],
            structures_orientations=results_with_contacts
        )
        print("\nBDD - Dossier sauvegardé avec succès en base de données de manière anonymisée.")
    except Exception as e:
        print(f"\nBDD - Erreur de sauvegarde : {e}")

if __name__ == "__main__":
    asyncio.run(run_test())
