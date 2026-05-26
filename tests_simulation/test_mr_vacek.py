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

    print("--- Lancement du test ORIA : Cas M. Vacek (Habitat Indigne & Danger) ---")
    
    extractor = SignalExtractor(schema_path=SCHEMA_PATH, comid_path=COMID_PATH)
    scoring_engine = ScoringEngine(comid_rules_path=COMID_PATH)
    orientation_engine = OrientationEngine(rules_path=ORIENTATION_RULES_PATH)
    territory_manager = TerritoryManager(territory_rules_path=TERRITORY_PATH)

    text = """M. Vacek, 65 ans, habite à Toulon. Son appartement est insalubre : il n'a plus d'eau courante depuis 3 mois et le plafond de sa chambre menace de s'effondrer suite à une infiltration. Il vit dans l'humidité totale et il commence à avoir des problèmes respiratoires sérieux. Son propriétaire est un marchand de sommeil qui le menace physiquement s'il appelle la mairie. M. Vacek est terrifié, il n'a plus de revenus car son dossier de retraite est bloqué. Il dort dans sa cuisine avec un petit réchaud à gaz, ce qui est extrêmement dangereux."""

    print(f"\n1. Extraction IA pour la situation de péril...")
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

    print(f"\n--- REPONSE D'ORIA (URGENCE HABITAT) ---")
    if not results_with_contacts:
        print("ORIA : 'Contactez les pompiers ou la police immédiatement.'")
    else:
        best_struct = results_with_contacts[0]
        print(f"ORIA : 'La situation de M. Vacek présente un DANGER IMMINENT.'")
        print(f"\nVOTRE PRIORITÉ ABSOLUE : [ {best_struct['label']} ]")
        print(f"MISSION : {best_struct.get('objectif', 'N/A')}")
        print(f"CONTACT : {best_struct.get('telephone', 'N/A')}")
        
        # On affiche quand même le social car c'est la suite logique
        if len(results_with_contacts) > 1:
            second_struct = results_with_contacts[1]
            print(f"\nENSUITE (VOLET SOCIAL) : [ {second_struct['label']} ]")
            print(f"MISSION : {second_struct.get('objectif', 'N/A')}")

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
