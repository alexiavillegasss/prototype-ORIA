import pandas as pd
import sys

sys.stdout.reconfigure(encoding='utf-8')

excel_path = r"c:\Users\milac\Documents\Projet ORIA\prototype-ORIA\config\rules\tableau_oria.xlsx"
df = pd.read_excel(excel_path, sheet_name="02_Besoins_x_structures (2)")

structures = ['POLICE', 'CEV', 'SERVICE_SOCIAL_HOPITAL', 'CPTS', 'CLIC', 'CRT', 'DAC', 'UTS', 'CCAS', 'COMPAGNONS_BATISSEURS', 'PSCG_SS_APA', 'PRADO', 'MISAS', "fil d'argent", 'CONSULTATION MÉMOIRE']

print("=== CHECKED NEEDS IN NEW SHEET 02 ===")
for idx, row in df.iterrows():
    detail = row.get("Besoin détaillé")
    if pd.isna(detail):
        continue
    cochees = []
    for s in structures:
        val = row.get(s)
        if pd.notna(val) and str(val).strip() in ['✓', 'x']:
            cochees.append(s)
    if cochees:
        print(f"Row {idx}: '{detail}' -> {cochees}")
