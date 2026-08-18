import sys
import os
import asyncio
import json

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "backend", "src")))
from ai.extraction.extractor import SignalExtractor
from application.scoring_engine import ScoringEngine
from application.orientation_engine import OrientationEngine

sys.stdout.reconfigure(encoding='utf-8')

sc12_text = "Je suis assistante sociale, j’accompagne un monsieur de 36 ans, vivant à Toulon d’origine Afghane présent en France depuis plus de 20 ans, profil très précarisé depuis son arrivée en France, soucis administratifs qui ne lui ont pas permis de solliciter le droit d’asile, soucis avec des employeurs, soucis financiers, surendettement, expulsion, locative, ancien toxicomane, dit avoir arrêté de consommer de manière autonome, a besoin d’être accompagné et soutenu dans son parcours de soins: pas de médecin traitant, soins dentaires, santé mentale. Monsieur a des capacités, il parle correctement français, mais peine à mener à bien ses démarches du fait de la démotivation et de la difficulté à faire valoir ses droits."

async def run():
    BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    SCHEMA_PATH = os.path.join(BASE_DIR, 'config', 'schemas', 'schema_definition.json')
    COMID_PATH = os.path.join(BASE_DIR, 'config', 'rules', 'COMID.json')
    ORIENTATION_RULES_PATH = os.path.join(BASE_DIR, 'config', 'rules', 'orientation_rules.json')
    
    extractor = SignalExtractor(schema_path=SCHEMA_PATH, comid_path=COMID_PATH)
    scoring_engine = ScoringEngine(comid_rules_path=COMID_PATH)
    orientation_engine = OrientationEngine(rules_path=ORIENTATION_RULES_PATH)
    
    extracted_data = await extractor.extract(sc12_text)
    comid_results = scoring_engine.calculate_comid_score(extracted_data)
    
    print("evaluation.comid.addiction =", extracted_data.get("evaluation.comid.addiction"))
    print("evaluation.comid.psychiatrie =", extracted_data.get("evaluation.comid.psychiatrie"))
    print("evaluation.comid.depression =", extracted_data.get("evaluation.comid.depression"))
    
    results = orientation_engine.evaluate_orientation(extracted_data, comid_results, original_text=sc12_text)
    print("Results:", results)

asyncio.run(run())
