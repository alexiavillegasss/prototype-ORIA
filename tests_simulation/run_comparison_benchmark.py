import os
import sys
import asyncio
import json

sys.path.append(os.path.join(os.getcwd(), 'backend', 'src'))

from ai.extraction.extractor import SignalExtractor
from application.scoring_engine import ScoringEngine
from application.orientation_engine import OrientationEngine

BASE_DIR = os.getcwd()
RULES_DIR = os.path.join(BASE_DIR, 'config', 'rules')
SCHEMA_PATH = os.path.join(BASE_DIR, 'config', 'schemas', 'schema_definition.json')
COMID_PATH = os.path.join(RULES_DIR, 'COMID.json')
ORIENTATION_RULES_PATH = os.path.join(RULES_DIR, 'orientation_rules.json')

extractor = SignalExtractor(schema_path=SCHEMA_PATH, comid_path=COMID_PATH, model="llama3")
scoring_engine = ScoringEngine(comid_rules_path=COMID_PATH)

engine_legacy = OrientationEngine(rules_path=ORIENTATION_RULES_PATH)
engine_legacy.excel_path = os.path.join(RULES_DIR, 'tableau_oria.xlsx')
engine_legacy._load_excel_rules()

engine_cassi = OrientationEngine(rules_path=ORIENTATION_RULES_PATH)
engine_cassi.excel_path = os.path.join(RULES_DIR, 'tableauORIA - NOMENCLATURE-CASSI.xlsx')
engine_cassi._load_excel_rules()

scenarios = [
    {
        "id": "Cas 2 - Mme Vial",
        "expected": "CPTS",
        "text": "Mme Vial, 82 ans, vient d'emménager à Toulon pour se rapprocher de sa fille. Elle souffre de diabète et d'hypertension. Elle n'a pas encore de médecin traitant dans la région et son ordonnance arrive à la fin. Elle est très angoissée à l'idée de ne pas pouvoir renouveler ses médicaments."
    },
    {
        "id": "Cas 4 - Mme Bernard",
        "expected": "CEV",
        "text": "Mme Bernard, 88 ans, habite à La Seyne-sur-Mer. Elle est très isolée. Une voisine signale que le petit-fils de Mme Bernard, qui vient la voir de temps en temps, semble lui voler de l'argent. Mme Bernard a été vue avec des ecchymoses suspectes sur les bras et elle semble terrorisée à l'idée de parler. Elle est très amaigrie et n'a plus de quoi s'acheter à manger car son compte est vide."
    },
    {
        "id": "Cas 12 - Mme Petit",
        "expected": "CCAS",
        "text": "Mme Petit, 78 ans, habite à La Garde. Elle vit seule et a une toute petite retraite de 900 euros. Ce mois-ci, après avoir payé son loyer et ses charges, son compte bancaire est à découvert. Elle n'a plus rien pour s'acheter à manger pour les 10 prochains jours et elle a reçu une lettre de rappel pour sa facture d'électricité. Elle demande si la mairie peut l'aider pour ses courses et pour ne pas avoir d'impayé."
    },
    {
        "id": "Cas 16 - M. Lambert",
        "expected": "DAC",
        "text": "Bonjour ORIA. Je suis infirmière libérale sur La Seyne. Je t'appelle parce que je suis perdue avec un de mes patients, M. Lambert (78 ans). C'est un monsieur d'habitude très digne, mais depuis 15 jours, c'est la chute libre. Il refuse que j'entre faire ses pansements, il me crie dessus et me dit que je veux l'empoisonner avec ses médicaments. Son appartement est devenu un dépotoir : il y a des sacs poubelles partout et ça sent très fort l'urine. Il est veuf, sa famille est à Paris et ils ne décrochent plus le téléphone. Aide-moi."
    }
]

async def run():
    print("=== Démarrage du comparatif Legacy vs CASSI ===")
    for sc in scenarios:
        print(f"\n--- {sc['id']} (Attendu: {sc['expected']}) ---")
        extracted_data = await extractor.extract(sc["text"])
        comid_results = scoring_engine.calculate_comid_score(extracted_data)
        
        # Legacy
        res_leg = engine_legacy.evaluate_orientation(extracted_data.copy(), comid_results, sc["text"])
        top_leg = res_leg[0]["structure_type"] if res_leg else "AUCUNE"
        needs_leg = [n["detaille"] for n in extracted_data.get("evaluation.moteur_points.besoins_identifies", [])]
        
        # CASSI
        res_cas = engine_cassi.evaluate_orientation(extracted_data.copy(), comid_results, sc["text"])
        top_cas = res_cas[0]["structure_type"] if res_cas else "AUCUNE"
        needs_cas = [n["detaille"] for n in extracted_data.get("evaluation.moteur_points.besoins_identifies", [])]
        
        print(f"Top Legacy: {top_leg} | Besoins ({len(needs_leg)}): {needs_leg[:3]}")
        print(f"Top CASSI : {top_cas} | Besoins ({len(needs_cas)}): {needs_cas[:3]}")
        
if __name__ == "__main__":
    asyncio.run(run())
