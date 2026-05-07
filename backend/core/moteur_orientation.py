import json

chemin_schema_pivot = "config/schemas/schema_pivot.json"
chemin_ref_territoire = "config/referentials/referentiel_territoire.json"

with open(chemin_schema_pivot, 'r', encoding='utf-8') as fichier:
    donnees_patient = json.load(fichier)

with open(chemin_ref_territoire, 'r', encoding='utf-8') as fichier :
    donnees_territoire = json.load(fichier)

commune = donnees_patient["usager"]["localisation"]["commune_residence"]
structure_presence = donnees_territoire[commune]["clic"]["present"]

print(f"Le patient habite à : {commune}")
print(f"Est ce que le CLIC est présent dans la commune du patient ? : {structure_presence}")