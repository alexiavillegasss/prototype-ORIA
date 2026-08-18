import sys
import os
import asyncio
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "backend", "src")))
from application.orientation_engine import OrientationEngine

sys.stdout.reconfigure(encoding='utf-8')

# Mock extracted data for the doctor case:
# Description: "Bonjour, je suis médecin et j'aurai besoin qu'un point global soit fait au domicile d'une patiente de 80 ans en GIR 4 parce que la situation se dégrade. Elle a déjà des aides au domicile mais je me demande si c'est suffisant. Madame et sa famille souhaiteraient retarder l'entrée en EHPAD mais je pense qu'il faudrait faire un accompagnement plus global des équipes qui sont déjà en place."
extracted_data = {
    "usager.identite.age_estime": 80,
    "usager.localisation.commune_residence": "La Seyne-sur-Mer",
    "usager.situation_actuelle.APA": "non",  # She does not have APA yet
    "usager.situation_actuelle.PCH": "non",
    "usager.situation_actuelle.GIR": "GIR 4",
    "vulnerabilites.sante.suivi_medical.medecin_traitant": "identifie",
    "usager.situation_actuelle.suspicion_malveillance": "aucune",
    "adresseur.degre_urgence_percu": "faible",
    "vulnerabilites.sante.hospitalisation.statut": "aucun",
    "demande.motif_principal": "evaluation_globale",
    "vulnerabilites.sante.professionnels_domicile": "oui",
    "usager.cadre_de_vie.aidant_regulier": "oui",
    "usager.cadre_de_vie.etat_logement": "non_renseigne",
    "evaluation.confiance.variables": {
        "age": 100,
        "ville": 100,
        "apa": 70,
        "pch": 40,
        "gir": 100,
        "medecin_traitant": 90,
        "malveillance": 100,
        "urgence": 90,
        "hospitalisation": 100,
        "motif": 100,
        "professionnels_domicile": 100,
        "aidant_regulier": 80,
        "etat_logement": 0
    },
    "evaluation.comid.precarite_financiere": False,
    "evaluation.comid.degradation_recente": False,
    "evaluation.comid.troubles_cognitifs": False,
    "evaluation.comid.perte_autonomie_recente": False,
    "evaluation.confiance.comid": {}
}

text = "Bonjour, je suis médecin et j'aurai besoin qu'un point global soit fait au domicile d'une patiente de 80 ans en GIR 4 parce que la situation se dégrade. Elle a déjà des aides au domicile mais je me demande si c'est suffisant. Madame et sa famille souhaiteraient retarder l'entrée en EHPAD mais je pense qu'il faudrait faire un accompagnement plus global des équipes qui sont déjà en place."

async def run():
    rules_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "config", "rules", "orientation_rules.json"))
    engine = OrientationEngine(rules_path)
    comid_results = {"niveau": "simple", "score_total": 0}
    results = engine.evaluate_orientation(extracted_data, comid_results, text)
    print("=== RESULTS ===")
    for r in results:
        print(f"Winner: {r['structure_type']} | Label: {r['label']} | Score: {r['priorite']}")
        print(f"  Objectif: {r['objectif']}")
    
    print("\n=== EXPLICABILITY ===")
    print("Scores:", extracted_data.get("evaluation.moteur_points.scores"))
    print("Besoins détectés:")
    for n in extracted_data.get("evaluation.moteur_points.besoins_identifies", []):
        print(f"  - {n['detaille']} -> {n['structures_cochees']}")

asyncio.run(run())
