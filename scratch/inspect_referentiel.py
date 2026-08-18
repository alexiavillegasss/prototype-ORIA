import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

ref_path = r"c:\Users\milac\Documents\Projet ORIA\prototype-ORIA\config\referentials\referentiel_territoire.json"
with open(ref_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

for key in data.keys():
    if "seyne" in key.lower():
        print(f"Key: {key}")
        structures = data[key].get("structures_disponibles", {})
        print("Available structures keys:", list(structures.keys()))
        # Print a few example structures
        for k in list(structures.keys())[:5]:
            print(f"  {k}: {structures[k]}")
