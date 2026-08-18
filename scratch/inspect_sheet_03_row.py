import pandas as pd
import sys

sys.stdout.reconfigure(encoding='utf-8')

excel_path = r"c:\Users\milac\Documents\Projet ORIA\prototype-ORIA\config\rules\tableau_besoins_orientation_oria.xlsx"
df = pd.read_excel(excel_path, sheet_name="03_Points_nouveau_moteur")

targets = ["Perte d’autonomie récente", "Multimorbidité"]

for t in targets:
    print(f"\nSearching for '{t}' in Sheet 3:")
    sub_df = df[df['Besoin détaillé'].str.contains(t, case=False, na=False)]
    for idx, row in sub_df.iterrows():
        print(f"Row {idx}:")
        for col in df.columns:
            val = row[col]
            if pd.notna(val):
                print(f"  {col}: {repr(val)}")
