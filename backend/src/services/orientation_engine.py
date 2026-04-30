import json


# -----------------------------
# LOAD RULES
# -----------------------------
def load_orientation_rules(path="config/scoring/orientation_rules.json"):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


# -----------------------------
# ENGINE PRINCIPAL
# -----------------------------
def compute_orientation(data: dict, rules: dict):
    """
    Calcule l’orientation principale + complémentaires
    """

    structures = rules["structures"]
    priorities = rules.get("regles_priorite", [])
    complements = rules.get("regles_orientations_complementaires", [])

    candidates = {}

    # -------------------------
    # 1. SCORE CHAQUE STRUCTURE
    # -------------------------
    for name, config in structures.items():

        score = 0

        # ALL conditions
        if not evaluate_all(data, config.get("conditions_entree_all", [])):
            continue

        # ANY conditions
        if not evaluate_any(data, config.get("conditions_entree_any", [])):
            continue

        # EXCLUSIONS
        if evaluate_any(data, config.get("conditions_exclusion", [])):
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
    # 3. COMPLEMENTS
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
        "orientations_complementaires": complements_list
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