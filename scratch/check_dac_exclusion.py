import pandas as pd
import sys

sys.stdout.reconfigure(encoding='utf-8')

excel_path = r"c:\Users\milac\Documents\Projet ORIA\prototype-ORIA\config\rules\tableau_oria.xlsx"
df = pd.read_excel(excel_path, sheet_name="01_Critère_prio_exclu")

for idx, row in df.iterrows():
    action = row.get("Action")
    struct = row.get("Structure")
    critere = row.get("Critères prioritisation / exclusion ")
    if str(action).strip().lower() == "exclu" and "dac" in str(struct).lower():
        print(f"Row {idx}: {critere} -> Excludes {struct}")
