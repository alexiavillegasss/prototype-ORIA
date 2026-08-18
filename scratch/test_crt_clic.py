import asyncio
import os
import sys

# Ajout du chemin pour importer les modules du backend
sys.path.append(os.path.join(os.getcwd(), 'backend', 'src'))

from ai.extraction.extractor import SignalExtractor
from application.scoring_engine import ScoringEngine
from application.orientation_engine import OrientationEngine

async def run_test(text, case_label):
    BASE_DIR = os.getcwd()
    SCHEMA_PATH = os.path.join(BASE_DIR, 'config', 'schemas', 'schema_definition.json')
    COMID_PATH = os.path.join(BASE_DIR, 'config', 'rules', 'COMID.json')
    ORIENTATION_RULES_PATH = os.path.join(BASE_DIR, 'config', 'rules', 'orientation_rules.json')

    extractor = SignalExtractor(schema_path=SCHEMA_PATH, comid_path=COMID_PATH)
    scoring_engine = ScoringEngine(comid_rules_path=COMID_PATH)
    orientation_engine = OrientationEngine(rules_path=ORIENTATION_RULES_PATH)

    print(f"\n=== TEST {case_label} ===")
    extracted_data = await extractor.extract(text)
    print(f"Extracted GIR: {extracted_data.get('usager.situation_actuelle.GIR')}")
    
    comid_results = scoring_engine.calculate_comid_score(extracted_data)
    orientation_results = orientation_engine.evaluate_orientation(extracted_data, comid_results)
    
    print("Top orientations:")
    for s in orientation_results[:3]:
        print(f"  - {s['label']} (Priorité: {s.get('priorite')}, Confiance: {s.get('score_confiance')}%)")

async def main():
    text_gir_1 = """Une famille cherche en urgence une alternative à l'EHPAD car l'aidant familial régulier qui s'occupe du patient au quotidien est totalement épuisé.

[Précisions apportées par le professionnel] :
- Précision (age) : 80
- Précision (apa) : non
- Précision (gir) : Oui,  1"""

    text_no_gir = """Une famille cherche en urgence une alternative à l'EHPAD car l'aidant familial régulier qui s'occupe du patient au quotidien est totalement épuisé.

[Précisions apportées par le professionnel] :
- Précision (age) : 70
- Précision (apa) : non
- Précision (gir) : non pas de GIR"""

    await run_test(text_gir_1, "GIR 1 (Attendu: CRT)")
    await run_test(text_no_gir, "Pas de GIR (Attendu: CLIC)")

if __name__ == "__main__":
    asyncio.run(main())
