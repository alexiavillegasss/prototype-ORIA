import pandas as pd
import sys

sys.stdout.reconfigure(encoding='utf-8')

excel_path = r"c:\Users\milac\Documents\Projet ORIA\prototype-ORIA\config\rules\tableau_oria.xlsx"
df = pd.read_excel(excel_path, sheet_name="02_Besoins_x_structures (2)")

for idx, row in df.iterrows():
    detail = row.get("Besoin détaillé")
    if any(word in str(detail).lower() for word in ["ehpad", "maintien renforcé", "aménagement", "médico-sociale"]):
        print(f"\nRow {idx}: {repr(detail)}")
        for col in df.columns:
            val = row.get(col)
            if pd.notna(val) and str(val).strip() in ['✓', 'x']:
                print(f"  - {col}: {val}")
