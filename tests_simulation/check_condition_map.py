import os, sys
sys.path.append(os.path.join(os.getcwd(), 'backend', 'src'))
from application.orientation_engine import OrientationEngine

e = OrientationEngine('config/rules/orientation_rules.json')
e.set_matrix('cassi')
print("=== PRIORITIZATION RULES ===")
for r in e.prioritization_rules:
    in_map = r['detail'] in e.condition_map
    print(f"Prio: {repr(r['detail'])} -> in condition_map? {in_map}")

print("\n=== EXCLUSION RULES ===")
for r in e.exclusion_rules:
    in_map = r['detail'] in e.condition_map
    print(f"Exclu: {repr(r['detail'])} -> in condition_map? {in_map}")
