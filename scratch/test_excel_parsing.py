import pandas as pd
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

excel_path = r"c:\Users\milac\Documents\Projet ORIA\prototype-ORIA\config\rules\tableau_besoins_orientation_oria.xlsx"

# 1. Parse sheet 01_Exclusions_garde-fous
df1 = pd.read_excel(excel_path, sheet_name="01_Exclusions_garde-fous")
print("=== Sheet 1 Exclusions / Garde-fous ===")
for idx, row in df1.iterrows():
    moteur = row.get("Moteur")
    if moteur != "Nouveau moteur":
        continue
    
    rule_type = row.get("Type de règle")
    struct = row.get("Structure")
    action = row.get("Action")
    cond_str = row.get("Champs techniques / conditions")
    
    print(f"Rule: {rule_type} | Struct: {struct} | Action: {action}")
    if pd.notna(cond_str):
        try:
            conds = json.loads(cond_str)
            print(f"  Conditions parsed: {conds}")
        except Exception as e:
            print(f"  Error parsing conditions: {cond_str} -> {e}")

# 2. Parse sheet 02_Besoins_x_structures
df2 = pd.read_excel(excel_path, sheet_name="02_Besoins_x_structures")
structures = ['POLICE', 'CEV', 'SERVICE_SOCIAL_HOPITAL', 'CPTS', 'CLIC', 'CRT', 'DAC', 'UTS', 'CCAS', 'COMPAGNONS_BATISSEURS', 'PSCG_SS_APA']

print("\n=== Sheet 2 Needs x Structures ===")
count = 0
for idx, row in df2.iterrows():
    detail = row.get("Besoin détaillé")
    if pd.isna(detail):
        continue
    kw = row.get("Mots-clés / critère moteur")
    struct_cochees = []
    for s in structures:
        val = row.get(s)
        if pd.notna(val) and str(val).strip() in ['✓', 'x']:
            struct_cochees.append(s)
            
    print(f"Need: {detail[:50]}... | Keywords: {kw} | Structures: {struct_cochees}")
    count += 1
    if count >= 10:
        print("... and more ...")
        break
