import asyncio
import os
import sys

# Ajout du chemin pour importer les modules du backend
sys.path.append(os.path.join(os.getcwd(), 'backend', 'src'))

from ai.extraction.extractor import SignalExtractor

async def main():
    BASE_DIR = os.getcwd()
    SCHEMA_PATH = os.path.join(BASE_DIR, 'config', 'schemas', 'schema_definition.json')
    COMID_PATH = os.path.join(BASE_DIR, 'config', 'rules', 'COMID.json')

    extractor = SignalExtractor(schema_path=SCHEMA_PATH, comid_path=COMID_PATH)

    text = """M. Martin, résidant à La Seyne-sur-Mer, oublie parfois de s'alimenter et semble désorienté au quotidien. Sa voisine nous a contactés car elle s'inquiète beaucoup pour lui.

[Précisions apportées par le professionnel] :
- À la question "Quel est l'âge estimé du patient M. M., résidant à La Seyne-sur-Mer, qui oublie parfois de s'alimenter et semble désorienté au quotidien ?" : 80 ans
- À la question "Est-ce que M. M. bénéficie de l'APA (Allocation Personnalisée d'Autonomie) ?" : Non il n'a pas l'APA
- À la question "L'époux ou la voisine de M. M., qui a contacté les services, intervient-il comme aidant régulier pour le patient ?" : Non pas régulièrement m.martin n'as pas d'aidant"""

    res = await extractor.extract(text)
    
    print("Checking text_lower overrides:")
    text_lower = text.lower()
    cond1 = "déjà l'apa" in text_lower
    cond2 = "a l'apa" in text_lower
    cond3 = "bénéficie de l'apa" in text_lower
    print(f"  'déjà l'apa' in text_lower: {cond1}")
    print(f"  'a l'apa' in text_lower: {cond2}")
    print(f"  'bénéficie de l'apa' in text_lower: {cond3}")
    
    print("\n--- EXTRACTED MAPPED ---")
    print(f"usager.situation_actuelle.APA: {res.get('usager.situation_actuelle.APA')}")

if __name__ == "__main__":
    asyncio.run(main())
