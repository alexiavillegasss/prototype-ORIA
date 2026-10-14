import os
import sys
import pandas as pd

sys.path.append(os.path.join(os.getcwd(), 'backend', 'src'))
from application.orientation_engine import OrientationEngine

BASE_DIR = os.getcwd()
RULES_DIR = os.path.join(BASE_DIR, 'config', 'rules')
ORIENTATION_RULES_PATH = os.path.join(RULES_DIR, 'orientation_rules.json')

engine_legacy = OrientationEngine(rules_path=ORIENTATION_RULES_PATH)
engine_legacy.excel_path = os.path.join(RULES_DIR, 'tableau_oria.xlsx')
engine_legacy._load_excel_rules()

engine_cassi = OrientationEngine(rules_path=ORIENTATION_RULES_PATH)
engine_cassi.excel_path = os.path.join(RULES_DIR, 'tableauORIA - NOMENCLATURE-CASSI.xlsx')
engine_cassi._load_excel_rules()

# Situation de test avec maintien à domicile, aide alimentaire et épuisement aidant
test_text = "Mme Dupont a besoin d'une aide à domicile pour le ménage et la toilette. Son frigo est vide, elle a besoin d'un colis alimentaire et de portage de repas. Sa fille aidante est totalement épuisée et sollicite un séjour de répit."

eval_context = {
    "usager.identite.age_estime": 84,
    "evaluation.comid.epuisement_aidant": True,
    "evaluation.comid.precarite_sociale": True,
    "usager.cadre_de_vie.etat_logement": "propre"
}
comid_results = {"niveau": "Situation à risque", "score_total": 4}

res_leg = engine_legacy.evaluate_orientation(eval_context.copy(), comid_results, test_text)
data_leg = eval_context.copy()
engine_legacy.evaluate_orientation(data_leg, comid_results, test_text)
besoins_leg = data_leg.get("evaluation.moteur_points.besoins_identifies", [])

data_cas = eval_context.copy()
res_cas = engine_cassi.evaluate_orientation(data_cas, comid_results, test_text)
besoins_cas = data_cas.get("evaluation.moteur_points.besoins_identifies", [])

print("=== RESULTATS LEGACY ===")
print("Structures recommandées:", [r["structure_type"] for r in res_leg])
print("Scores:", data_leg.get("evaluation.moteur_points.scores", {}))
print(f"Besoins identifiés ({len(besoins_leg)}):")
for b in besoins_leg:
    print("  *", b)

print("\n=== RESULTATS CASSI (brut actuel) ===")
print("Structures recommandées:", [r["structure_type"] for r in res_cas])
print("Scores:", data_cas.get("evaluation.moteur_points.scores", {}))
print(f"Besoins identifiés ({len(besoins_cas)}):")
for b in besoins_cas:
    print("  *", b)
