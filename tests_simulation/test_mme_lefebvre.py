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

    print("--- Lancement du test ORIA : Cas Mme Lefebvre ---")
    
    extractor = SignalExtractor(schema_path=SCHEMA_PATH, comid_path=COMID_PATH)
    scoring_engine = ScoringEngine(comid_rules_path=COMID_PATH)
    orientation_engine = OrientationEngine(rules_path=ORIENTATION_RULES_PATH)
    territory_manager = TerritoryManager(territory_rules_path=TERRITORY_PATH)

    text = "Mme Lefebvre, 65 ans, vit à La Garde. Elle est suivie pour une bipolarité depuis des années mais elle a arrêté son traitement le mois dernier. Elle consomme beaucoup d'alcool pour 'calmer ses angoisses' selon ses propres mots. Elle vit dans un appartement très encombré (Syndrome de Diogène suspecté) et ses voisins se plaignent d'odeurs fortes. Elle n'a plus de famille et refuse toute aide du service social, se montrant parfois très agressive verbalement quand on frappe à sa porte."

    print(f"\n1. Extraction IA pour : '{text[:50]}...'")
    try:
        extracted_data = await extractor.extract(text)
        print("Donnees extraites (JSON) :")
        print(json.dumps(extracted_data, indent=2, ensure_ascii=False))
    except Exception as e:
        print(f"Erreur extraction : {e}")
        return
    
    print("\n2. Calcul du score de complexité COMID...")
    comid_results = scoring_engine.calculate_comid_score(extracted_data)
    print(f"Score Total : {comid_results['score_total']} ({comid_results['label']})")

    print("\n3. Evaluation de l'orientation...")
    orientation_results = orientation_engine.evaluate_orientation(extracted_data, comid_results)

    print(f"\n4. Recherche des contacts territoriaux ({extracted_data.get('usager.localisation.commune_residence', 'La Garde')})...")
    commune = extracted_data.get('usager.localisation.commune_residence', 'La Garde')
    results_with_contacts = territory_manager.get_contacts_for_structures(orientation_results, commune)

    print("\n--- RESULTATS DE L'ORIENTATION ---")
    if not results_with_contacts:
        print("Aucune structure eligible detectee.")
    for struct in results_with_contacts:
        print(f"\n[ {struct['label']} ] - Priorite : {struct.get('priorite', 'N/A')}")
        print(f"Objectif : {struct.get('objectif', 'N/A')}")
        if struct.get("telephone") or struct.get("adresse"):
            print(f"Contact : {struct.get('telephone', 'N/A')} | {struct.get('adresse', 'N/A')}")
        else:
            print("Contact : Non trouve dans le referentiel territorial")

if __name__ == "__main__":
    asyncio.run(run_test())
