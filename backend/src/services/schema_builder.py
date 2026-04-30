from datetime import datetime
import copy


def build_schema(template, text, signals, score, risk_level):
    data = copy.deepcopy(template)

    # ---------------- META ----------------
    data["meta"]["id_dossier"] = "ORIA-TEST-001"
    data["meta"]["date_creation"] = datetime.utcnow().isoformat()
    data["meta"]["statut_dossier"] = "analyse_terminee_en_attente_de_relecture"
    data["meta"]["niveau_confiance_global"] = 0.8

    # ---------------- DEMANDE ----------------
    data["demande"]["resume_structure"] = text
    data["demande"]["motif_principal"] = "analyse_automatique"

    # ---------------- SIGNAUX ----------------
    data["signaux_detectes"] = []

    for key, value in signals.items():
        if value:
            data["signaux_detectes"].append({
                "categorie": key,
                "intensite": "detecte",
                "indice_textuel": key,
                "niveau_confiance": 0.9
            })

    # ---------------- COMPLEXITE ----------------
    data["complexite"]["score_total"] = score

    if score >= 5:
        data["complexite"]["niveau"] = "complexe"
    elif score >= 3:
        data["complexite"]["niveau"] = "a_risque_de_complexite"
    else:
        data["complexite"]["niveau"] = "non_complexe"

    return data