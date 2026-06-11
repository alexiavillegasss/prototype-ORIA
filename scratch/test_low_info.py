import asyncio
import os
import sys
import json

sys.path.append(os.path.join(os.getcwd(), 'backend', 'src'))

from ai.extraction.extractor import SignalExtractor
from application.scoring_engine import ScoringEngine
from application.orientation_engine import OrientationEngine
from application.territory_manager import TerritoryManager

async def test_mme_martin():
    BASE_DIR = os.getcwd()
    SCHEMA_PATH = os.path.join(BASE_DIR, 'config', 'schemas', 'schema_definition.json')
    COMID_PATH = os.path.join(BASE_DIR, 'config', 'rules', 'COMID.json')
    ORIENTATION_RULES_PATH = os.path.join(BASE_DIR, 'config', 'rules', 'orientation_rules.json')
    TERRITORY_PATH = os.path.join(BASE_DIR, 'config', 'referentials', 'referentiel_territoire.json')

    orientation_engine = OrientationEngine(rules_path=ORIENTATION_RULES_PATH)
    territory_manager = TerritoryManager(territory_rules_path=TERRITORY_PATH)

    # Scenarios to test:
    # 1. Non-complex (COMID score = 5) -> Penalty -70%
    # 2. Pseudo-complex (COMID score = 7) -> Penalty -30%
    # 3. Complex (COMID score = 10) -> No penalty
    scenarios = [5, 7, 10]

    for score in scenarios:
        print(f"\n--- SCENARIO: Score COMID = {score} ---")
        mock_extracted_data = {
            "usager.identite.age_estime": 82,
            "usager.localisation.commune_residence": "Toulon",
            "complexite.score_total": score,
            "evaluation.confiance.variables": {},
            "evaluation.confiance.comid": {
                "epuisement_aidant": 95,
                "troubles_cognitifs": 95
            }
        }
        
        mock_comid_results = {
            "score_total": score,
            "niveau": "Situation complexe" if score >= 10 else ("Situation à risque" if score >= 6 else "Situation non complexe"),
            "label": "Situation complexe" if score >= 10 else ("Situation à risque" if score >= 6 else "Situation non complexe"),
            "items_detectes": []
        }

        orientation_results = orientation_engine.evaluate_orientation(mock_extracted_data, mock_comid_results)
        # Filter to only DAC for clarity
        dac_results = [s for s in orientation_results if s["structure_type"] == "DAC"]

        for struct in dac_results:
            print(f"[{struct['label']}] (Confiance : {struct.get('score_confiance')}% | Priorité : {struct.get('priorite')})")
            print(f"  Justification : {struct.get('explication_confiance')}")
            print(f"  Objectif : {struct['objectif']}")

if __name__ == "__main__":
    asyncio.run(test_mme_martin())
