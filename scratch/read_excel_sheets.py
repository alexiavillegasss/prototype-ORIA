import pandas as pd
import os

excel_path = r"c:\Users\milac\Documents\Projet ORIA\prototype-ORIA\config\rules\tableau_besoins_orientation_oria.xlsx"

xl = pd.ExcelFile(excel_path)
print("Available sheets:", xl.sheet_names)

for sheet in xl.sheet_names:
    print(f"\n=========================================")
    print(f"SHEET: {sheet}")
    print(f"=========================================")
    try:
        df = pd.read_excel(excel_path, sheet_name=sheet)
        print("Columns:", df.columns.tolist())
        print("Shape:", df.shape)
        print("First 10 rows:")
        # We replace NaN with empty string for better printing
        print(df.head(10).fillna("").to_string())
    except Exception as e:
        print(f"Error reading {sheet}: {e}")
