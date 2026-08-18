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

            is_eligible = self._check_eligibility(rule, eval_context)

            if is_eligible:
                score_confiance, explication_confiance = self._calculate_rule_confidence(rule, extracted_data, comid_results)
                eligible_structures.append({
                    "structure_type": rule["structure_type"],
                    "label": rule.get("label", rule["structure_type"]),
                    "priorite": rule.get("result", {}).get("base_priority_score", 0),
                    "pertinence": rule.get("result", {}).get("base_pertinence", "moyenne"),
                    "objectif": rule.get("result", {}).get("objectif_orientation", "N/A"),
                    "score_confiance": score_confiance,
                    "explication_confiance": explication_confiance
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
                    "score_confiance": struct["score_confiance"],
                    "explication_confiance": struct["explication_confiance"],
                    "matches": [(struct["label"], struct["objectif"], struct["score_confiance"], struct["explication_confiance"])]
                }
            else:
                # On garde la priorité maximale
                if struct["priorite"] > grouped_structures[stype]["priorite"]:
                    grouped_structures[stype]["priorite"] = struct["priorite"]
                    grouped_structures[stype]["winning_label"] = struct["label"]
                # On combine les pertinences
                if struct["pertinence"] == "eleve":
                    grouped_structures[stype]["pertinence"] = "eleve"
                # On garde la confiance maximale
                if struct["score_confiance"] > grouped_structures[stype]["score_confiance"]:
                    grouped_structures[stype]["score_confiance"] = struct["score_confiance"]
                    grouped_structures[stype]["explication_confiance"] = struct["explication_confiance"]
                # On évite d'ajouter des doublons exacts d'explications
                match_entry = (struct["label"], struct["objectif"], struct["score_confiance"], struct["explication_confiance"])
                if match_entry not in grouped_structures[stype]["matches"]:
                    grouped_structures[stype]["matches"].append(match_entry)

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
                    "score_confiance": data["score_confiance"],
                    "explication_confiance": data["explication_confiance"]
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
                for label, obj, conf, expl in data["matches"]:
                    clean_label = label
                    if " - " in clean_label:
                        clean_label = clean_label.split(" - ", 1)[1].strip()
                    combined_objectifs += f"\n  - [{clean_label}] (Confiance : {conf}%) : {obj}"
                    combined_objectifs += f"\n    -> Justification confiance : {expl}"

                final_structures.append({
                    "structure_type": stype,
                    "label": base_label,
                    "priorite": data["priorite"],
                    "pertinence": data["pertinence"],
                    "objectif": combined_objectifs,
                    "score_confiance": data["score_confiance"],
                    "explication_confiance": data["explication_confiance"]
                })

        # On trie par score de priorité (le plus élevé en premier)
        final_structures.sort(key=lambda x: x["priorite"], reverse=True)

        # Si les règles globales imposent une seule structure ou si on veut la meilleure
        allow_multiple = self.rules.get("global_rules", {}).get("allow_multiple_eligible_structures", True)
        if not allow_multiple and final_structures:
            final_structures = [final_structures[0]]

        # Ajout du message d'alerte explicite si la confiance est < 40%
        for struct in final_structures:
            if struct.get("score_confiance", 100) < 40:
                warning_prefix = "[/!\\ INFORMATIONS INSUFFISANTES : Il est vivement conseille de recueillir plus de precisions sur la situation du patient pour fiabiliser cette orientation] "
                struct["objectif"] = warning_prefix + struct.get("objectif", "")

        # Si aucune structure n'est éligible
        if not final_structures:
            age = extracted_data.get("usager.identite.age_estime")
            ville = extracted_data.get("usager.localisation.commune_residence")
            if age is not None or (ville is not None and ville != "inconnu" and ville != "non_renseigne"):
                final_structures.append({
                    "structure_type": "DAC",
                    "label": "DAC - Dispositif d'Appui à la Coordination (Orientation indéterminée)",
                    "priorite": 10,
                    "pertinence": "moyenne",
                    "objectif": "Aucun profil type n'a été identifié pour les autres structures. Orientation vers le DAC pour évaluation globale et coordination.",
                    "score_confiance": 50,
                    "explication_confiance": "Orientation par défaut car la situation ne correspond à aucun parcours standard."
                })
            else:
                final_structures.append({
                    "structure_type": "BESOIN_INFOS",
                    "label": "Informations insuffisantes pour orienter",
                    "priorite": 0,
                    "pertinence": "faible",
                    "objectif": "Les informations fournies ne permettent pas de determiner une orientation. Il est necessaire de recueillir plus de precisions (ex: age de la personne, commune de residence, presence d'aides comme l'APA/professionnels, description precise des difficultes ou de la demande).",
                    "score_confiance": 0,
                    "explication_confiance": "Aucune structure n'est eligible car les informations sont trop incompletes ou absentes dans le recit."
                })

        return final_structures

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
        elif operator == "contains_any":
            if isinstance(target_value, list):
                if isinstance(actual_value, list):
                    return any(str(item) in [str(v) for v in actual_value] for item in target_value)
                return any(str(item) in str(actual_value) for item in target_value)
            return str(target_value) in str(actual_value)
        
        return False

    def _calculate_rule_confidence(self, rule: dict, extracted_data: dict, comid_results: dict) -> tuple[int, str]:
        """
        Calcule de manière hybride la confiance d'une règle d'orientation et produit une explication détaillée.
        """
        fields = []
        for cond in rule.get("all_of", []) + rule.get("any_of", []) + rule.get("none_of", []):
            if "field" in cond:
                fields.append(cond["field"])
        fields = list(set(fields))

        if not fields:
            return 100, "Aucun critère à évaluer."

        FIELD_TO_VAR_MAP = {
            "adresseur.degre_urgence_percu": "urgence",
            "demande.motif_principal": "motif",
            "usager.situation_actuelle.APA": "apa",
            "usager.situation_actuelle.PCH": "pch",
            "usager.situation_actuelle.GIR": "gir",
            "vulnerabilites.sante.suivi_medical.medecin_traitant": "medecin_traitant",
            "usager.situation_actuelle.suspicion_malveillance": "malveillance",
            "vulnerabilites.sante.hospitalisation.statut": "hospitalisation",
            "vulnerabilites.sante.professionnels_domicile": "professionnels_domicile",
            "usager.cadre_de_vie.aidant_regulier": "aidant_regulier",
            "usager.cadre_de_vie.etat_logement": "etat_logement",
            "usager.identite.age_estime": "age",
            "usager.localisation.commune_residence": "ville"
        }

        confiances_variables = extracted_data.get("evaluation.confiance.variables", {})
        confiances_comid = extracted_data.get("evaluation.confiance.comid", {})

        conf_scores = []
        missing_count = 0
        detail_explications = []

        for field in fields:
            if field in FIELD_TO_VAR_MAP:
                var_name = FIELD_TO_VAR_MAP[field]
                actual_val = extracted_data.get(field)
                
                if actual_val is None or str(actual_val).lower() in ["inconnu", "non_renseigne", "incertain"]:
                    conf_scores.append(0)
                    missing_count += 1
                    detail_explications.append(f"variable clé '{var_name}' manquante")
                else:
                    conf = confiances_variables.get(var_name, 100)
                    conf_scores.append(conf)
                    detail_explications.append(f"variable '{var_name}' extraite avec certitude de {conf}%")

            elif field.startswith("evaluation.comid."):
                code = field.replace("evaluation.comid.", "")
                is_present = extracted_data.get(field, False)
                if is_present:
                    conf = confiances_comid.get(code, 100)
                    conf_scores.append(conf)
                    detail_explications.append(f"critère COMID '{code}' détecté avec certitude de {conf}%")
                else:
                    conf_scores.append(100)

            elif field.startswith("complexite."):
                if confiances_comid:
                    avg_comid = sum(confiances_comid.values()) / len(confiances_comid)
                    score_total = comid_results.get("score_total", 0)
                    if score_total >= 10:
                        conf_scores.append(avg_comid)
                        detail_explications.append(f"score complexite COMID estime a {int(avg_comid)}% de certitude (Situation complexe)")
                    elif 6 <= score_total <= 9:
                        val_conf = max(avg_comid - 30, 0)
                        conf_scores.append(val_conf)
                        detail_explications.append(f"score complexite COMID estime a {int(avg_comid)}% de certitude (Penalite de pseudo-complexite de -30% appliquee)")
                    else:
                        val_conf = max(avg_comid - 70, 0)
                        conf_scores.append(val_conf)
                        detail_explications.append(f"score complexite COMID estime a {int(avg_comid)}% de certitude (Penalite de situation non complexe de -70% appliquee)")
                else:
                    conf_scores.append(100)

            else:
                actual_val = extracted_data.get(field)
                if actual_val is None or str(actual_val).lower() in ["inconnu", "non_renseigne", "incertain"]:
                    conf_scores.append(0)
                    missing_count += 1
                    detail_explications.append(f"donnée '{field}' manquante")
                else:
                    conf_scores.append(100)
                    detail_explications.append(f"donnée '{field}' présente (100% certitude)")

        if not conf_scores:
            return 100, "Aucun critère pertinent à évaluer."

        base_confidence = sum(conf_scores) / len(conf_scores)
        penalty = missing_count * 20
        final_confidence = int(min(max(base_confidence - penalty, 0), 100))

        explication = ", ".join(detail_explications)
        if penalty > 0:
            explication += f" (Pénalité de complétude appliquée de -{penalty}% pour {missing_count} variable(s) manquante(s))"

        return final_confidence, explication
