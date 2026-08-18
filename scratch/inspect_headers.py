import pandas as pd
import sys

sys.stdout.reconfigure(encoding='utf-8')

excel_path = r"c:\Users\milac\Documents\Projet ORIA\prototype-ORIA\config\rules\tableau_besoins_orientation_oria.xlsx"
xl = pd.ExcelFile(excel_path)
df = pd.read_excel(excel_path, sheet_name="02_Besoins_x_structures")

print("Headers:")
for i, col in enumerate(df.columns):
    print(f"Col {i}: {repr(col)}")
