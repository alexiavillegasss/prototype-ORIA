import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

schema_path = r"c:\Users\milac\Documents\Projet ORIA\prototype-ORIA\config\schemas\schema_definition.json"
with open(schema_path, 'r', encoding='utf-8') as f:
    schema = json.load(f)

print("=== SCHEMA FIELDS ===")
for path in sorted(schema.keys()):
    if any(word in path.lower() for word in ["sante", "soins", "medecin", "paramed", "professionnel", "autonomie"]):
        print(f"{path}:")
        print(f"  Type: {schema[path].get('type')}")
        print(f"  Description: {schema[path].get('description')}")
        if 'enum' in schema[path]:
            print(f"  Enum: {schema[path]['enum']}")
