import json

class OrientationResultList(list):
    def __init__(self, items=None, score_breakdown=None):
        super().__init__(items or [])
        self.score_breakdown = score_breakdown or []

class OrientationEngine:
    def __init__(self, rules_path: str):
        with open(rules_path, 'r', encoding='utf-8') as f:
            self.rules = json.load(f)

    def evaluate_orientation(self, extracted_data: dict, comid_results: dict):
        """
        Évalue les garde-fous stricts et accumule les scores cliniques pondérés pour orienter.
        """
        if comid_results is None:
            comid_results = {}

        # Préparation du contexte d'évaluation
        eval_context = {**extracted_data}
        eval_context["complexite.niveau"] = comid_results.get("niveau")
        eval_context["complexite.score_total"] = comid_results.get("score_total")

        # Initialisation de toutes les structures
        all_structures = {
            "POLICE": {"label": "Police / Gendarmerie (Urgence Vitale & Intervention)", "points": 0},
            "CEV": {"label": "CEV - Cellule Écoute et Vigilance (Violences & Spoliation)", "points": 0},
            "SERVICE_SOCIAL_HOPITAL": {"label": "Service Social de l'Hôpital", "points": 0},
            "CLIC": {"label": "CLIC - Centre Local d'Information et de Coordination", "points": 0},
            "CRT": {"label": "CRT - Centre de Ressources Territorial (Accompagnement Renforcé)", "points": 0},
            "DAC": {"label": "DAC - Dispositif d'Appui à la Coordination", "points": 0},
            "UTS": {"label": "UTS / ASPI - Unité Territoriale Sociale (Action Sociale Prévention Insertion)", "points": 0},
            "CCAS": {"label": "CCAS - Centre Communal d'Action Sociale", "points": 0},
            "CPTS": {"label": "CPTS - Communauté Professionnelle Territoriale de Santé", "points": 0},
            "COMPAGNONS_BATISSEURS": {"label": "Les Compagnons Bâtisseurs (Diogène ou Incurie unique/principale)", "points": 0},
            "PSCG_SS_APA": {"label": "PSCG SS APA - Pôle Social de Solidarité et de Gestion (APA)", "points": 0}
        }

        forced_structures = {}  # structure_type -> (priority, objective, guardrail_id)
        excluded_structures = set()

        # 1. ÉVALUATION DES GARDE-FOUS (GUARDRAILS)
        for guardrail in self.rules.get("guardrails", []):
            conditions = guardrail.get("conditions", [])
            match = True
            for cond in conditions:
                if not self._evaluate_condition(cond, eval_context):
                    match = False
                    break
            
            if match:
                stype = guardrail["structure_type"]
                action = guardrail["action"]
                if action == "exclude":
                    excluded_structures.add(stype)
                elif action == "force":
                    forced_structures[stype] = (
                        guardrail.get("priority", 100),
                        guardrail.get("objective", "N/A"),
                        guardrail["id"]
                    )

        # 2. PONDÉRATION DES SCORES CLINIQUES (SCORING RULES)
        matched_rules_per_structure = {}  # stype -> list of (rule_id, points, variables_involved)
        score_breakdown = []

        for rule in self.rules.get("scoring_rules", []):
            conditions = rule.get("conditions", [])
            match = True
            for cond in conditions:
                if not self._evaluate_condition(cond, eval_context):
                    match = False
                    break
            
            if match:
                rule_id = rule["id"]
                points_map = rule.get("points", {})
                
                # Récupérer les variables impliquées dans les conditions (pour le score de confiance)
                vars_involved = [cond.get("field") for cond in conditions if cond.get("field")]
                
                # --- TRAÇABILITÉ DES PHRASES / JUSTIFICATIONS ---
                justification = None
                comid_code = None
                for cond in conditions:
                    f = cond.get("field", "")
                    if f.startswith("evaluation.comid."):
                        comid_code = f.replace("evaluation.comid.", "")
                        break
                
                if comid_code:
                    justifications_list = extracted_data.get("evaluation.comid.justifications", [])
                    if isinstance(justifications_list, list):
                        for j in justifications_list:
                            if isinstance(j, dict) and j.get("code") == comid_code:
                                justification = j.get("justification")
                                break
                    if not justification:
                        justification = f"Critère COMID '{comid_code}' détecté"
                else:
                    # Non-COMID
                    cond_vals = []
                    for cond in conditions:
                        f = cond.get("field")
                        if f:
                            val = eval_context.get(f)
                            cond_vals.append(f"{f.split('.')[-1]} = {val}")
                    justification = ", ".join(cond_vals)

                rule_desc = rule.get("id", "").replace("score_", "").replace("_", " ").capitalize()
                
                # On applique les points uniquement aux structures non exclues
                clean_points = {}
                for stype, pts in points_map.items():
                    if stype not in excluded_structures:
                        all_structures[stype]["points"] += pts
                        clean_points[stype] = pts
                        if stype not in matched_rules_per_structure:
                            matched_rules_per_structure[stype] = []
                        matched_rules_per_structure[stype].append((rule_id, pts, vars_involved))
                
                if clean_points:
                    score_breakdown.append({
                        "rule_id": rule_id,
                        "description": rule_desc,
                        "justification": justification,
                        "points": clean_points
                    })

        # 3. LOGIQUE SPÉCIFIQUE : COMPLEXITÉ ÉLEVÉE (COMID >= 10) -> BONUS DAC
        if comid_results.get("niveau") == "complexe" or comid_results.get("score_total", 0) >= 10:
            if "DAC" not in excluded_structures:
                all_structures["DAC"]["points"] += 70
                if "DAC" not in matched_rules_per_structure:
                    matched_rules_per_structure["DAC"] = []
                matched_rules_per_structure["DAC"].append(("complexite_comid_bonus", 70, ["complexite.score_total"]))
                
                score_breakdown.append({
                    "rule_id": "complexite_comid_bonus",
                    "description": "Complexité COMID >= 10 (Bonus DAC)",
                    "justification": f"Score COMID total = {comid_results.get('score_total')}/30",
                    "points": {"DAC": 70}
                })

        # 4. SÉLECTION ET NORMALISATION DES ORIENTATIONS ÉLIGIBLES
        eligible_structures = []

        for stype, data in all_structures.items():
            if stype in excluded_structures:
                continue

            is_forced = stype in forced_structures
            score = data["points"]

            if is_forced or score > 0:
                if is_forced:
                    priority = forced_structures[stype][0]
                    objective = forced_structures[stype][1]
                    pertinence = "eleve"
                else:
                    priority = score
                    if score >= 50:
                        pertinence = "eleve"
                    elif score >= 25:
                        pertinence = "moyenne"
                    else:
                        pertinence = "faible"
                    
                    objective = f"Orientation clinique recommandée par l'évaluation clinique multicritère (Score : {score} pts)."

                # Calcul dynamique de la confiance
                score_confiance, explication_confiance = self._calculate_hybrid_confidence(
                    stype, is_forced, matched_rules_per_structure.get(stype, []), extracted_data, comid_results
                )

                eligible_structures.append({
                    "structure_type": stype,
                    "label": data["label"],
                    "priorite": priority,
                    "pertinence": pertinence,
                    "objectif": objective,
                    "score_confiance": score_confiance,
                    "explication_confiance": explication_confiance
                })

        # Tri des orientations par priorité décroissante
        eligible_structures.sort(key=lambda x: x["priorite"], reverse=True)

        # 5. FALLBACK : SI AUCUNE STRUCTURE N'EST ÉLIGIBLE MAIS QUE LE CAS EST IDENTIFIABLE -> DAC
        if not eligible_structures:
            age = extracted_data.get("usager.identite.age_estime")
            ville = extracted_data.get("usager.localisation.commune_residence")
            if age is not None or (ville is not None and ville != "inconnu" and ville != "non_renseigne"):
                eligible_structures.append({
                    "structure_type": "DAC",
                    "label": all_structures["DAC"]["label"],
                    "priorite": 10,
                    "pertinence": "moyenne",
                    "objectif": "Aucun profil type n'a été identifié pour les autres structures. Orientation vers le DAC pour évaluation globale et coordination.",
                    "score_confiance": 50,
                    "explication_confiance": "Orientation par défaut car la situation ne correspond à aucun parcours standard."
                })
            else:
                eligible_structures.append({
                    "structure_type": "BESOIN_INFOS",
                    "label": "Informations insuffisantes pour orienter",
                    "priorite": 0,
                    "pertinence": "faible",
                    "objectif": "Les informations fournies ne permettent pas de determiner une orientation. Il est necessaire de recueillir plus de precisions (ex: age de la personne, commune de residence, presence d'aides comme l'APA/professionnels, description precise des difficultes ou de la demande).",
                    "score_confiance": 0,
                    "explication_confiance": "Aucune structure n'est eligible car les informations sont trop incompletes ou absentes dans le recit."
                })

        # Alerte si la confiance globale est trop basse (< 40%)
        for struct in eligible_structures:
            if struct.get("score_confiance", 100) < 40:
                warning_prefix = "[/!\\ INFORMATIONS INSUFFISANTES : Il est vivement conseille de recueillir plus de precisions sur la situation du patient pour fiabiliser cette orientation] "
                struct["objectif"] = warning_prefix + struct.get("objectif", "")

        return OrientationResultList(eligible_structures, score_breakdown=score_breakdown)

    def _evaluate_condition(self, condition: dict, data: dict):
        field = condition.get("field")
        operator = condition.get("operator")
        target_value = condition.get("value")
        
        actual_value = data.get(field)

        if operator == "==":
            if actual_value is None or target_value is None:
                return str(actual_value) == str(target_value)
            return str(actual_value) == str(target_value)
        elif operator == "!=":
            return str(actual_value) != str(target_value)
        elif operator == ">=":
            if actual_value is None or target_value is None:
                return False
            try:
                return float(actual_value) >= float(target_value)
            except:
                return False
        elif operator == "<=":
            if actual_value is None or target_value is None:
                return False
            try:
                return float(actual_value) <= float(target_value)
            except:
                return False
        elif operator == ">":
            if actual_value is None or target_value is None:
                return False
            try:
                return float(actual_value) > float(target_value)
            except:
                return False
        elif operator == "<":
            if actual_value is None or target_value is None:
                return False
            try:
                return float(actual_value) < float(target_value)
            except:
                return False
        elif operator == "in":
            if actual_value is None or target_value is None:
                return False
            if isinstance(target_value, list):
                return str(actual_value) in [str(v) for v in target_value]
            return str(actual_value) in str(target_value)
        elif operator == "contains_any":
            if actual_value is None or target_value is None:
                return False
            if isinstance(target_value, list):
                if isinstance(actual_value, list):
                    return any(str(item) in [str(v) for v in actual_value] for item in target_value)
                return any(str(item) in str(actual_value) for item in target_value)
            return str(target_value) in str(actual_value)
        
        return False

    def _calculate_hybrid_confidence(self, stype, is_forced, matched_rules, extracted_data, comid_results):
        """
        Calcule de manière hybride la certitude des informations supportant l'orientation.
        """
        if is_forced:
            return 100, "Orientation d'urgence absolue ou réglementaire forcée."

        if not matched_rules:
            return 50, "Basé sur des critères généraux par défaut."

        # Récupérer l'ensemble des variables contributrices
        vars_involved = []
        for rule_id, pts, fields in matched_rules:
            vars_involved.extend(fields)
        
        vars_involved = list(set(vars_involved))
        if not vars_involved:
            return 100, "Critères stables d'orientation."

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

        for field in vars_involved:
            if field in FIELD_TO_VAR_MAP:
                var_name = FIELD_TO_VAR_MAP[field]
                actual_val = extracted_data.get(field)
                
                if actual_val is None or str(actual_val).lower() in ["inconnu", "non_renseigne", "incertain", "none", "null"]:
                    conf_scores.append(0)
                    missing_count += 1
                    detail_explications.append(f"variable clé '{var_name}' manquante")
                else:
                    conf = confiances_variables.get(var_name, 100)
                    conf_scores.append(conf)
                    detail_explications.append(f"variable '{var_name}' extraite à {conf}%")

            elif field.startswith("evaluation.comid."):
                code = field.replace("evaluation.comid.", "")
                is_present = extracted_data.get(field, False)
                if is_present:
                    conf = confiances_comid.get(code, 100)
                    conf_scores.append(conf)
                    detail_explications.append(f"critère COMID '{code}' détecté à {conf}%")
                else:
                    conf_scores.append(100)

            elif field.startswith("complexite."):
                if confiances_comid:
                    avg_comid = sum(confiances_comid.values()) / len(confiances_comid)
                    conf_scores.append(avg_comid)
                    detail_explications.append(f"complexité COMID ({int(avg_comid)}% certitude)")
                else:
                    conf_scores.append(100)
            else:
                conf_scores.append(100)

        if not conf_scores:
            return 100, "Orientation stable."

        base_confidence = sum(conf_scores) / len(conf_scores)
        penalty = missing_count * 15
        final_confidence = int(min(max(base_confidence - penalty, 0), 100))

        explication = ", ".join(detail_explications)
        if penalty > 0:
            explication += f" (Pénalité de complétude de -{penalty}% appliquée)"

        return final_confidence, explication
