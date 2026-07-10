import pandas as pd
import sys

sys.stdout.reconfigure(encoding='utf-8')

excel_path = r"c:\Users\milac\Documents\Projet ORIA\prototype-ORIA\config\rules\tableau_oria.xlsx"
df = pd.read_excel(excel_path, sheet_name="02_Besoins_x_structures (2)")

print("Sheet 2 columns:")
for i, col in enumerate(df.columns):
    print(f"Col {i}: {repr(col)}")

print("\nTotal needs:", len(df))
print("\nFirst 10 needs:")
for idx, row in df.head(10).iterrows():
    print(f"Row {idx}: {repr(row['Besoin détaillé'])} | Keywords: {repr(row['Mots-clés / critère moteur'])}")
