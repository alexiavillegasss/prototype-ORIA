import os
import sys
import json

# Add path to import modules
sys.path.append(os.path.join(os.getcwd(), 'backend', 'src'))

from application.orientation_engine import OrientationEngine
from application.scoring_engine import ScoringEngine

def run_tests():
    BASE_DIR = os.getcwd()
    COMID_PATH = os.path.join(BASE_DIR, 'config', 'rules', 'COMID.json')
    ORIENTATION_RULES_PATH = os.path.join(BASE_DIR, 'config', 'rules', 'orientation_rules.json')

    print("--- Initialisation du Moteur d'Orientation par Points ---")
    orientation_engine = OrientationEngine(rules_path=ORIENTATION_RULES_PATH)
    scoring_engine = ScoringEngine(comid_rules_path=COMID_PATH)

    # Helper function to run a mock test case
    def test_case(name, extracted, text):
        print(f"\n=========================================")
        print(f"TEST CASE: {name}")
        print(f"=========================================")
        comid = scoring_engine.calculate_comid_score(extracted)
        results = orientation_engine.evaluate_orientation(extracted, comid, original_text=text)
        
        # Display results
        for r in results[:3]:
            print(f"-> Winner: {r['structure_type']} ({r['label']}) | Score: {r['priorite']} | Pertinence: {r['pertinence']}")
            print(f"   Objectif: {r['objectif'][:100]}...")
            
        print("\nExplainability:")
        print(f"  Scores: { {k: v for k, v in extracted.get('evaluation.moteur_points.scores', {}).items() if v > 0} }")
        print(f"  Besoins détectés ({len(extracted.get('evaluation.moteur_points.besoins_identifies', []))}):")
        for b in extracted.get('evaluation.moteur_points.besoins_identifies', []):
            print(f"    - {b['detaille']} -> {b['structures_cochees']}")
        print(f"  Exclusions: {extracted.get('evaluation.moteur_points.exclusions_declenchees')}")
        return results

    # CASE 1: UTS and CCAS tie with social need (dettes).
    # Since we assume no ASS in any CCAS, UTS must win.
    extracted_1 = {
        "usager.identite.age_estime": 70,
        "usager.localisation.commune_residence": "La Seyne-sur-Mer",
        "demande.motif_principal": "dettes"
    }
    # Dettes is a social need, should trigger UTS and CCAS.
    test_case("UTS vs CCAS - Besoin social (dettes) - Pas d'ASS au CCAS", extracted_1, "Il a des dettes et a besoin d'aide pour s'en sortir.")

    # CASE 2: UTS and CCAS tie without social need (information).
    # Expected: CCAS wins.
    extracted_2 = {
        "usager.identite.age_estime": 70,
        "usager.localisation.commune_residence": "La Seyne-sur-Mer",
        "demande.motif_principal": "information_aides"
    }
    test_case("UTS vs CCAS - Information uniquement", extracted_2, "Il veut des informations générales sur les aides.")

    # CASE 3: UTS winner but cannot move.
    # Expected: DAC wins.
    extracted_3 = {
        "usager.identite.age_estime": 70,
        "usager.localisation.commune_residence": "La Seyne-sur-Mer",
        "demande.motif_principal": "dettes"
    }
    test_case("UTS mais déplacement impossible", extracted_3, "Il a des dettes mais ne peut pas se déplacer de chez lui, il est alité.")

    # CASE 4: More than 5 needs.
    # Expected: DAC wins.
    # We trigger several COMID needs.
    extracted_4 = {
        "usager.identite.age_estime": 75,
        "usager.localisation.commune_residence": "La Seyne-sur-Mer",
        "demande.motif_principal": "maintien_a_domicile",
        "evaluation.comid.troubles_cognitifs": True,
        "evaluation.comid.epuisement_aidant": True,
        "evaluation.comid.precarite_financiere": True,
        "evaluation.comid.polymedication": True,
        "evaluation.comid.douleurs": True,
        "evaluation.comid.isolement_social": True
    }
    test_case("Plus de 5 besoins", extracted_4, "Marie a 75 ans, elle a de graves troubles cognitifs et prend beaucoup de médicaments. Son aidant est épuisé. Elle souffre de douleurs chroniques et est isolée financièrement et socialement.")

    # CASE 5: Refused by establishment in a commune with CLIC (La Seyne-sur-Mer has CLIC)
    # Expected: CLIC.
    extracted_5 = {
        "usager.identite.age_estime": 75,
        "usager.localisation.commune_residence": "La Seyne-sur-Mer",
        "demande.motif_principal": "maintien_a_domicile"
    }
    test_case("Refusé par l'établissement (avec CLIC local)", extracted_5, "Le patient a été refusé par l'ehpad local.")

    # CASE 6: The user's exact query
    # "Bonjour, je suis IDE. J'ai une tournée sur La Seyne-sur-Mer et j'ai un patient de 75 ans qui se dégrade beaucoup il aurait besoin d'aides à domicile. Merci pour votre aide."
    # Expected: CLIC.
    extracted_6 = {
        "usager.identite.age_estime": 75,
        "usager.localisation.commune_residence": "La Seyne-sur-Mer",
        "demande.motif_principal": "maintien_a_domicile",
        "vulnerabilites.sante.professionnels_domicile": "oui",
        "evaluation.comid.degradation_recente": True
    }
    test_case("Cas Utilisateur - IDE avec patient de 75 ans qui se dégrade et a besoin d'aides à domicile", extracted_6, "Bonjour, je suis IDE. J'ai une tournée sur La Seyne-sur-Mer et j'ai un patient de 75 ans qui se dégrade beaucoup il aurait besoin d'aides à domicile. Merci pour votre aide.")

if __name__ == "__main__":
    run_tests()
