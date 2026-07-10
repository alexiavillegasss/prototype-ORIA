import pandas as pd
import sys

sys.stdout.reconfigure(encoding='utf-8')

excel_path = r"c:\Users\milac\Documents\Projet ORIA\prototype-ORIA\config\rules\tableau_oria.xlsx"
df = pd.read_excel(excel_path, sheet_name="02_Besoins_x_structures (2)")

for idx, row in df.iterrows():
    detail = row.get("Besoin détaillé")
    kw = row.get("Mots-clés / critère moteur")
    print(f"Row {idx}: {repr(detail)} | Key: {repr(kw)}")
