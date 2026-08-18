import pandas as pd
import sys

sys.stdout.reconfigure(encoding='utf-8')

excel_path = r"c:\Users\milac\Documents\Projet ORIA\prototype-ORIA\config\rules\tableau_besoins_orientation_oria.xlsx"
df = pd.read_excel(excel_path, sheet_name="02_Besoins_x_structures")

structures = ['POLICE', 'CEV', 'SERVICE_SOCIAL_HOPITAL', 'CPTS', 'CLIC', 'CRT', 'DAC', 'UTS', 'CCAS', 'COMPAGNONS_BATISSEURS', 'PSCG_SS_APA']

targets = ["Perte d’autonomie récente", "Personne de 75 ans ou plus", "Multimorbidité", "Médecin traitant non identifié avec certitude"]

for t in targets:
    print(f"\nSearching for: '{t}'")
    # Match by substring
    sub_df = df[df['Besoin détaillé'].str.contains(t, case=False, na=False)]
    if sub_df.empty:
        print("  Not found!")
        continue
    for idx, row in sub_df.iterrows():
        print(f"Row {idx}:")
        print(f"  Besoin: {row['Besoin détaillé']}")
        print(f"  Keywords: {row['Mots-clés / critère moteur']}")
        print(f"  Structure principale proposée: {row['Structure principale proposée']}")
        cochees = []
        for s in structures:
            val = row.get(s)
            if pd.notna(val):
                cochees.append(f"{s}={repr(val)}")
        print(f"  Checked structures in Excel: {cochees}")
