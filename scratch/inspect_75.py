import pandas as pd
import sys

sys.stdout.reconfigure(encoding='utf-8')

excel_path = r"c:\Users\milac\Documents\Projet ORIA\prototype-ORIA\config\rules\tableau_besoins_orientation_oria.xlsx"
df = pd.read_excel(excel_path, sheet_name="02_Besoins_x_structures")

# Find the row
rows = df[df['Besoin détaillé'].str.contains("75", case=False, na=False)]

for idx, row in rows.iterrows():
    print(f"\nRow {idx}:")
    for col in df.columns:
        print(f"  {col}: {repr(row[col])}")
