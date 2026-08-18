import pandas as pd
import sys

sys.stdout.reconfigure(encoding='utf-8')

excel_path = r"c:\Users\milac\Documents\Projet ORIA\prototype-ORIA\config\rules\tableau_oria.xlsx"
df = pd.read_excel(excel_path, sheet_name="01_Critère_prio_exclu")

print("Sheet 1 contents:")
for idx, row in df.iterrows():
    print(f"Row {idx}:")
    for col in df.columns:
        print(f"  {col}: {repr(row[col])}")
