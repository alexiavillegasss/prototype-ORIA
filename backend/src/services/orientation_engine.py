import json


# -----------------------------
# LOAD RULES
# -----------------------------
def load_orientation_rules(path="config/scoring/orientation_rules.json"):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


FIELD_LABELS = {
    "usager.identite.age_estime": "l'âge de la personne",
    "usager.localisation.commune_residence": "la commune de résidence",
    "usager.localisation.adresse_precise": "l'adresse précise",
    "usager.situation_actuelle.GIR": "le niveau GIR (autonomie)",
    "demande.description_factuelle.autonomie_observee": "l'autonomie observée",
    "vulnerabilites.social.isolement_relationnel": "le degré d'isolement social",
    "usager.cadre_de_vie.etat_logement": "l'état du logement",
    "vulnerabilites.sante.suivi_medical.medecin_traitant": "le médecin traitant",
    "vulnerabilites.administratif.ouverture_des_droits": "l'ouverture des droits",
    "usager.cadre_de_vie.adequation_logement_situation": "l'adéquation du logement",
    "vulnerabilites.social.risque_epuisement_entourage": "le risque d'épuisement de l'aidant",
    "usager.identite.mesure_protection": "la présence d'une mesure de protection",
    "vulnerabilites.sante.suivi_medical.continuité_soins": "la continuité des soins",
    "vulnerabilites.administratif.probleme_financier": "l'existence de problèmes financiers"
}


# -----------------------------
# ENGINE PRINCIPAL
# -----------------------------
def compute_orientation(data: dict, rules: dict):
    """
    Calcule l’orientation principale + complémentaires + questions d'affinage
    """

    structures = rules["structures"]
    priorities = rules.get("regles_priorite", [])
    complements = rules.get("regles_orientations_complementaires", [])

    candidates = {}
    missing_fields_by_structure = {}

    # -------------------------
    # 1. SCORE CHAQUE STRUCTURE
    # -------------------------
    for name, config in structures.items():

        score = 0
        missing_for_this = []

        # ALL conditions
        all_ok, missing_all = evaluate_all_with_missing(data, config.get("conditions_entree_all", []))
        if not all_ok:
            if missing_all:
                missing_fields_by_structure[name] = missing_all
            print(f"  [DEBUG] {name} rejeté par ALL")
            continue

        # ANY conditions
        any_ok, missing_any = evaluate_any_with_missing(data, config.get("conditions_entree_any", []))
        if not any_ok:
            if missing_any:
                missing_fields_by_structure[name] = missing_any
            print(f"  [DEBUG] {name} rejeté par ANY")
            continue

        # EXCLUSIONS
        if evaluate_any(data, config.get("conditions_exclusion", [])):
            print(f"  [DEBUG] {name} rejeté par EXCLUSION")
            continue

        # RENFORT
        if "conditions_renfort" in config:
            score += count_matches(data, config["conditions_renfort"])

        # base score implicite
        score += 1

        candidates[name] = {
            "score": score,
            "result": config["resultat"]
        }

    # -------------------------
    # 2. PRIORITÉS MÉTIER
    # -------------------------
    winner = select_winner(candidates, priorities, data)

    # -------------------------
    # 3. QUESTIONS D'AFFINAGE CONTEXTUELLES
    # -------------------------
    questions = []
    
    # Cas 1: Ambiguité
    if winner == "AMBIGU":
        max_score = max(c["score"] for c in candidates.values())
        tied = [k for k, v in candidates.items() if v["score"] == max_score]
        questions.append(f"La situation est ambigüe entre {', '.join(tied)}. Pourriez-vous préciser les vulnérabilités dominantes ?")

    # Cas 2: Structures proches (manque juste un champ null)
    # On regarde les structures qui n'ont pas été candidates mais qui n'avaient que des champs null en bloquant
    missing_fields_counts = {}
    for name, fields in missing_fields_by_structure.items():
        if name not in candidates:
            for f in fields:
                missing_fields_counts[f] = missing_fields_counts.get(f, 0) + 1
    
    # Priorité aux champs critiques
    priority_fields = ["usager.identite.age_estime", "usager.localisation.commune_residence"]
    sorted_missing = sorted(missing_fields_counts.keys(), 
                           key=lambda x: (x not in priority_fields, -missing_fields_counts[x]))
    
    for f in sorted_missing:
        label = FIELD_LABELS.get(f, f)
        if f == "usager.identite.age_estime":
            questions.append("Quel est l'âge de la personne ? Cette information est cruciale pour déterminer les aides disponibles.")
        elif f == "usager.localisation.commune_residence":
            questions.append("Dans quelle commune réside la personne ? L'orientation dépend des structures territoriales.")
        else:
            questions.append(f"Pouvez-vous préciser {label} ? Cela permettrait d'affiner l'éligibilité à certaines structures.")

    # Nettoyage doublons
    questions = list(dict.fromkeys(questions))[:3] # Limite à 3 questions

    # -------------------------
    # 4. COMPLEMENTS
    # -------------------------
    complements_list = []

    for rule in complements:
        if evaluate_all(data, rule.get("if_all", [])):
            complements_list.append(rule["append_complement"])

    # -------------------------
    # OUTPUT FINAL
    # -------------------------
    return {
        "orientation_principale": winner,
        "orientations_candidates": candidates,
        "orientations_complementaires": complements_list,
        "questions_affinage": questions
    }


# -----------------------------
# PRIORITY RESOLUTION
# -----------------------------
def select_winner(candidates, priorities, data):
    if not candidates:
        return None

    # apply priority overrides en premier
    for rule in priorities:
        if evaluate_any(data, rule.get("if_any", [])):
            # Si le gagnant prioritaire est un candidat valide
            if rule["winner"] in candidates:
                return rule["winner"]
        if evaluate_all(data, rule.get("if_all", [])):
            if rule["winner"] in candidates:
                return rule["winner"]

    # max score
    max_score = max(c["score"] for c in candidates.values())
    tied_candidates = [k for k, v in candidates.items() if v["score"] == max_score]

    if len(tied_candidates) > 1:
        return "AMBIGU"

    return tied_candidates[0]


# -----------------------------
# CONDITION ENGINE SIMPLE
# -----------------------------
def evaluate_all(data, conditions):
    return all(evaluate_condition(data, c) for c in conditions)


def evaluate_any(data, conditions):
    return any(evaluate_condition(data, c) for c in conditions)


def evaluate_all_with_missing(data, conditions):
    missing = []
    results = []
    for c in conditions:
        res = evaluate_condition(data, c)
        results.append(res)
        if not res:
            val = get_value(data, c["field"])
            if val is None:
                missing.append(c["field"])
    
    return all(results), missing


def evaluate_any_with_missing(data, conditions):
    if not conditions:
        return True, []
        
    missing = []
    results = []
    for c in conditions:
        res = evaluate_condition(data, c)
        results.append(res)
        if not res:
            val = get_value(data, c["field"])
            if val is None:
                missing.append(c["field"])
    
    return any(results), missing


def evaluate_any_field(conditions):
    # Plus utilisé, on utilise evaluate_any ou evaluate_all directement
    pass


def evaluate_condition(data, condition):
    try:
        field = condition["field"]
        operator = condition["operator"]
        value = condition["value"]

        actual = get_value(data, field)

        if operator == "equals":
            return actual == value

        if operator == "in":
            return actual in value

        if operator == "contains":
            return value in str(actual)

        if operator == "gte":
            return actual >= value

        if operator == "lt":
            return actual < value

        if operator == "between":
            return value[0] <= actual <= value[1]

        if operator == "not_empty":
            return actual is not None and actual != ""

    except:
        return False

    return False


# -----------------------------
# SAFE FIELD ACCESS
# -----------------------------
def get_value(data, path):
    keys = path.split(".")
    value = data

    for k in keys:
        if isinstance(value, dict):
            value = value.get(k)
        else:
            return None

    return value


# -----------------------------
# COUNT MATCHES
# -----------------------------
def count_matches(data, conditions):
    return sum(1 for c in conditions if evaluate_condition(data, c))