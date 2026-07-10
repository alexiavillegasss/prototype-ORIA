import pandas as pd
import sys

sys.stdout.reconfigure(encoding='utf-8')

excel_path = r"c:\Users\milac\Documents\Projet ORIA\prototype-ORIA\config\rules\tableau_oria.xlsx"
df1 = pd.read_excel(excel_path, sheet_name="01_Critère_prio_exclu")

for idx, row in df1.iterrows():
    detail = row.get("Critère détaillé")
    action = row.get("Action")
    struct = row.get("Structure")
    print(f"Row {idx}: {repr(detail)} | Action: {repr(action)} | Struct: {repr(struct)}")
