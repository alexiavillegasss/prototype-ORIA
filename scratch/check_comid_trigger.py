import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

comid_path = r"c:\Users\milac\Documents\Projet ORIA\prototype-ORIA\config\rules\COMID.json"
with open(comid_path, 'r', encoding='utf-8') as f:
    rules = json.load(f)

for category in rules.get("categories", []):
    print(f"\nCategory: {category.get('nom')}")
    for item in category.get("items", []):
        print(f"  - {item.get('code')}: {item.get('label')}")
