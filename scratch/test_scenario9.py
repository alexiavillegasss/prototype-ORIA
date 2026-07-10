import sys
import os
import asyncio

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "backend", "src")))
from ai.extraction.extractor import SignalExtractor
from application.scoring_engine import ScoringEngine
from application.orientation_engine import OrientationEngine

sys.stdout.reconfigure(encoding='utf-8')

text = "Je suis la fille d’une femme de 88 ans dont le maintien à domicile est devenu trop compliqué par sa perte d’autonomie et son isolement. Elle souhaite intégrer un EHPAD mais nous n’avons pas les moyens pour payer. Je souhaite faire une demande d’aide sociale à l’hébergement."

async def test():
    extractor = SignalExtractor(schema_path='config/schemas/schema_definition.json', comid_path='config/rules/COMID.json')
    orientation_engine = OrientationEngine(rules_path='config/rules/orientation_rules.json')
    
    extracted_data = await extractor.extract(text)
    eval_context = {**extracted_data}
    text_lower = text.lower()
    
    print("=== SCENARIO 9 NEEDS MATCHING ===")
    for need in orientation_engine.needs_mapping:
        criteria_str = need["moteur_criteria"].lower()
        criteria_list = [c.strip() for c in criteria_str.split(",") if c.strip()]
        
        tech_matched = False
        for c in criteria_list:
            if orientation_engine._match_single_criterion(c, eval_context):
                tech_matched = True
                
        lex_matched = orientation_engine._is_need_identified_textual(need, text_lower)
        
        final_matched = orientation_engine._is_need_identified(need, eval_context, text_lower)
        if final_matched:
            print(f"Need: {need['detaille']} | Tech matched: {tech_matched} | Lex matched: {lex_matched}")

asyncio.run(test())
