import pandas as pd

df = pd.read_excel('config/rules/tableauORIA - NOMENCLATURE-CASSI.xlsx', sheet_name='01_Critère_prio_exclu')
for idx, r in df.iterrows():
    action = str(r['Action']).strip()
    struct = str(r['Structure']).strip()
    crit = str(r['Critère détaillé']).strip()
    print(f"{idx:2d} | {action:15s} | {struct:22s} | {crit}")
