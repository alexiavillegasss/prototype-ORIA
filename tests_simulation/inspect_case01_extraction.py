import os, sys, asyncio
sys.path.append(os.path.join(os.getcwd(), 'backend', 'src'))
from ai.extraction.extractor import SignalExtractor

SCHEMA_PATH = 'config/schemas/schema_definition.json'
COMID_PATH = 'config/rules/COMID.json'
extractor = SignalExtractor(schema_path=SCHEMA_PATH, comid_path=COMID_PATH, model="llama3")

text = "Bonjour, je suis kinésithérapeute et j'intervient chez un Monsieur de 55 ans. Son voisin est très aidant mais je suspecte qu'il lui prenne de l'argent lors de ses passages. Je ne sais pas qui contacter pour faire un signalement pour protéger ce Monsieur. Merci pour votre aide."

async def run():
    data = await extractor.extract(text)
    print("ALL KEYS containing malveillance or spoliation or maltraitance:")
    for k, v in data.items():
        if any(x in k.lower() for x in ['malveillance', 'spoliation', 'maltraitance', 'danger', 'abus', 'finance']):
            print(f"  {k} = {repr(v)}")
    print("\nusager.situation_actuelle.suspicion_malveillance =", repr(data.get("usager.situation_actuelle.suspicion_malveillance")))

asyncio.run(run())
