import json

ref_path = r"c:\Users\milac\Documents\Projet ORIA\prototype-ORIA\config\referentials\referentiel_territoire.json"
with open(ref_path, "r", encoding="utf-8") as f:
    ref = json.load(f)

for commune, data in ref.items():
    print(f"Commune: {commune}")
    for struct_type, struct_data in data.items():
        if "ccas" in struct_type.lower():
            print(f"  {struct_type}: {struct_data}")
