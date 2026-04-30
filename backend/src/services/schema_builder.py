from datetime import datetime
import copy


def build_schema(template, text, signals, score, risk_level, entities=None):
    data = copy.deepcopy(template)

    # ---------------- NETTOYAGE DES DONNEES EN DUR ----------------
    # On supprime les informations hardcodées du schéma pivot pour qu'elles 
    # ne soient plus prises en compte si non détectées dans le texte.
    data["usager"] = {
        "identite": {
            "age_estime": entities.get("age") if entities and "age" in entities else None
        },
        "localisation": {},
        "cadre_de_vie": {},
        "situation_actuelle": {}
    }
    data["adresseur"] = {}
    data["vulnerabilites"] = {}
    data["cercle_de_soins"] = {}
    
    if "demande" in data:
        data["demande"]["motifs_secondaires"] = []
        data["demande"]["evenement_declencheur"] = "non_renseigne"
        data["demande"]["description_factuelle"] = {}
        data["demande"]["actions_deja_menees"] = []
        data["demande"]["attentes_formulees"] = {}

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

    # Ajustement des niveaux selon le modèle (à titre d'exemple)
    if score >= 5:
        niveau = "complexe"
    elif score >= 3:
        niveau = "a_risque_de_complexite"
    else:
        niveau = "non_complexe"
        
    data["complexite"]["niveau"] = niveau

    # ---------------- MAPPING DES SIGNAUX VERS LES DONNÉES STRUCTURÉES ----------------
    if "vulnerabilites" not in data:
        data["vulnerabilites"] = {}
    if "social" not in data["vulnerabilites"]:
        data["vulnerabilites"]["social"] = {}
    if "sante" not in data["vulnerabilites"]:
        data["vulnerabilites"]["sante"] = {}
        data["vulnerabilites"]["sante"]["hospitalisation"] = {}
    if "demande" not in data:
        data["demande"] = {}
    if "description_factuelle" not in data["demande"]:
        data["demande"]["description_factuelle"] = {}
    if "cadre_de_vie" not in data["usager"]:
        data["usager"]["cadre_de_vie"] = {}
    if "situation_actuelle" not in data["usager"]:
        data["usager"]["situation_actuelle"] = {}
    if "identite" not in data["usager"]:
        data["usager"]["identite"] = {}

    # Mappings existants
    if signals.get("isolement"):
        data["vulnerabilites"]["social"]["isolement_relationnel"] = "important"
    if signals.get("retour_hospit"):
        data["vulnerabilites"]["sante"]["hospitalisation"]["statut"] = "recente"
    if signals.get("chute"):
        data["demande"]["description_factuelle"]["autonomie_observee"] = "diminuee"

    # Nouveaux mappings mock
    if signals.get("epuisement_aidant"):
        data["vulnerabilites"]["social"]["risque_epuisement_entourage"] = "probable"
        
    if signals.get("urgence_medicale"):
        data["adresseur"]["degre_urgence_percu"] = "critique"
        
    if signals.get("violence_danger"):
        data["usager"]["situation_actuelle"]["suspiion_malveillance"] = "violence physique"
        data["adresseur"]["degre_urgence_percu"] = "eleve"
        
    if signals.get("logement_insalubre"):
        data["usager"]["cadre_de_vie"]["etat_logement"] = "insalubre"
        
    if signals.get("troubles_cognitifs"):
        data["vulnerabilites"]["sante"]["problematique_de_sante"] = "neuro"
        
    if signals.get("presence_mandataire"):
        data["usager"]["identite"]["mesure_protection"] = "tutelle"
        
    if signals.get("refus_aide"):
        data["demande"]["description_factuelle"]["refus_aide"] = True

    # ---------------- ORIENTATION DYNAMIQUE ----------------
    from backend.src.services.rules_loader import load_orientation
    from backend.src.services.orientation_engine import compute_orientation

    try:
        rules = load_orientation()
        orientation_result = compute_orientation(data, rules)
        
        winner_key = orientation_result.get("orientation_principale")
        if winner_key == "AMBIGU":
            tied_candidates = [k for k, v in orientation_result["orientations_candidates"].items() if v["score"] == max(c["score"] for c in orientation_result["orientations_candidates"].values())]
            proposition = {
                "type_structure": "AMBIGU",
                "nom_structure": "Égalité détectée - Choix humain requis",
                "niveau_pertinence": "eleve",
                "objectif_orientation": "departager_candidats"
            }
            justification = f"Le moteur n'a pas pu trancher. Plusieurs structures ont le même score maximum : {', '.join(tied_candidates)}."
            complements = []
        elif winner_key:
            winner_data = orientation_result["orientations_candidates"][winner_key]
            proposition = winner_data["result"]
            
            # Assure la présence d'un nom de structure si manquant dans les règles
            if "nom_structure" not in proposition:
                proposition["nom_structure"] = f"{winner_key} (Orientation dynamique)"
                
            justification = f"Orientation par moteur de règles vers {winner_key} (Score: {winner_data['score']})."
            complements = orientation_result.get("orientations_complementaires", [])
        else:
            proposition = {
                "type_structure": "NON_DEFINIE",
                "nom_structure": "Orientation manuelle requise",
                "niveau_pertinence": "faible",
                "objectif_orientation": "evaluation_humaine"
            }
            justification = "Aucune structure ne correspond aux critères de la situation."
            complements = []
            
    except Exception as e:
        print(f"Erreur lors de l'orientation dynamique: {e}")
        # Fallback statique minimal en cas d'erreur
        proposition = {
            "type_structure": "ERREUR",
            "nom_structure": "Erreur Moteur",
            "niveau_pertinence": "faible",
            "objectif_orientation": "erreur"
        }
        justification = f"Erreur d'exécution du moteur: {str(e)}"
        complements = []

    data["orientation"] = {
        "proposition_principale": proposition,
        "propositions_complementaires": complements,
        "justification_detaillee": justification,
        "niveau_confiance_orientation": 0.85
    }

    return data