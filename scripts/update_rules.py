import json

filepath = 'c:\\Users\\milac\\Documents\\Projet ORIA\\prototype-ORIA\\config\\rules\\orientation_rules.json'

with open(filepath, 'r', encoding='utf-8') as f:
    rules = json.load(f)

for rule in rules.get('eligibility_rules', []):
    # Priorities updates
    if rule['structure_type'] == 'CRT':
        rule['result']['base_priority_score'] = 90
    elif rule['structure_type'] == 'CEV':
        rule['result']['base_priority_score'] = 95
    elif rule['structure_type'].startswith('CLIC'):
        rule['result']['base_priority_score'] = 80
    elif rule['structure_type'] == 'CCAS':
        rule['result']['base_priority_score'] = 75
    elif rule['structure_type'] == 'UTS':
        rule['result']['base_priority_score'] = 60
    elif rule['structure_type'] == 'CPTS':
        rule['result']['base_priority_score'] = 65
        # fix typo abscent -> absent
        for cond in rule['all_of']:
            if cond['field'] == "vulnerabilites.sante.suivi_medical.medecin_traitant" and cond['value'] == "abscent":
                cond['value'] = "absent"
    elif rule['structure_type'] == 'DAC':
        rule['result']['base_priority_score'] = 100
        # Add conditions for DAC: besoin de coordination, refus de soins, plusieurs problematiques
        new_conditions = [
            {
                "field": "demande.motif_principal",
                "operator": "contains_any",
                "value": ["coordination", "refus_de_soins", "complexite_medico_sociale"]
            },
            {
                "field": "demande.motifs_secondaires",
                "operator": "contains_any",
                "value": ["coordination", "refus_de_soins", "complexite_medico_sociale"]
            }
        ]
        rule['any_of'].extend(new_conditions)

with open(filepath, 'w', encoding='utf-8') as f:
    json.dump(rules, f, indent=4, ensure_ascii=False)
    
print("Rules updated successfully.")
