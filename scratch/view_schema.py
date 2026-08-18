import json

schema_path = r"c:\Users\milac\Documents\Projet ORIA\prototype-ORIA\config\schemas\schema_definition.json"
with open(schema_path, "r", encoding="utf-8") as f:
    schema = json.load(f)

print("Root keys:", list(schema.keys()))
if "properties" in schema:
    print("Properties keys:", list(schema["properties"].keys()))

# Let's search for "besoin" in the schema keys and descriptions
def search_schema(obj, path=""):
    results = []
    if isinstance(obj, dict):
        for k, v in obj.items():
            current_path = f"{path}.{k}" if path else k
            if "besoin" in k.lower() or "need" in k.lower():
                results.append((current_path, type(v)))
            results.extend(search_schema(v, current_path))
    elif isinstance(obj, list):
        for i, item in enumerate(obj):
            results.extend(search_schema(item, f"{path}[{i}]"))
    return results

print("\nFields containing 'besoin' or 'need':")
for p, t in set(search_schema(schema)):
    # Let's keep it clean
    if "properties" in p:
        print(f"Path: {p}")
