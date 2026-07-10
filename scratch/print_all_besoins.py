import pandas as pd
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

excel_path = r"c:\Users\milac\Documents\Projet ORIA\prototype-ORIA\config\rules\tableau_besoins_orientation_oria.xlsx"
df = pd.read_excel(excel_path, sheet_name="02_Besoins_x_structures")

structures = ['POLICE', 'CEV', 'SERVICE_SOCIAL_HOPITAL', 'CPTS', 'CLIC', 'CRT', 'DAC', 'UTS', 'CCAS', 'COMPAGNONS_BATISSEURS', 'PSCG_SS_APA']

besoins = []
for idx, row in df.iterrows():
    # If the row is empty or description is empty, skip
    if pd.isna(row['Besoin détaillé']):
        continue
    
    struct_checks = []
    for s in structures:
        val = row.get(s)
        if pd.notna(val) and (str(val).strip() == '✓' or str(val).strip() == 'x'):
            struct_checks.append(s)
            
    b = {
        "index": idx,
        "categorie": str(row['Catégorie']).strip() if pd.notna(row['Catégorie']) else "",
        "besoin_detaille": str(row['Besoin détaillé']).strip(),
        "mot_cles": str(row['Mots-clés / critère moteur']).strip() if pd.notna(row['Mots-clés / critère moteur']) else "",
        "besoin_principal": str(row['Besoin principal ?']).strip() if pd.notna(row['Besoin principal ?']) else "",
        "struct_proposee": str(row['Structure principale proposée']).strip() if pd.notna(row['Structure principale proposée']) else "",
        "structures_cochees": struct_checks
    }
    besoins.append(b)

print(json.dumps(besoins, indent=2, ensure_ascii=False))
