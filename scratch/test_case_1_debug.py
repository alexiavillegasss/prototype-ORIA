import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "backend", "src")))
from application.orientation_engine import OrientationEngine

sys.stdout.reconfigure(encoding='utf-8')

extracted_1 = {
    "usager.identite.age_estime": 72,
    "usager.localisation.commune_residence": "La Seyne-sur-Mer",
    "demande.motif_principal": "dettes",
    "vulnerabilites.social.precarite": "averee"
}

rules_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "config", "rules", "orientation_rules.json"))
engine = OrientationEngine(rules_path)

eval_context = {**extracted_1}
eval_context["complexite.niveau"] = "simple"
eval_context["complexite.score_total"] = 0

print("=== Needs Identification for Case 1 ===")
for need in engine.needs_mapping:
    matched = engine._is_need_identified(need, eval_context, "dettes")
    if matched:
        print(f"Matched need: {need['detaille']} | Categ: {need['categorie']} | Key: {need['moteur_criteria']} | Structs: {need['structures_cochees']}")
