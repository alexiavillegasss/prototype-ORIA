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
from infrastructure.database import DatabaseManager

async def run_test():
    BASE_DIR = os.getcwd()
    SCHEMA_PATH = os.path.join(BASE_DIR, 'config', 'schemas', 'schema_definition.json')
    COMID_PATH = os.path.join(BASE_DIR, 'config', 'rules', 'COMID.json')
    ORIENTATION_RULES_PATH = os.path.join(BASE_DIR, 'config', 'rules', 'orientation_rules.json')
    TERRITORY_PATH = os.path.join(BASE_DIR, 'config', 'referentials', 'referentiel_territoire.json')

    print("--- Lancement du test ORIA : Cas Mme Huguette (Urgence Sociale / Protection) ---")
    
    # Initialisation de la chaîne ORIA
    extractor = SignalExtractor(schema_path=SCHEMA_PATH, comid_path=COMID_PATH)
    scoring_engine = ScoringEngine(comid_rules_path=COMID_PATH)
    orientation_engine = OrientationEngine(rules_path=ORIENTATION_RULES_PATH)
    territory_manager = TerritoryManager(territory_rules_path=TERRITORY_PATH)
    db = DatabaseManager(db_path=os.path.join(BASE_DIR, 'oria_database.db'))

    text = (
        "Mme Huguette, 79 ans, vit seule dans un logement insalubre et humide à La Valette du Var. "
        "Elle n'a pas l'APA et vit sous le seuil de pauvreté avec une infime pension de retraite. "
        "Une amie très proche s'inquiète : elle signale que le neveu d'Huguette, qui a procuration sur ses comptes bancaires, "
        "effectue des retraits d'argent massifs et répétés sans justification, laissant Huguette sans le moindre sou pour s'acheter de quoi manger. "
        "Huguette est terrifiée par son neveu et n'ose rien dire par peur de représailles."
    )

    print(f"\n1. Extraction IA (Temp=0.0) pour : '{text[:80]}...'")
    try:
        extracted_data = await extractor.extract(text)
        print("Données extraites (JSON) :")
        print(json.dumps(extracted_data, indent=2, ensure_ascii=False))
    except Exception as e:
        import traceback
        print("Erreur d'extraction de l'IA :")
        traceback.print_exc()
        return
    
    print("\n2. Calcul du score de complexité COMID...")
    comid_results = scoring_engine.calculate_comid_score(extracted_data)
    print(f"Score Total : {comid_results['score_total']} ({comid_results['label']})")

    print("\n3. Évaluation de l'orientation...")
    orientation_results = orientation_engine.evaluate_orientation(extracted_data, comid_results)

    print("\n4. Recherche des contacts territoriaux (La Valette)...")
    results_with_contacts = territory_manager.get_contacts_for_structures(orientation_results, "La Valette")

    print("\n--- RÉSULTATS DE L'ORIENTATION POUR MME HUGUETTE ---")
    if not results_with_contacts:
        print("Aucune structure éligible détectée.")
    for struct in results_with_contacts:
        print(f"\n[ {struct['label']} ] - Priorité : {struct.get('priorite', 'N/A')}")
        print(f"Objectif : {struct.get('objectif', 'N/A')}")
        if struct.get("telephone") or struct.get("adresse"):
            print(f"Contact : {struct.get('telephone', 'N/A')} | {struct.get('adresse', 'N/A')}")
        else:
            print("Contact : Non trouvé dans le référentiel territorial")

    print("\n5. Sauvegarde en Base de Données...")
    dossier_id = db.save_dossier(
        texte_original=text,
        donnees_extraites=extracted_data,
        score_comid=comid_results['score_total'],
        niveau_comid=comid_results['label'],
        structures_orientations=results_with_contacts
    )
    print(f"[DB] Succès ! Dossier sauvegardé dans 'oria_database.db' avec l'ID numéro {dossier_id}")

if __name__ == "__main__":
    asyncio.run(run_test())
