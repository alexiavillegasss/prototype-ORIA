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

    text = "Un usager âgé résidant dans le Var a fait une chute."
    
    print("1. Extraction des signaux...")
    extracted_data = await extractor.extract(text)
    
    print("\n2. Évaluation COMID...")
    comid_results = scoring_engine.calculate_comid_score(extracted_data)
    
    print("\n3. Évaluation de l'orientation...")
    orientation_results = orientation_engine.evaluate_orientation(extracted_data, comid_results)
    
    print("\n4. Détection du besoin d'affinement...")
    needs_refinement = False
    if not orientation_results or orientation_results[0].get("structure_type") == "BESOIN_INFOS":
        needs_refinement = True
    elif orientation_results[0].get("score_confiance", 100) < 40:
        needs_refinement = True
        
    print(f"  Needs refinement: {needs_refinement}")
    print(f"  Top structure: {orientation_results[0] if orientation_results else None}")
    
    if needs_refinement:
        missing_vars = orientation_engine.get_missing_critical_variables(extracted_data, orientation_results)
        print(f"  Missing vars: {missing_vars}")
        
        if missing_vars:
            print("\n5. Génération des questions d'affinement...")
            questions = await extractor.generate_refinement_questions(text, missing_vars)
            print(f"  Questions générées : {questions}")

if __name__ == "__main__":
    asyncio.run(main())
