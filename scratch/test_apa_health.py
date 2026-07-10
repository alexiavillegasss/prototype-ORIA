import asyncio
import os
import sys

# Ajout du chemin pour importer les modules du backend
sys.path.append(os.path.join(os.getcwd(), 'backend', 'src'))

from ai.extraction.extractor import SignalExtractor
from application.scoring_engine import ScoringEngine
from application.orientation_engine import OrientationEngine

async def main():
    BASE_DIR = os.getcwd()
    SCHEMA_PATH = os.path.join(BASE_DIR, 'config', 'schemas', 'schema_definition.json')
    COMID_PATH = os.path.join(BASE_DIR, 'config', 'rules', 'COMID.json')
    ORIENTATION_RULES_PATH = os.path.join(BASE_DIR, 'config', 'rules', 'orientation_rules.json')

    extractor = SignalExtractor(schema_path=SCHEMA_PATH, comid_path=COMID_PATH)
    scoring_engine = ScoringEngine(comid_rules_path=COMID_PATH)
    orientation_engine = OrientationEngine(rules_path=ORIENTATION_RULES_PATH)

    text = "Mme Chantal (84 ans) vit avec sa fille qui l'accompagne quotidiennement en tant qu'aidante régulière. Elle bénéficie déjà de l'APA à domicile mais son état de santé général décline depuis quelques jours."

    print("Extraction...")
    extracted_data = await extractor.extract(text)
    
    print("\nÉvaluation COMID...")
    comid_results = scoring_engine.calculate_comid_score(extracted_data)
    print(f"COMID Results: {comid_results}")
    
    print("\nÉvaluation de l'orientation...")
    orientation_results = orientation_engine.evaluate_orientation(extracted_data, comid_results)
    
    print("\nTop orientations:")
    for s in orientation_results[:3]:
        print(f"  - {s['label']} (Priorité: {s.get('priorite')}, Confiance: {s.get('score_confiance')}%)")

if __name__ == "__main__":
    asyncio.run(main())
