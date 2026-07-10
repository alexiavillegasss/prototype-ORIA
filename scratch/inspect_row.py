import pandas as pd
import sys

sys.stdout.reconfigure(encoding='utf-8')

excel_path = r"c:\Users\milac\Documents\Projet ORIA\prototype-ORIA\config\rules\tableau_besoins_orientation_oria.xlsx"
df = pd.read_excel(excel_path, sheet_name="02_Besoins_x_structures")

# Find the row
row = df[df['Besoin détaillé'].str.contains("Perte d’autonomie récente", case=False, na=False)].iloc[0]

print("Columns and values for Perte d’autonomie récente:")
for col in df.columns:
    print(f"  {col}: {repr(row[col])}")
