import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

ref_path = r"c:\Users\milac\Documents\Projet ORIA\prototype-ORIA\config\referentials\referentiel_territoire.json"
with open(ref_path, "r", encoding="utf-8") as f:
    ref = json.load(f)

city = "La Seyne-sur-mer"
if city in ref:
    print(f"Data for {city}:")
    print(json.dumps(ref[city], indent=2, ensure_ascii=False))
