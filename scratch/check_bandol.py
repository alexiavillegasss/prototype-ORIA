import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

ref_path = r"c:\Users\milac\Documents\Projet ORIA\prototype-ORIA\config\referentials\referentiel_territoire.json"
with open(ref_path, 'r', encoding='utf-8') as f:
    ref = json.load(f)

print("=== BANDOL STRUCTURES ===")
for city, data in ref.items():
    if "bandol" in city.lower():
        print(f"City: {city}")
        print(json.dumps(data, indent=2, ensure_ascii=False))
