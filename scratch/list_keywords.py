import pandas as pd
import sys

sys.stdout.reconfigure(encoding='utf-8')

excel_path = r"c:\Users\milac\Documents\Projet ORIA\prototype-ORIA\config\rules\tableau_besoins_orientation_oria.xlsx"
df = pd.read_excel(excel_path, sheet_name="02_Besoins_x_structures")

print("Rows with 'Mots-clés / critère moteur':")
for idx, row in df.iterrows():
    if pd.isna(row['Besoin détaillé']):
        continue
    kw = row.get('Mots-clés / critère moteur')
    print(f"{idx}: '{row['Besoin détaillé']}' -> keywords: '{kw}'")
