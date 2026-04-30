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
    winner = select_winner(candidates, priorities)

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
def select_winner(candidates, priorities):
    if not candidates:
        return None

    # default max score
    best = max(candidates.items(), key=lambda x: x[1]["score"])
    winner = best[0]

    # apply priority overrides
    for rule in priorities:
        if evaluate_any_field(rule.get("if_any", [])):
            return rule["winner"]

    return winner


# -----------------------------
# CONDITION ENGINE SIMPLE
# -----------------------------
def evaluate_all(data, conditions):
    return all(evaluate_condition(data, c) for c in conditions)


def evaluate_any(data, conditions):
    return any(evaluate_condition(data, c) for c in conditions)


def evaluate_any_field(conditions):
    # version simplifiée (priorité globale)
    return True if conditions else False


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