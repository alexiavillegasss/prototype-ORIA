import pandas as pd
import sys

sys.stdout.reconfigure(encoding='utf-8')

excel_path = r"c:\Users\milac\Documents\Projet ORIA\prototype-ORIA\config\rules\tableau_besoins_orientation_oria.xlsx"
xl = pd.ExcelFile(excel_path)

print("Sheet names:", xl.sheet_names)

for sheet in xl.sheet_names:
    print(f"\n--- Sheet: {sheet} ---")
    df = pd.read_excel(excel_path, sheet_name=sheet)
    print(f"Shape: {df.shape}")
    print(f"Columns: {list(df.columns)}")
    print("First 3 rows:")
    print(df.head(3))
