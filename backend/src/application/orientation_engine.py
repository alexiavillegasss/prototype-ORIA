import json

class OrientationEngine:
    def __init__(self, rules_path: str):
        with open(rules_path, 'r', encoding='utf-8') as f:
            self.rules = json.load(f)

    def evaluate_orientation(self, extracted_data: dict, comid_results: dict):
        """
        Évalue l'éligibilité du patient pour chaque structure définie dans les règles.
        """
        if comid_results is None:
            comid_results = {}

        # On prépare un dictionnaire de données complet pour l'évaluation
        eval_context = {**extracted_data}
        eval_context["complexite.niveau"] = comid_results.get("niveau")
        eval_context["complexite.score_total"] = comid_results.get("score_total")

        eligible_structures = []

        for rule in self.rules.get("eligibility_rules", []):
            if not rule.get("enabled", True):
                continue

            is_eligible, matched_conditions = self._check_eligibility(rule, eval_context)

            if is_eligible:
                eligible_structures.append({
                    "structure_type": rule["structure_type"],
                    "label": rule.get("label", rule["structure_type"]),
                    "priorite": rule.get("result", {}).get("base_priority_score", 0),
                    "pertinence": rule.get("result", {}).get("base_pertinence", "moyenne"),
                    "objectif": rule.get("result", {}).get("objectif_orientation", "N/A"),
                    "pourquoi": matched_conditions
                })

        # Dédoublonner et regrouper par structure_type pour éviter les doublons à l'affichage
        grouped_structures = {}
        for struct in eligible_structures:
            stype = struct["structure_type"]
            if stype not in grouped_structures:
                grouped_structures[stype] = {
                    "structure_type": stype,
                    "winning_label": struct["label"],
                    "priorite": struct["priorite"],
                    "pertinence": struct["pertinence"],
                    "matches": [(struct["label"], struct["objectif"])],
                    "pourquoi": list(struct.get("pourquoi", []))
                }
            else:
                # On garde la priorité maximale
                if struct["priorite"] > grouped_structures[stype]["priorite"]:
                    grouped_structures[stype]["priorite"] = struct["priorite"]
                    grouped_structures[stype]["winning_label"] = struct["label"]
                # On combine les pertinences
                if struct["pertinence"] == "eleve":
                    grouped_structures[stype]["pertinence"] = "eleve"
                # On évite d'ajouter des doublons exacts d'explications
                match_entry = (struct["label"], struct["objectif"])
                if match_entry not in grouped_structures[stype]["matches"]:
                    grouped_structures[stype]["matches"].append(match_entry)
                # On ajoute les conditions de pourquoi s'ils n'y sont pas déjà
                for cond in struct.get("pourquoi", []):
                    if cond not in grouped_structures[stype]["pourquoi"]:
                        grouped_structures[stype]["pourquoi"].append(cond)

        # On reconstruit la liste finale avec les explications combinées
        final_structures = []
        for stype, data in grouped_structures.items():
            if len(data["matches"]) == 1:
                final_structures.append({
                    "structure_type": stype,
                    "label": data["winning_label"],
                    "priorite": data["priorite"],
                    "pertinence": data["pertinence"],
                    "objectif": data["matches"][0][1],
                    "pourquoi": data["pourquoi"]
                })
            else:
                # On définit un label propre de niveau structure pour le regroupement
                base_label = data["winning_label"]
                if " - " in base_label:
                    parts = base_label.split(" - ")
                    prefix = parts[0].strip()
                    if prefix == "DAC":
                        base_label = "DAC - Dispositif d'Appui à la Coordination"
                    elif prefix == "CRT":
                        base_label = "CRT - Centre de Ressources Territorial (Accompagnement Renforcé)"
                    elif prefix == "CLIC":
                        base_label = "CLIC - Centre Local d'Information et de Coordination"
                
                # Regroupement des explications sous forme de liste à puces propre
                combined_objectifs = "Motifs d'orientation combinés :"
                for label, obj in data["matches"]:
                    clean_label = label
                    if " - " in clean_label:
                        clean_label = clean_label.split(" - ", 1)[1].strip()
                    combined_objectifs += f"\n  - [{clean_label}] : {obj}"

                final_structures.append({
                    "structure_type": stype,
                    "label": base_label,
                    "priorite": data["priorite"],
                    "pertinence": data["pertinence"],
                    "objectif": combined_objectifs,
                    "pourquoi": data["pourquoi"]
                })

        # On trie par score de priorité (le plus élevé en premier)
        final_structures.sort(key=lambda x: x["priorite"], reverse=True)

        # Si les règles globales imposent une seule structure ou si on veut la meilleure
        allow_multiple = self.rules.get("global_rules", {}).get("allow_multiple_eligible_structures", True)
        if not allow_multiple and final_structures:
            return [final_structures[0]]

        return final_structures

    def _check_eligibility(self, rule: dict, data: dict):
        matched_conditions = []  # Preuves des conditions qui ont matché

        # 1. Vérification ALL_OF (toutes les conditions doivent être vraies)
        for condition in rule.get("all_of", []):
            if not self._evaluate_condition(condition, data):
                return False, []
            # On enregistre la preuve
            field = condition.get("field")
            matched_conditions.append({
                "champ": field,
                "valeur": data.get(field),
                "operateur": condition.get("operator"),
                "attendu": condition.get("value")
            })

        # 2. Vérification ANY_OF (au moins une doit être vraie s'il y en a)
        any_of_conditions = rule.get("any_of", [])
        if any_of_conditions:
            found_any = False
            for condition in any_of_conditions:
                if self._evaluate_condition(condition, data):
                    found_any = True
                    # On enregistre la condition gagnante
                    field = condition.get("field")
                    matched_conditions.append({
                        "champ": field,
                        "valeur": data.get(field),
                        "operateur": condition.get("operator"),
                        "attendu": condition.get("value")
                    })
                    break
            if not found_any:
                return False, []

        # 3. Vérification NONE_OF (aucune ne doit être vraie)
        for condition in rule.get("none_of", []):
            if self._evaluate_condition(condition, data):
                return False, []

        return True, matched_conditions

    def _evaluate_condition(self, condition: dict, data: dict):
        field = condition.get("field")
        operator = condition.get("operator")
        target_value = condition.get("value")
        
        # On récupère la valeur actuelle dans les données
        actual_value = data.get(field)

        if actual_value is None or target_value is None:
            return False

        if operator == "==":
            return str(actual_value) == str(target_value)
        elif operator == ">=":
            try:
                return float(actual_value) >= float(target_value)
            except:
                return False
        elif operator == "in":
            if isinstance(target_value, list):
                # On compare en string pour éviter les problèmes int/str
                return str(actual_value) in [str(v) for v in target_value]
            return str(actual_value) in str(target_value)
        elif operator == "not_in":
            if isinstance(target_value, list):
                return str(actual_value) not in [str(v) for v in target_value]
            return str(actual_value) not in str(target_value)
        elif operator == "contains_any":
            if isinstance(target_value, list):
                if isinstance(actual_value, list):
                    return any(str(item) in [str(v) for v in actual_value] for item in target_value)
                return any(str(item) in str(actual_value) for item in target_value)
            return str(target_value) in str(actual_value)
        
        return False
