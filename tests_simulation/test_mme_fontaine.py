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

    print("--- Lancement du test ORIA : Cas Mme Fontaine (Alerte Kiné) ---")
    
    extractor = SignalExtractor(schema_path=SCHEMA_PATH, comid_path=COMID_PATH)
    scoring_engine = ScoringEngine(comid_rules_path=COMID_PATH)
    orientation_engine = OrientationEngine(rules_path=ORIENTATION_RULES_PATH)
    territory_manager = TerritoryManager(territory_rules_path=TERRITORY_PATH)

    text = """Bonjour ORIA. Je suis kiné à Sanary. Je m'inquiète pour ma patiente, Mme Fontaine (85 ans). Je viens pour sa rééducation de la hanche, mais la situation dérape. Elle a perdu 5kg en un mois, son frigo est littéralement vide. Elle oublie ses médicaments contre la douleur, donc on ne peut plus faire les exercices. Mais le plus grave, c'est son fils qui vit avec elle : il est très agressif, il lui crie dessus et j'ai remarqué qu'il lui demande de l'argent de façon très insistante à chaque fois que je suis là. Elle a l'air terrorisée."""

    print(f"\n1. Extraction IA pour l'alerte du kiné...")
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

    print(f"\n4. Recherche des contacts territoriaux (Sanary-sur-Mer)...")
    results_with_contacts = territory_manager.get_contacts_for_structures(orientation_results, "Sanary-sur-Mer")

    print(f"\n--- REPONSE D'ORIA POUR LE KINE ---")
    if not results_with_contacts:
        print("ORIA : 'Alerte non traitée, contactez les services d'urgence.'")
    else:
        print(f"ORIA : 'Situation identifiée comme {comid_results['label']}. Voici les actions prioritaires :'")
        for struct in results_with_contacts:
            print(f"\nACTION : [ {struct['label']} ]")
            print(f"MOTIF : {struct.get('objectif', 'N/A')}")
            print(f"CONTACT : {struct.get('telephone', 'N/A')}")

    # Sauvegarde en Base de Données (anonymisée)
    try:
        from infrastructure.database import DatabaseManager
        db_path = os.path.join(BASE_DIR, 'oria_database.db')
        db_manager = DatabaseManager(db_path=db_path)
        safe_text = extractor.anonymizer.pseudonymize(text)
        db_manager.save_dossier(
            texte_original=safe_text,
            donnees_extraites=extracted_data,
            score_comid=comid_results["score_total"],
            niveau_comid=comid_results["label"],
            structures_orientations=results_with_contacts
        )
        print("\nBDD - Dossier sauvegardé avec succès en base de données de manière anonymisée.")
    except Exception as e:
        print(f"\nBDD - Erreur de sauvegarde : {e}")

if __name__ == "__main__":
    asyncio.run(run_test())
