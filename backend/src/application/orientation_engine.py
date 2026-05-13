import json

class OrientationEngine:
    def __init__(self, rules_path: str):
        with open(rules_path, 'r', encoding='utf-8') as f:
            self.rules = json.load(f)

    def evaluate_orientation(self, extracted_data: dict, comid_results: dict):
        """
        Évalue l'éligibilité du patient pour chaque structure définie dans les règles.
        """
        # On prépare un dictionnaire de données complet pour l'évaluation
        # On fusionne les données d'extraction et les résultats de complexité
        eval_context = {**extracted_data}
        eval_context["complexite.niveau"] = comid_results.get("niveau")
        eval_context["complexite.score_total"] = comid_results.get("score_total")

        eligible_structures = []

        for rule in self.rules.get("eligibility_rules", []):
            if not rule.get("enabled", True):
                continue

            is_eligible = self._check_eligibility(rule, eval_context)

            if is_eligible:
                eligible_structures.append({
                    "structure_type": rule["structure_type"],
                    "label": rule["label"],
                    "priorite": rule["result"]["base_priority_score"],
                    "pertinence": rule["result"]["base_pertinence"],
                    "objectif": rule["result"]["objectif_orientation"]
                })

        # On trie par score de priorité (le plus élevé en premier)
        eligible_structures.sort(key=lambda x: x["priorite"], reverse=True)

        return eligible_structures

    def _check_eligibility(self, rule: dict, data: dict):
        # 1. Vérification ALL_OF (toutes les conditions doivent être vraies)
        for condition in rule.get("all_of", []):
            if not self._evaluate_condition(condition, data):
                return False

        # 2. Vérification ANY_OF (au moins une doit être vraie s'il y en a)
        any_of_conditions = rule.get("any_of", [])
        if any_of_conditions:
            found_any = False
            for condition in any_of_conditions:
                if self._evaluate_condition(condition, data):
                    found_any = True
                    break
            if not found_any:
                return False

        # 3. Vérification NONE_OF (aucune ne doit être vraie)
        for condition in rule.get("none_of", []):
            if self._evaluate_condition(condition, data):
                return False

        return True

    def _evaluate_condition(self, condition: dict, data: dict):
        field = condition.get("field")
        operator = condition.get("operator")
        target_value = condition.get("value")
        
        # On récupère la valeur actuelle dans les données
        actual_value = data.get(field)

        if actual_value is None:
            return False

        if operator == "==":
            return actual_value == target_value
        elif operator == ">=":
            try:
                return float(actual_value) >= float(target_value)
            except:
                return False
        elif operator == "in":
            return actual_value in target_value
        elif operator == "contains_any":
            # Si target_value est une liste, on vérifie si l'un d'eux est dans actual_value
            if isinstance(target_value, list):
                if isinstance(actual_value, list):
                    return any(item in actual_value for item in target_value)
                return any(item in str(actual_value) for item in target_value)
            return target_value in str(actual_value)
        
        return False
