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

    text_initial = "M. Martin, résidant à La Seyne-sur-Mer, oublie parfois de s'alimenter et semble désorienté au quotidien. Sa voisine nous a contactés car elle s'inquiète beaucoup pour lui."

    # First run
    print("=== RUN 1 ===")
    extracted_1 = await extractor.extract(text_initial)
    comid_1 = scoring_engine.calculate_comid_score(extracted_1)
    orientation_1 = orientation_engine.evaluate_orientation(extracted_1, comid_1)
    print(f"Top structure: {orientation_1[0]['structure_type']}")
    
    missing_vars = orientation_engine.get_missing_critical_variables(extracted_1, orientation_1)
    print(f"Missing variables: {missing_vars}")
    questions = await extractor.generate_refinement_questions(text_initial, missing_vars)
    print(f"Questions (dict): {questions}")

    # Simulate answering "Non il n'a pas l'APA"
    print("\n=== RUN 2 (Answering Non to APA) ===")
    text_with_answers = text_initial + """\n\n[Précisions apportées par le professionnel] :
- Précision (age) : 80 ans
- Précision (apa) : Non il n'a pas l'APA
- Précision (aidant_regulier) : Non pas régulièrement m.martin n'as pas d'aidant"""

    extracted_2 = await extractor.extract(text_with_answers)
    comid_2 = scoring_engine.calculate_comid_score(extracted_2)
    orientation_2 = orientation_engine.evaluate_orientation(extracted_2, comid_2)
    
    print(f"Extracted APA value: {extracted_2.get('usager.situation_actuelle.APA')}")
    print(f"Extracted Age value: {extracted_2.get('usager.identite.age_estime')}")
    print(f"Extracted Aidant value: {extracted_2.get('usager.cadre_de_vie.aidant_regulier')}")
    
    print("\nTop orientations:")
    for s in orientation_2[:3]:
        print(f"  - {s['label']} (Priorité: {s.get('priorite')}, Confiance: {s.get('score_confiance')}%)")

if __name__ == "__main__":
    asyncio.run(main())
