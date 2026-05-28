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
from application.clarification_engine import ClarificationEngine

async def run_test():
    BASE_DIR = os.getcwd()
    SCHEMA_PATH = os.path.join(BASE_DIR, 'config', 'schemas', 'schema_definition.json')
    COMID_PATH = os.path.join(BASE_DIR, 'config', 'rules', 'COMID.json')
    ORIENTATION_RULES_PATH = os.path.join(BASE_DIR, 'config', 'rules', 'orientation_rules.json')
    TERRITORY_PATH = os.path.join(BASE_DIR, 'config', 'referentials', 'referentiel_territoire.json')

    print("--- Lancement du test : Moteur de Clarification & Validation Humaine ---")
    
    extractor = SignalExtractor(schema_path=SCHEMA_PATH, comid_path=COMID_PATH)
    scoring_engine = ScoringEngine(comid_rules_path=COMID_PATH)
    orientation_engine = OrientationEngine(rules_path=ORIENTATION_RULES_PATH)
    territory_manager = TerritoryManager(territory_rules_path=TERRITORY_PATH)
    clarification_engine = ClarificationEngine()

    # Récit d'une patiente (Mme Antoinette) où nous n'avons pas d'info sur l'APA et le GIR dans le texte.
    text = (
        "Mme Antoinette, 82 ans, vit seule à La Garde. Son fils habite loin et ne peut pas l'aider. "
        "Elle a de grosses difficultés à faire ses courses et à préparer ses repas. "
        "Elle refuse pour l'instant toute aide professionnelle à domicile."
    )

    print(f"\n1. Récit initial : '{text}'")
    
    # Étape A : Première extraction IA
    print("\n--- ÉTAPE A : ANALYSE INITIALE (INFORMATIONS INCOMPLÈTES) ---")
    extracted_data = await extractor.extract(text)
    
    print("\n[ DEBUG : extracted_data ]")
    print(json.dumps(extracted_data, indent=2, ensure_ascii=False))
    
    # Calcul du score initial et des orientations
    comid_results = scoring_engine.calculate_comid_score(extracted_data)
    orientation_results = orientation_engine.evaluate_orientation(extracted_data, comid_results)
    orientation_with_contacts = territory_manager.get_contacts_for_structures(orientation_results, "La Garde")
    
    # Détection des questions de clarification
    questions = clarification_engine.get_clarification_questions(extracted_data, orientation_with_contacts)
    
    print(f"Statut de l'analyse : {'en_attente_clarification' if questions else 'analyse_terminee'}")
    print("\n[ Orientations Suggérées (Base IA) ] :")
    for struct in orientation_with_contacts:
        print(f"  - {struct['label']} (Priorité : {struct['priorite']})")
        
    print("\n[ Questions de Clarification Générées ] :")
    for q in questions:
        print(f"  [?] {q['libelle']} : {q['question']}")
        print(f"      Impact : {q['impact']}")

    # Étape B : L'humain répond à la question (validation/correction humaine)
    print("\n--- ÉTAPE B : APPLICATION DES CORRECTIONS HUMAINES (OVERRIDES) ---")
    print("Saisie du travailleur social : L'APA n'est pas encore en place ('non'), son GIR est estimé à 4, et elle n'a pas d'aidant régulier ('non').")
    
    # On applique les overrides manuels de l'utilisateur
    extracted_data["usager.situation_actuelle.APA"] = "non"
    extracted_data["usager.situation_actuelle.GIR"] = 4
    extracted_data["usager.cadre_de_vie.aidant_regulier"] = "non"
    
    # Recalcul de l'orientation avec les nouvelles données validées
    comid_results_updated = scoring_engine.calculate_comid_score(extracted_data)
    orientation_results_updated = orientation_engine.evaluate_orientation(extracted_data, comid_results_updated)
    orientation_with_contacts_updated = territory_manager.get_contacts_for_structures(orientation_results_updated, "La Garde")
    questions_updated = clarification_engine.get_clarification_questions(extracted_data, orientation_with_contacts_updated)
    
    print(f"\nNouveau Statut de l'analyse : {'en_attente_clarification' if questions_updated else 'analyse_affinee_par_humain'}")
    print("\n[ Orientations Affinées & Validées ] :")
    for struct in orientation_with_contacts_updated:
        print(f"  - {struct['label']} (Priorité : {struct['priorite']})")
        print(f"    Objectif : {struct['objectif']}")
        if struct.get("telephone") or struct.get("adresse"):
            print(f"    Contact : {struct.get('telephone', 'N/A')} | {struct.get('adresse', 'N/A')}")
        else:
            print("    Contact : Non trouvé dans le référentiel territorial")

if __name__ == "__main__":
    asyncio.run(run_test())
