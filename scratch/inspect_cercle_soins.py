import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

schema_path = r"c:\Users\milac\Documents\Projet ORIA\prototype-ORIA\config\schemas\schema_definition.json"
with open(schema_path, 'r', encoding='utf-8') as f:
    schema = json.load(f)

for path in sorted(schema.keys()):
    if "cercle_de_soins" in path:
        print(f"=== {path} ===")
        print(json.dumps(schema[path], indent=2, ensure_ascii=False))
