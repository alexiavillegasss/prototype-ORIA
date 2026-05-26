import asyncio
import os
import sys
import json

# Ajout du chemin pour importer les modules
sys.path.append(os.path.join(os.getcwd(), 'backend', 'src'))

from ai.extraction.extractor import SignalExtractor
from application.scoring_engine import ScoringEngine
from application.orientation_engine import OrientationEngine
from application.territory_manager import TerritoryManager

async def run_test():
    BASE_DIR = os.getcwd()
    SCHEMA_PATH = os.path.join(BASE_DIR, 'config', 'schemas', 'schema_definition.json')
    COMID_PATH = os.path.join(BASE_DIR, 'config', 'rules', 'COMID.json')
    ORIENTATION_RULES_PATH = os.path.join(BASE_DIR, 'config', 'rules', 'orientation_rules.json')
    TERRITORY_PATH = os.path.join(BASE_DIR, 'config', 'referentials', 'referentiel_territoire.json')

    print("--- Lancement du test ORIA : Cas Mme Martin (Détresse Aidant) ---")
    
    extractor = SignalExtractor(schema_path=SCHEMA_PATH, comid_path=COMID_PATH)
    scoring_engine = ScoringEngine(comid_rules_path=COMID_PATH)
    orientation_engine = OrientationEngine(rules_path=ORIENTATION_RULES_PATH)
    territory_manager = TerritoryManager(territory_rules_path=TERRITORY_PATH)

    text = """Bonjour ORIA. Je suis la fille de Mme Martin (82 ans) à Toulon. Je n'en peux plus, je craque. Je travaille à temps plein et je passe toutes mes soirées et mes week-ends chez elle. Ma mère commence à perdre la tête, elle laisse le gaz allumé, elle se relève la nuit et elle est tombée deux fois. Je ne dors plus, je pleure tout le temps au travail. J'ai peur de devenir méchante avec elle tellement je suis à bout. On n'a aucune aide à part l'infirmière le matin. Est-ce qu'il existe des solutions pour qu'elle soit en sécurité et pour que moi je puisse enfin souffler un peu ?"""

    print(f"\n1. Extraction IA pour le récit de l'aidante...")
    try:
        extracted_data = await extractor.extract(text)
        print("Donnees extraites (JSON) :")
        print(json.dumps(extracted_data, indent=2, ensure_ascii=False))
    except Exception as e:
        print(f"Erreur extraction : {e}")
        return
    
    print("\n2. Calcul du score de complexité COMID...")
    comid_results = scoring_engine.calculate_comid_score(extracted_data)
    print(f"Score Total : {comid_results['score_total']} ({comid_results['label']})")

    print("\n3. Evaluation de l'orientation...")
    orientation_results = orientation_engine.evaluate_orientation(extracted_data, comid_results)

    print(f"\n4. Recherche des contacts territoriaux (Toulon)...")
    results_with_contacts = territory_manager.get_contacts_for_structures(orientation_results, "Toulon")

    from oria_display import afficher_orientations
    if not results_with_contacts:
        print("ORIA : 'Je ne trouve pas de solution immediate, parlez-en au medecin traitant.'")
    else:
        print(f"ORIA : 'Je comprends votre epuisement. La situation de votre mere est {comid_results['label']}.'")
        afficher_orientations(results_with_contacts)
        
        if extracted_data.get('evaluation.comid.epuisement_aidant') == True:
            print("\nCONSEIL POUR VOUS : 'Pensez egalement a contacter une plateforme de repit pour aidants. Ces structures proposent du soutien psychologique pour vous permettre de souffler.'")

if __name__ == "__main__":
    asyncio.run(run_test())
