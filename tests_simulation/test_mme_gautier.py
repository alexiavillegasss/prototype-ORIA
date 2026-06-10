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

    print("--- Lancement du test ORIA : Cas Mme Jeanne Gautier (Très Complexe) ---")
    
    extractor = SignalExtractor(schema_path=SCHEMA_PATH, comid_path=COMID_PATH)
    scoring_engine = ScoringEngine(comid_rules_path=COMID_PATH)
    orientation_engine = OrientationEngine(rules_path=ORIENTATION_RULES_PATH)
    territory_manager = TerritoryManager(territory_rules_path=TERRITORY_PATH)

    text = (
        "Mme Jeanne Gautier, 90 ans, habite à Toulon. Elle traverse une période de transition majeure suite au "
        "décès récent de son époux, ce qui a déclenché une grave dépression clinique avec des idées noires. "
        "Elle souffre d'un diabète de type 2, d'une insuffisance cardiaque et d'une arthrose déformante qui "
        "lui causent des douleurs chroniques permanentes et intolérables. Son ordonnance est extrêmement lourde "
        "avec une polymédication de plus de 9 médicaments par jour. Elle présente des troubles cognitifs majeurs "
        "avec une perte de mémoire et une désorientation temporelle. Elle vit seule dans un logement insalubre et "
        "inadapté, situé au 3ème étage sans ascenseur. Sa retraite de 800 € ne lui permet plus de faire face à ses "
        "factures d'électricité, créant une grande précarité financière. Sa fille unique est en situation "
        "d'épuisement total de l'aidant régulier et ne peut plus l'assister. De plus, Mme Gautier est très angoissée "
        "par sa santé, mais elle s'oppose de manière hostile aux soins et refuse d'ouvrir aux infirmiers à domicile. "
        "Depuis sa chute récente avec fracture du poignet, elle présente une perte d'autonomie récente pour toutes les "
        "activités de la vie quotidienne. Son état de santé est instable et caractérisé par une forte imprévisibilité."
    )

    print(f"\n1. Extraction IA pour le cas très complexe...")
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

    print(f"\n4. Recherche des contacts territoriaux ({extracted_data.get('usager.localisation.commune_residence', 'Toulon')})...")
    commune = extracted_data.get('usager.localisation.commune_residence', 'Toulon')
    results_with_contacts = territory_manager.get_contacts_for_structures(orientation_results, commune)

    print("\n--- RESULTATS DE L'ORIENTATION ---")
    if not results_with_contacts:
        print("Aucune structure eligible detectee.")
    for struct in results_with_contacts:
        print(f"\n[ {struct['label']} ] - Priorite : {struct.get('priorite', 'N/A')}")
        print(f"Objectif : {struct.get('objectif', 'N/A')}")
        if struct.get("telephone") or struct.get("adresse"):
            print(f"Contact : {struct.get('telephone', 'N/A')} | {struct.get('adresse', 'N/A')}")
        else:
            print("Contact : Non trouve dans le referentiel territorial")

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
