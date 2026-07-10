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

    text = """Une famille cherche en urgence une alternative à l'EHPAD car l'aidant familial régulier qui s'occupe du patient au quotidien est totalement épuisé et le patient a besoin d'un maintien à domicile renforcé

[Précisions apportées par le professionnel] :
- Précision (age) : 75
- Précision (apa) : non
- Précision (gir) : Oui GIR 1"""

    print("Extraction...")
    extracted_data = await extractor.extract(text)
    
    gir_value = extracted_data.get('usager.situation_actuelle.GIR')
    print(f"Extracted GIR value: {gir_value} (Type: {type(gir_value)})")
    
    print("\nÉvaluation de l'orientation...")
    comid_results = scoring_engine.calculate_comid_score(extracted_data)
    orientation_results = orientation_engine.evaluate_orientation(extracted_data, comid_results)
    
    print("\nEligible orientations:")
    for s in orientation_results:
        print(f"  - {s['label']} (Priorité: {s.get('priorite')}, Confiance: {s.get('score_confiance')}%)")

if __name__ == "__main__":
    asyncio.run(main())
