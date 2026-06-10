import asyncio
import os
import sys
import json

sys.path.append(os.path.join(os.getcwd(), 'backend', 'src'))

from ai.extraction.extractor import SignalExtractor
from application.scoring_engine import ScoringEngine
from application.orientation_engine import OrientationEngine
from application.territory_manager import TerritoryManager

async def test_low_info():
    BASE_DIR = os.getcwd()
    SCHEMA_PATH = os.path.join(BASE_DIR, 'config', 'schemas', 'schema_definition.json')
    COMID_PATH = os.path.join(BASE_DIR, 'config', 'rules', 'COMID.json')
    ORIENTATION_RULES_PATH = os.path.join(BASE_DIR, 'config', 'rules', 'orientation_rules.json')
    TERRITORY_PATH = os.path.join(BASE_DIR, 'config', 'referentials', 'referentiel_territoire.json')

    extractor = SignalExtractor(schema_path=SCHEMA_PATH, comid_path=COMID_PATH)
    scoring_engine = ScoringEngine(comid_rules_path=COMID_PATH)
    orientation_engine = OrientationEngine(rules_path=ORIENTATION_RULES_PATH)
    territory_manager = TerritoryManager(territory_rules_path=TERRITORY_PATH)

    # Programmatic mock test case
    print("--- TEST PROGRAMMATIQUE MOCK (CONFIANCE < 40%) ---")
    mock_extracted_data = {
        "usager.identite.age_estime": 85,
        "usager.localisation.commune_residence": "Sanary",
        "usager.situation_actuelle.APA": "inconnu", # trigger missing penalty
        "usager.situation_actuelle.PCH": "inconnu",
        "usager.situation_actuelle.GIR": None,
        "vulnerabilites.sante.suivi_medical.medecin_traitant": "incertain",
        "usager.situation_actuelle.suspicion_malveillance": "aucune",
        "adresseur.degre_urgence_percu": "faible",
        "vulnerabilites.sante.hospitalisation.statut": "aucun",
        "demande.motif_principal": "maintien_a_domicile",  # UTS rule matches on this
        "vulnerabilites.sante.professionnels_domicile": "non",
        "usager.cadre_de_vie.aidant_regulier": "non",
        "usager.cadre_de_vie.etat_logement": "propre",
        "evaluation.confiance.variables": {
            "age": 20, # Low confidence
            "ville": 100,
            "apa": 0,
            "pch": 0,
            "gir": 0,
            "professionnels_domicile": 0,
            "aidant_regulier": 0,
            "medecin_traitant": 0,
            "malveillance": 0,
            "urgence": 0,
            "hospitalisation": 0,
            "motif": 10, # Very low confidence
            "etat_logement": 0
        },
        "evaluation.comid.precarite_financiere": False,
        "evaluation.confiance.comid": {}
    }
    
    mock_comid_results = {
        "score_total": 1,
        "niveau": "Situation non complexe",
        "label": "Situation non complexe",
        "items_detectes": []
    }

    # UTS check uses:
    # any_of: precarite_financiere, precarite, motif in ["rsa", "violence_conjugale", "gestion_budget", "parentalite", "logement"]
    # Wait, "maintien_a_domicile" is not in UTS list, but CCAS check uses:
    # any_of: motif in ["information", "information_locale", "aide_financiere", "rsa", "aide_administrative", "foyer_logement", "residence_autonomie"]
    # CLIC check uses:
    # any_of: epuisement_aidant, motif in ["maintien_a_domicile", ...]
    # So CLIC will be matched! Let's see what CLIC fields are:
    # any_of: epuisement_aidant, motif in [...]
    # none_of: age <= 60, APA == "oui", motif in ["recherche_medecin", "acces_aux_soins"]
    # So fields involved in CLIC are: epuisement_aidant, motif, age, APA.
    # Let's see how confidence is calculated.
    
    orientation_results = orientation_engine.evaluate_orientation(mock_extracted_data, mock_comid_results)
    results_with_contacts = territory_manager.get_contacts_for_structures(orientation_results, "Sanary")

    print("\n--- RESULTATS MOCK ---")
    for struct in results_with_contacts:
        print(f"[{struct['label']}] (Confiance : {struct.get('score_confiance')}% | Priorité : {struct.get('priorite')})")
        print(f"  Objectif : {struct['objectif']}")
        print(f"  Explication : {struct['explication_confiance']}")

if __name__ == "__main__":
    asyncio.run(test_low_info())
