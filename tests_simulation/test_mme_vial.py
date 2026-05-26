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

    print("--- Lancement du test ORIA : Cas Mme Vial (Recherche Médecin Traitant) ---")
    
    extractor = SignalExtractor(schema_path=SCHEMA_PATH, comid_path=COMID_PATH)
    scoring_engine = ScoringEngine(comid_rules_path=COMID_PATH)
    orientation_engine = OrientationEngine(rules_path=ORIENTATION_RULES_PATH)
    territory_manager = TerritoryManager(territory_rules_path=TERRITORY_PATH)

    text = "Mme Vial, 82 ans, vient de s'installer à Toulon pour se rapprocher de sa fille. Elle souffre de diabète de type 2 et d'hypertension. Elle n'a plus de médecin traitant car elle a déménagé et son ancien cabinet est trop loin. Elle a appelé plusieurs médecins dans son nouveau quartier mais aucun ne prend de nouveaux patients. Elle commence à manquer de médicaments et elle est très angoissée par cette rupture de suivi médical. Sa fille travaille beaucoup et s'inquiète de ne pas trouver de solution pour sa mère."

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

    print(f"\n4. Recherche des contacts territoriaux...")
    commune_extraite = extracted_data.get('usager.localisation.commune_residence')
    print(f"Ville extraite par l'IA : {commune_extraite}")
    
    # Normalisation de la commune pour le référentiel territorial
    commune_cible = "Toulon - Canton 1, 2 et 3" # Valeur par défaut pour ce test
    if commune_extraite and "Toulon" in str(commune_extraite):
        commune_cible = "Toulon - Canton 1, 2 et 3"
    elif commune_extraite:
        commune_cible = commune_extraite

    results_with_contacts = territory_manager.get_contacts_for_structures(orientation_results, commune_cible)

    print(f"\n--- RESULTATS DE L'ORIENTATION (Territoire: {commune_cible}) ---")
    from oria_display import afficher_orientations
    afficher_orientations(results_with_contacts)

if __name__ == "__main__":
    asyncio.run(run_test())
