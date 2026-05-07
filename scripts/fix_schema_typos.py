import json

filepath = 'c:\\Users\\milac\\Documents\\Projet ORIA\\prototype-ORIA\\config\\schemas\\schema_definition.json'

with open(filepath, 'r', encoding='utf-8') as f:
    text = f.read()

# Replace typos
text = text.replace('"decription"', '"description"')
text = text.replace('suspiion_malveillance', 'suspicion_malveillance')
text = text.replace('téléphonne', 'téléphone')
text = text.replace('oientation', 'orientation')
text = text.replace('sauvergarde', 'sauvegarde')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(text)

print("Schema definition updated successfully.")
