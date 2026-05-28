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

    print("--- Lancement du test ORIA : Cas M. Lambert (Appel Infirmière) ---")
    
    extractor = SignalExtractor(schema_path=SCHEMA_PATH, comid_path=COMID_PATH)
    scoring_engine = ScoringEngine(comid_rules_path=COMID_PATH)
    orientation_engine = OrientationEngine(rules_path=ORIENTATION_RULES_PATH)
    territory_manager = TerritoryManager(territory_rules_path=TERRITORY_PATH)

    text = """Bonjour ORIA. Je suis infirmière libérale sur La Seyne. Je t'appelle parce que je suis perdue avec un de mes patients, M. Lambert (78 ans). C'est un monsieur d'habitude très digne, mais depuis 15 jours, c'est la chute libre. Il refuse que j'entre faire ses pansements, il me crie dessus et me dit que je veux l'empoisonner avec ses médicaments. Son appartement, qui était impeccable, est devenu un dépotoir : il y a des sacs poubelles partout et ça sent très fort l'urine. Il est veuf, sa famille est à Paris et ils ne décrochent plus le téléphone. Je ne sais pas si c'est une décompensation psy, un début d'Alzheimer ou juste de l'isolement qui tourne mal. Je ne sais plus qui appeler : le médecin ? les services sociaux ? la mairie ? Aide-moi."""

    print(f"\n1. Extraction IA pour le récit de l'infirmière...")
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

    print(f"\n4. Recherche des contacts territoriaux (La Seyne-sur-Mer)...")
    results_with_contacts = territory_manager.get_contacts_for_structures(orientation_results, "La Seyne-sur-Mer")

    print(f"\n--- REPONSE D'ORIA POUR L'INFIRMIERE ---")
    if not results_with_contacts:
        print("ORIA : 'Désolé, je n'ai pas trouvé de structure adaptée, contactez le médecin traitant.'")
    else:
        print(f"ORIA : 'D'après votre description, la situation de M. Lambert est {comid_results['label']}. Voici les priorités d'appel :'")
        for struct in results_with_contacts:
            print(f"\nCONTACTER : [ {struct['label']} ]")
            print(f"POURQUOI : {struct.get('objectif', 'N/A')}")
            print(f"CONTACT : {struct.get('telephone', 'N/A')} | {struct.get('adresse', 'N/A')}")

    # Sauvegarde en Base de Données (anonymisée)
    try:
        from infrastructure.database import DatabaseManager
        db_path = os.path.join(BASE_DIR, 'oria_database.db')
        db_manager = DatabaseManager(db_path=db_path)
        safe_text = extractor.anonymizer.pseudonymize(text)
        details = {
            "orientation_results": orientation_results,
            "orientation_with_contacts": results_with_contacts
        }
        db_manager.save_dossier(
            texte_original=safe_text,
            donnees_extraites=extracted_data,
            score_comid=comid_results["score_total"],
            niveau_comid=comid_results["label"],
            structures_orientations=results_with_contacts,
            details_complet=details
        )
        print("\nBDD - Dossier sauvegardé avec succès en base de données de manière anonymisée.")
    except Exception as e:
        print(f"\nBDD - Erreur de sauvegarde : {e}")

if __name__ == "__main__":
    asyncio.run(run_test())
