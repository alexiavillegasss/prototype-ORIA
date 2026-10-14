import json
import os
import re
import pandas as pd

class OrientationEngine:
    def __init__(self, rules_path: str):
        # Charge la version JSON pour compatibilité et fallbacks potentiels
        try:
            with open(rules_path, 'r', encoding='utf-8') as f:
                self.rules = json.load(f)
        except Exception as e:
            self.rules = {}
            print(f"Warning: could not load orientation_rules.json: {e}")
            
        # Déduit le chemin vers les fichiers de règles Excel (dans le même dossier rules)
        self.rules_dir = os.path.dirname(rules_path)
        self.available_matrices = {
            "cassi": {
                "id": "cassi",
                "filename": "tableauORIA - NOMENCLATURE-CASSI.xlsx",
                "label": "Nomenclature CASSI (Nouveau & Précis)",
                "description": "Matrice enrichie avec la nomenclature nationale CASSI (95 besoins & prestations)"
            },
            "legacy": {
                "id": "legacy",
                "filename": "tableau_oria.xlsx",
                "label": "Standard ORIA (Historique)",
                "description": "Matrice initiale originale d'ORIA (58 besoins regroupés)"
            }
        }
        self.active_matrix_id = "cassi"
        self.excel_path = os.path.join(self.rules_dir, self.available_matrices[self.active_matrix_id]["filename"])
        
        # Mappings des structures de la feuille 1 vers les identifiants techniques
        self.structure_mapping = {
            "POLICE": "POLICE",
            "CEV": "CEV",
            "SERVICE SOCIAL HÔPITAL": "SERVICE_SOCIAL_HOPITAL",
            "PRADO": "PRADO",
            "PSCG SS APA": "PSCG_SS_APA",
            "CRT": "CRT",
            "CLIC": "CLIC",
            "CPTS": "CPTS",
            "MISAS": "MISAS",
            "CCAS": "CCAS"
        }

        self.structure_missions = {
            "CLIC": "Le CLIC (Centre Local d'Information et de Coordination) est un service public de proximité qui informe, évalue et coordonne gratuitement l'ensemble des aides pour le maintien à domicile des personnes âgées de 60 ans et plus.",
            "DAC": "Le DAC (Dispositif d'Appui à la Coordination) vient en appui aux professionnels pour coordonner l'accompagnement des personnes en situation clinique complexe ou avec cumuls de vulnérabilités.",
            "CCAS": "Le CCAS (Centre Communal d'Action Sociale) est le service municipal de proximité qui attribue les aides sociales d'urgence, alimentaires et d'accompagnement du quotidien.",
            "UTS": "L'UTS (Unité Territoriale Sociale du Conseil Départemental) assure l'accompagnement social global des usagers et des familles en situation de précarité ou de vulnérabilité.",
            "CRT": "Le CRT (Centre de Ressources Territorial) offre un accompagnement renforcé et coordonné à domicile comme alternative directe à l'entrée en EHPAD.",
            "MISAS": "La MISAS (Mission d'Appui en Santé Mentale) apporte un soutien spécialisé pour l'orientation et la prise en charge des besoins en santé mentale et psychiatrie.",
            "POLICE": "La Police et la Gendarmerie interviennent en urgence absolue pour assurer la protection des personnes, faire cesser les violences et prévenir les détresses vitales.",
            "CEV": "La CEV (Cellule Écoute et Vigilance) enregistre et traite les signalements de maltraitance, de danger ou de spoliation d'adultes vulnérables.",
            "COMPAGNONS_BATISSEURS": "Les Compagnons Bâtisseurs interviennent directement à domicile pour l’insalubrité, la réhabilitation et la désinfection du logement (syndrome de Diogène, incurie).",
            "CPTS": "La CPTS (Communauté Professionnelle Territoriale de Santé) facilite l'accès aux soins de premier recours en coordonnant les médecins traitants, infirmiers et kinésithérapeutes du secteur.",
            "SERVICE_SOCIAL_HOPITAL": "Le Service Social Hospitalier prépare et organise le plan d'aides et de soins à domicile en amont de la sortie d'établissement d'hospitalisation.",
            "PSCG_SS_APA": "Ce service départemental évalue le niveau de perte d'autonomie (GIR) et attribue l'APA (Allocation Personnalisée d'Autonomie) pour financer les aides à domicile.",
            "PRADO": "Le programme PRADO de l'Assurance Maladie anticipe et sécurise le retour à domicile du patient après une hospitalisation.",
            "fil d'argent": "Le Fil d'Argent est une plateforme téléphonique dédiée au soutien psychologique, au répit et à l'écoute des aidants familiaux.",
            "CONSULTATION MÉMOIRE": "La Consultation Mémoire réalise le bilan et le suivi médical spécialisé des troubles de la mémoire et des fonctions cognitives."
        }
        self.structure_domains = {
            "POLICE": {"id": "securite_urgence", "label": "Urgence Vitale & Protection (Sécurité)"},
            "CEV": {"id": "securite_urgence", "label": "Protection & Vigilance (Signalement)"},
            "CLIC": {"id": "medico_social", "label": "Accompagnement & Maintien à Domicile (Médico-Social)"},
            "CRT": {"id": "medico_social", "label": "Accompagnement Renforcé à Domicile (Médico-Social)"},
            "DAC": {"id": "medico_social", "label": "Coordination des Parcours Complexes (Médico-Social)"},
            "CCAS": {"id": "medico_social", "label": "Action Sociale & Aides de Proximité (Social)"},
            "UTS": {"id": "medico_social", "label": "Accompagnement Social Global (Social)"},
            "PSCG_SS_APA": {"id": "medico_social", "label": "Évaluation & Instruction APA (Autonomie)"},
            "COMPAGNONS_BATISSEURS": {"id": "medico_social", "label": "Aménagement & Salubrité du Logement (Habitat)"},
            "SERVICE_SOCIAL_HOPITAL": {"id": "medico_social", "label": "Préparation de Sortie d'Hospitalisation (Social)"},
            "PRADO": {"id": "medico_social", "label": "Retour à Domicile Post-Hospitalisation (Santé-Social)"},
            "CPTS": {"id": "sante_soins", "label": "Accès aux Soins & Médecin Traitant (Médical / Soins)"},
            "CONSULTATION MÉMOIRE": {"id": "sante_soins", "label": "Bilan & Suivi Spécialisé de la Mémoire (Médical)"},
            "MISAS": {"id": "sante_soins", "label": "Appui & Prévention en Santé Mentale (Médical / Psychique)"},
            "fil d'argent": {"id": "aidants", "label": "Soutien & Écoute des Aidants"}
        }
        
        # Mappings des critères de la feuille 1 vers les conditions techniques
        self.condition_map = {
            "La situation est critique et la demande concerne un secours d'urgence immédiat.": 
                lambda d, c, text_lower: d.get("adresseur.degre_urgence_percu") == "critique" and d.get("demande.motif_principal") == "secours_urgence",
            "Violences sexuelles": 
                lambda d, c, text_lower: d.get("usager.situation_actuelle.suspicion_malveillance") == "violences_sexuelles",
            "Violences conjugales": 
                lambda d, c, text_lower: d.get("usager.situation_actuelle.suspicion_malveillance") in ["violences_physiques", "violences_psychologiques"] and ("conjugal" in text_lower or "conjoint" in text_lower),
            "Violences psychologiques": 
                lambda d, c, text_lower: d.get("usager.situation_actuelle.suspicion_malveillance") == "violences_psychologiques",
            "Spoliation financière": 
                lambda d, c, text_lower: d.get("usager.situation_actuelle.suspicion_malveillance") in ["spoliation_financiere", "abus_de_confiance_ou_faiblesse"] or any(k in text_lower for k in ["prenne de l'argent", "prend de l'argent", "vol d'argent", "voler de l'argent", "spoliation", "dérobe", "extorsion"]),
            "Négligence": 
                lambda d, c, text_lower: d.get("usager.situation_actuelle.suspicion_malveillance") == "negligence",
            "Négligence professionnelle":
                lambda d, c, text_lower: d.get("usager.situation_actuelle.suspicion_malveillance") in ["negligence", "maltraitance_institutionnelle"],
            "Abus de confiance ou abus de faiblesse": 
                lambda d, c, text_lower: d.get("usager.situation_actuelle.suspicion_malveillance") in ["abus_de_confiance_ou_faiblesse", "spoliation_financiere"] or "abus de faiblesse" in text_lower or "abus de confiance" in text_lower,
            "Privation de droits": 
                lambda d, c, text_lower: d.get("usager.situation_actuelle.suspicion_malveillance") == "privation_de_droits",
            "Maltraitance institutioinnelle": 
                lambda d, c, text_lower: d.get("usager.situation_actuelle.suspicion_malveillance") == "maltraitance_institutionnelle",
            "Sécurité du domicile problématique critique ou danger iminnent": 
                lambda d, c, text_lower: d.get("vulnerabilites.habitat.securite_du_domicile") in ["problematique", "critique", "danger_imminent"],
            "Problématique non sociale": 
                lambda d, c, text_lower: not (d.get("vulnerabilites.social.precarite") in ["possible", "probable", "averee"] or d.get("evaluation.comid.precarite_financiere") is True),
            "Sortie d'hospitalisation de + de 10 jours": 
                lambda d, c, text_lower: d.get("vulnerabilites.sante.hospitalisation.statut") != "recente",
            "La personne a 75 ans ou moins.": 
                lambda d, c, text_lower: d.get("usager.identite.age_estime") is not None and float(d.get("usager.identite.age_estime")) <= 75,
            "La personne a 60 ans ou moins.": 
                lambda d, c, text_lower: d.get("usager.identite.age_estime") is not None and float(d.get("usager.identite.age_estime")) <= 60,
            "La personne n'a pas l'APA.": 
                lambda d, c, text_lower: d.get("usager.situation_actuelle.APA") != "oui",
            "La personne bénéficie déjà de l'APA.": 
                lambda d, c, text_lower: d.get("usager.situation_actuelle.APA") == "oui",
            "La personne a 60 ans ou moins et ne bénéficie pas de la PCH.": 
                lambda d, c, text_lower: d.get("usager.identite.age_estime") is not None and float(d.get("usager.identite.age_estime")) <= 60 and d.get("usager.situation_actuelle.PCH") != "oui",
            "Médecin traitant identifié": 
                lambda d, c, text_lower: d.get("vulnerabilites.sante.suivi_medical.medecin_traitant") == "identifie" and not any(k in text_lower for k in ["retraite", "partir à la retraite", "plus de médecin", "cherche un médecin"]),
            "Médecin traitant ne se déplace plus": 
                lambda d, c, text_lower: "ne se déplace plus" in text_lower or "ne se deplace plus" in text_lower,
            "Recherche de kinésithérapeute": 
                lambda d, c, text_lower: any(kw in text_lower for kw in ["cherche kiné", "cherche kinésithérapeute", "recherche kiné", "besoin de kiné", "ordonnance de kiné", "séances de kiné"]),
            "Recherche d'infirmière": 
                lambda d, c, text_lower: any(kw in text_lower for kw in ["cherche infirmière", "cherche infirmier", "recherche idel", "besoin d'infirmier", "soins infirmiers à domicile"]),
            "Recherche de Médecin Traitant": 
                lambda d, c, text_lower: any(kw in text_lower for kw in ["cherche médecin", "cherche medecin", "recherche médecin", "recherche medecin", "plus de médecin", "sans médecin", "retraite du mt", "départ à la retraite"]),
            "Évaluation médicale": 
                lambda d, c, text_lower: "médical" in text_lower or "medical" in text_lower or "médecin" in text_lower or "medecin" in text_lower
        }

        # Charge les règles et la matrice de besoins depuis le fichier Excel
        self._load_excel_rules()

    def _get_condition_checker(self, detail_name: str):
        if not detail_name:
            return None
        norm_target = str(detail_name).replace("’", "'").strip().lower()
        for k, checker in self.condition_map.items():
            if k.replace("’", "'").strip().lower() == norm_target:
                return checker
        return None

    def set_matrix(self, matrix_id: str):
        """Bascule vers une matrice spécifique ('cassi' ou 'legacy') et recharge les règles."""
        if matrix_id not in self.available_matrices:
            raise ValueError(f"Matrice inconnue: '{matrix_id}'. Disponibles: {list(self.available_matrices.keys())}")
        self.active_matrix_id = matrix_id
        self.excel_path = os.path.join(self.rules_dir, self.available_matrices[matrix_id]["filename"])
        self._load_excel_rules()
        return self.get_active_matrix_info()

    def get_active_matrix_info(self):
        info = self.available_matrices[self.active_matrix_id].copy()
        info["needs_count"] = len(self.needs_mapping)
        info["rules_count"] = len(self.prioritization_rules) + len(self.exclusion_rules)
        return info

    def get_available_matrices(self):
        result = []
        for m_id, m_info in self.available_matrices.items():
            item = m_info.copy()
            item["active"] = (m_id == self.active_matrix_id)
            path = os.path.join(self.rules_dir, m_info["filename"])
            item["exists"] = os.path.exists(path)
            if m_id == self.active_matrix_id:
                item["rules_count"] = len(self.needs_mapping)
            else:
                item["rules_count"] = 95 if m_id == "cassi" else 58
            result.append(item)
        return result

    def _load_excel_rules(self):
        if not os.path.exists(self.excel_path):
            print(f"Warning: Excel rules file not found: {self.excel_path}")
            return
        self.last_excel_mtime = os.path.getmtime(self.excel_path)
        
        # 1. Charge Feuille 1: Exclusions et Garde-fous (avec tolérance sur le nom de l'onglet)
        try:
            xl = pd.ExcelFile(self.excel_path)
            sheet1_name = "01_Critère_prio_exclu"
            if sheet1_name not in xl.sheet_names:
                for s in xl.sheet_names:
                    if "01" in s or "prio" in s.lower() or "critere" in s.lower() or "exclu" in s.lower():
                        sheet1_name = s
                        break
            df1 = pd.read_excel(self.excel_path, sheet_name=sheet1_name)
            df1.columns = [str(c).strip() for c in df1.columns]
        except Exception as e:
            print(f"Warning: could not load sheet 1 from {self.excel_path}: {e}")
            df1 = pd.DataFrame()
        
        self.prioritization_rules = []
        self.exclusion_rules = []
        
        if not df1.empty:
            for idx, row in df1.iterrows():
                detail = row.get("Critère détaillé")
                action = row.get("Action")
                struct = row.get("Structure")
                conseil = row.get("Conseils")
                
                if pd.isna(detail) or pd.isna(action) or pd.isna(struct):
                    continue
                    
                detail = str(detail).strip()
                action = str(action).strip()
                struct = str(struct).strip()
                
                struct_code = self.structure_mapping.get(struct, struct)
                
                rule_item = {
                    "detail": detail,
                    "action": action,
                    "structure": struct_code,
                    "priority": 100.0 if action == "Prioritaire" else 0.0,
                    "objectif": f"Priorisé selon le critère : {detail}" if action == "Prioritaire" else f"Exclu selon le critère : {detail}",
                    "conseil": str(conseil).strip() if pd.notna(conseil) and str(conseil).strip() != "nan" else ""
                }
                
                if action == "Prioritaire":
                    self.prioritization_rules.append(rule_item)
                elif action == "Exclu":
                    self.exclusion_rules.append(rule_item)
                    
        # 2. Charge Feuille 2: Cartographie des Besoins (avec détection dynamique de l'onglet et des colonnes CASSI)
        try:
            xl = pd.ExcelFile(self.excel_path)
            sheet2_name = "02_Besoins_x_structures (2)"
            if sheet2_name not in xl.sheet_names:
                for s in xl.sheet_names:
                    if "02" in s or "besoin" in s.lower():
                        sheet2_name = s
                        break
                else:
                    sheet2_name = xl.sheet_names[1] if len(xl.sheet_names) > 1 else xl.sheet_names[0]
            df2 = pd.read_excel(self.excel_path, sheet_name=sheet2_name)
            df2.columns = [str(c).strip() for c in df2.columns]
        except Exception as e:
            print(f"Warning: could not load sheet 2 from {self.excel_path}: {e}")
            df2 = pd.DataFrame()

        self.needs_mapping = []
        self.structures = ['POLICE', 'CEV', 'SERVICE_SOCIAL_HOPITAL', 'CPTS', 'CLIC', 'CRT', 'DAC', 'UTS', 'CCAS', 'COMPAGNONS_BATISSEURS', 'PSCG_SS_APA', 'PRADO', 'MISAS', "fil d'argent", 'CONSULTATION MÉMOIRE']
        
        if not df2.empty:
            cassi_prob_col = next((c for c in df2.columns if "cassi" in c.lower() and ("prob" in c.lower() or "problématique" in c.lower())), None)
            cassi_bes_col = next((c for c in df2.columns if "cassi" in c.lower() and "besoin" in c.lower()), None)
            cassi_prest_col = next((c for c in df2.columns if "cassi" in c.lower() and "prest" in c.lower()), None)

            for idx, row in df2.iterrows():
                detail = row.get("Besoin détaillé")
                if pd.isna(detail) or not str(detail).strip():
                    continue
                kw = row.get("Mots-clés / critère moteur")
                struct_proposee = row.get("Structure principale proposée")
                categorie = row.get("Catégorie")
                conseil_val = row.get("Conseils")
                
                # Extraction CASSI sécurisée
                c_prob = ""
                if cassi_prob_col and pd.notna(row.get(cassi_prob_col)):
                    val_p = str(row.get(cassi_prob_col)).strip()
                    if val_p.lower() not in ['x', '-', 'nan', 'none']:
                        c_prob = val_p
                        
                c_bes = ""
                if cassi_bes_col and pd.notna(row.get(cassi_bes_col)):
                    val_b = str(row.get(cassi_bes_col)).strip()
                    if val_b.lower() not in ['x', '-', 'nan', 'none']:
                        c_bes = val_b
                        
                c_prest = ""
                if cassi_prest_col and pd.notna(row.get(cassi_prest_col)):
                    val_pr = str(row.get(cassi_prest_col)).strip()
                    if val_pr.lower() not in ['x', '-', 'nan', 'none']:
                        c_prest = val_pr

                struct_cochees = []
                for s in self.structures:
                    col_match = next((c for c in df2.columns if c.strip() == s), None)
                    if not col_match:
                        col_match = next((c for c in df2.columns if c.strip().lower() == s.lower() or c.strip().lower() == s.lower().replace('_', ' ')), None)
                    if col_match:
                        val = row.get(col_match)
                        if pd.notna(val) and str(val).strip() in ['✓', '✔', 'x', 'X', '1', 'oui', 'true', 'OUI', 'True']:
                            struct_cochees.append(s)
                        
                self.needs_mapping.append({
                    "categorie": str(categorie).strip() if pd.notna(categorie) else "",
                    "cassi_problematique": c_prob,
                    "cassi_besoin": c_bes,
                    "cassi_prestation": c_prest,
                    "detaille": str(detail).strip(),
                    "moteur_criteria": str(kw).strip() if pd.notna(kw) else "",
                    "struct_proposee": str(struct_proposee).strip() if pd.notna(struct_proposee) else "",
                    "structures_cochees": struct_cochees,
                    "conseil": str(conseil_val).strip() if pd.notna(conseil_val) and str(conseil_val).strip() != "nan" else ""
                })

    def _reload_excel_if_modified(self):
        try:
            if os.path.exists(self.excel_path):
                current_mtime = os.path.getmtime(self.excel_path)
                if getattr(self, 'last_excel_mtime', 0) != current_mtime:
                    self._load_excel_rules()
        except Exception as e:
            print(f"Warning: could not reload excel rules: {e}")

    def evaluate_orientation(self, extracted_data: dict, comid_results: dict, original_text: str = "", matrix: str = None):
        """
        Calcule l'orientation recommandée à l'aide d'un algorithme par points.
        matrix: 'cassi' ou 'legacy' (si None, utilise la matrice active courante).
        """
        if matrix and matrix in self.available_matrices and matrix != self.active_matrix_id:
            self.set_matrix(matrix)
        else:
            self._reload_excel_if_modified()
        # Prépare le contexte d'évaluation complet
        eval_context = {**extracted_data}
        eval_context["complexite.niveau"] = comid_results.get("niveau")
        eval_context["complexite.score_total"] = comid_results.get("score_total")
        
        text_lower = original_text.lower() if original_text else ""
        if text_lower:
            import re
            text_lower = re.sub(r'\b([Aa])([0-9]{2,4})\b', r'\1 \2', text_lower)
            text_lower = re.sub(r'\b(6|8)01([1-9])\b', lambda m: ('7' if m.group(1) == '6' else '9') + m.group(2), text_lower)
            text_lower = re.sub(r'\b(6|8)0\s+1([1-9])\b', lambda m: ('7' if m.group(1) == '6' else '9') + m.group(2), text_lower)
            text_lower = re.sub(r'\b([2-9])0([1-9])\b', r'\1\2', text_lower)
            text_lower = re.sub(r'\b([2-9])0\s+([1-9])\b', r'\1\2', text_lower)

        # Nettoyage des artéfacts d'âge issus de la reconnaissance vocale
        raw_age = eval_context.get("usager.identite.age_estime")
        if raw_age is not None:
            try:
                age_val = float(raw_age)
                if age_val > 120:
                    str_age = str(int(age_val))
                    if len(str_age) == 4 and str_age[1] == '0' and str_age[2] == '1':
                        decade = '7' if str_age[0] == '6' else '9'
                        eval_context["usager.identite.age_estime"] = int(decade + str_age[3])
                    elif len(str_age) == 3 and str_age[1] == '0':
                        eval_context["usager.identite.age_estime"] = int(str_age[0] + str_age[2])
            except:
                pass
        
        # Prétraitement du texte pour la détection des besoins :
        # On masque les présentations de l'adresseur ("je suis kinésithérapeute", "je suis IDE", "je suis médecin", etc.)
        # afin de ne pas interpréter la profession du professionnel appelant comme un besoin manquant pour le patient.
        speaker_regex = (
            r'\b(?:bonjour\s*,?\s*)?je suis (?:le |la |un |une )?(?:masseur-)?(?:kinésithérapeute|kinesitherapeute|kiné|kine|'
            r'infirmière libérale|infirmiere liberale|infirmier libéral|infirmier liberal|infirmière|infirmiere|infirmier|idel?|'
            r'médecin traitant|medecin traitant|médecin|medecin|mt|docteur|généraliste|generaliste|neurologue|gériatre|geriatre|psychiatre|'
            r'assistante? sociale?|as|travailleur social|travailleuse sociale)\b[^.,;\n]*'
        )
        patient_text = re.sub(speaker_regex, ' ', text_lower, flags=re.IGNORECASE)
        
        # On masque également les mentions de professionnels déjà mis en place (ex: "nous avons mis en place infirmier libéral, kiné")
        in_place_regex = (
            r'\b(?:nous avons mis en place|a déjà mis en place|ont mis en place|intervient déjà|passent déjà|passage d\'un|passage d\'une)\s+'
            r'[^.,;\n]*'
        )
        patient_text = re.sub(in_place_regex, ' ', patient_text, flags=re.IGNORECASE)

        # Étape 1 : Garde-fous prioritaires
        triggered_garde_fous = []
        for rule in self.prioritization_rules:
            detail = rule["detail"]
            checker = self._get_condition_checker(detail)
            if checker:
                try:
                    if checker(eval_context, eval_context, text_lower):
                        rule_copy = rule.copy()
                        # Si Spoliation financière ou Abus de faiblesse dans un contexte de signalement/protection sans agression physique armée en cours
                        # => la CEV est la cellule d'écoute et de vigilance référente
                        if detail in ["Spoliation financière", "Abus de confiance ou abus de faiblesse"]:
                            is_armed_vital_emergency = (
                                eval_context.get("adresseur.degre_urgence_percu") == "critique" or
                                any(w in text_lower for w in ["arme", "couteau", "frappe en cours", "agression physique", "17", "secours d'urgence"])
                            )
                            if not is_armed_vital_emergency:
                                rule_copy["structure"] = "CEV"
                                rule_copy["objectif"] = f"Signalement et protection d'adulte vulnérable (Maltraitance / Spoliation) : {detail}"
                        triggered_garde_fous.append(rule_copy)
                except Exception as e:
                    print(f"Error checking prio rule {detail}: {e}")
                
        if triggered_garde_fous:
            # Tri par priorité décroissante
            triggered_garde_fous.sort(key=lambda x: x["priority"], reverse=True)
            winner = triggered_garde_fous[0]
            struct_type = winner["structure"]
            label = self._get_structure_label(struct_type)
            
            identified_conseils_detail = []
            for gf in triggered_garde_fous:
                c = gf.get("conseil")
                if c and str(c).strip() and str(c).strip() != "nan":
                    c_clean = str(c).strip()
                    if not any(item["text"] == c_clean for item in identified_conseils_detail):
                        identified_conseils_detail.append({
                            "text": c_clean,
                            "verbatim": self._extract_verbatim(gf.get("detail", ""), "", original_text)
                        })

            for need in self.needs_mapping:
                if self._is_need_identified(need, eval_context, patient_text):
                    c = need.get("conseil")
                    if c and str(c).strip() and str(c).strip() != "nan":
                        c_clean = str(c).strip()
                        if not any(item["text"] == c_clean for item in identified_conseils_detail):
                            criteria_search = str(need.get("moteur_criteria", "") or "")
                            if "addiction" in need["detaille"].lower():
                                criteria_search += ", médicaments, medicaments, doses, surdosage, addiction, alcool, drogues, antalgiques"
                            identified_conseils_detail.append({
                                "text": c_clean,
                                "verbatim": self._extract_verbatim(need["detaille"], criteria_search, original_text)
                            })

            conseils_simple_texts = [item["text"] for item in identified_conseils_detail]

            final_elements_detail = []
            for gf in triggered_garde_fous:
                final_elements_detail.append({
                    "titre": gf.get("detail", "Signalement de situation d'urgence"),
                    "verbatim": self._extract_verbatim(gf.get("detail", ""), "", original_text)
                })

            orientation_result = {
                "structure_type": struct_type,
                "label": label,
                "priorite": int(winner["priority"]),
                "pertinence": "eleve",
                "objectif": winner["objectif"],
                "score_confiance": 100,
                "explication_confiance": "Priorisation absolue par garde-fou prioritaire.",
                "conseils": conseils_simple_texts,
                "ressources": identified_conseils_detail,
                "mission_structure": self.structure_missions.get(struct_type, "Structure d'accompagnement et d'orientation d'urgence."),
                "elements_recit": [winner.get("detail", "Signalement d'urgence ou de situation critique identifié dans la saisie.")],
                "elements_recit_detail": final_elements_detail
            }
            
            # Enrichit extracted_data pour la traçabilité dans l'interface
            extracted_data["evaluation.moteur_points.active_matrix"] = self.active_matrix_id
            extracted_data["evaluation.moteur_points.active_matrix_label"] = self.available_matrices[self.active_matrix_id]["label"]
            extracted_data["evaluation.moteur_points.priorisations_declenchees"] = [winner["structure"]]
            extracted_data["evaluation.moteur_points.scores"] = {s: 0 for s in self.structures}
            extracted_data["evaluation.moteur_points.scores"][struct_type] = int(winner["priority"])
            extracted_data["evaluation.moteur_points.besoins_identifies"] = []
            extracted_data["evaluation.moteur_points.exclusions_declenchees"] = []
            
            return [orientation_result]
            
        # Étape 2 : Attribution des points par besoin détecté (seulement si le besoin est lié à des structures)
        scores = {struct: 0 for struct in self.structures}
        identified_needs = []
        identified_conseils_detail = []
        scored_struct_per_need = set()
        
        danger_needs = [
            "spoliation financière", "spoliation financiere",
            "violence conjugale", "violence",
            "maltraitance", "abus de confiance", "abus de faiblesse",
            "privation de droits", "privation de droit"
        ]
        
        for need in self.needs_mapping:
            if self._is_need_identified(need, eval_context, patient_text):
                verbatim = self._extract_verbatim(need["detaille"], need.get("moteur_criteria", ""), original_text)
                need_obj = {
                    "detaille": need["detaille"],
                    "categorie": need.get("categorie", ""),
                    "cassi_problematique": need.get("cassi_problematique", ""),
                    "cassi_besoin": need.get("cassi_besoin", ""),
                    "cassi_prestation": need.get("cassi_prestation", ""),
                    "moteur_criteria": need.get("moteur_criteria", ""),
                    "structures_cochees": need.get("structures_cochees", []),
                    "verbatim": verbatim
                }

                if len(need["structures_cochees"]) > 0:
                    is_dup = any(
                        ex["detaille"] == need_obj["detaille"] and 
                        ex.get("cassi_prestation") == need_obj.get("cassi_prestation")
                        for ex in identified_needs
                    )
                    if not is_dup:
                        identified_needs.append(need_obj)

                    detail_lower = need["detaille"].lower().replace("’", "'").strip()
                    is_danger = any(dn in detail_lower for dn in danger_needs)
                    for s in need["structures_cochees"]:
                        if s in scores:
                            # Déduplication équitable des points par couple (structure, besoin)
                            score_key = (s, detail_lower)
                            if score_key not in scored_struct_per_need:
                                scored_struct_per_need.add(score_key)
                                if is_danger and s in ["CEV", "POLICE"]:
                                    scores[s] += 100
                                else:
                                    scores[s] += 1

                c_text = need.get("conseil")
                if c_text and str(c_text).strip() and str(c_text).strip() != "nan":
                    c_clean = str(c_text).strip()
                    # Filtre de sécurité : Les entreprises de nettoyage spécialisées ne sont conseillées qu'en cas d'insalubrité / Diogène avéré
                    if "nettoyage" in c_clean.lower() or "sociétés spécialisées" in c_clean.lower():
                        has_real_insalubrite = any(k in text_lower for k in ["diogène", "diogene", "incurie", "insalubre", "insalubrité", "nettoyage extrême", "nettoyage extreme", "désinfection", "desinfection", "très sale", "tres sale"])
                        if not has_real_insalubrite:
                            continue

                    if not any(item["text"] == c_clean for item in identified_conseils_detail):
                        crit_search = str(need.get("moteur_criteria", "") or "")
                        if "addiction" in need["detaille"].lower():
                            crit_search += ", médicaments, medicaments, doses, surdosage, addiction, alcool, drogues, antalgiques"
                        v_final = verbatim if (verbatim and verbatim.strip()) else self._extract_verbatim(need["detaille"], crit_search, original_text)
                        identified_conseils_detail.append({
                            "text": c_clean,
                            "verbatim": v_final
                        })
                        
        # Étape 3 : Application des exclusions
        excluded_structures = []
        for rule in self.exclusion_rules:
            detail = rule["detail"]
            struct_type = rule["structure"]
            checker = self._get_condition_checker(detail)
            if checker:
                try:
                    if checker(eval_context, eval_context, text_lower):
                        # Ne pas exclure la CPTS si la personne cherche explicitement un médecin traitant / visite à domicile
                        if struct_type == "CPTS" and any(k in text_lower for k in ["retraite", "partir à la retraite", "plus de médecin", "cherche un médecin", "besoin d'un médecin", "visite au domicile", "visites au domicile"]):
                            continue
                        excluded_structures.append(struct_type)
                except Exception as e:
                    print(f"Error checking exclusion rule {detail}: {e}")
                    
        # Exclure Compagnons Bâtisseurs si pas de Diogène ou incurie ou insalubrité avérée dans le récit
        has_real_insalubrite = any(
            kw in text_lower for kw in [
                "diogène", "diogene", "incurie", "insalubre", "insalubrité", "insalubrite",
                "très sale", "tres sale", "dépotoir", "depotoir", "poubelles partout",
                "odeur d'urine", "odeur d’urine", "désinfection", "desinfection", "auto-réhabilitation", "auto-rehabilitation"
            ]
        )
        if not has_real_insalubrite:
            if "COMPAGNONS_BATISSEURS" not in excluded_structures:
                excluded_structures.append("COMPAGNONS_BATISSEURS")
            scores["COMPAGNONS_BATISSEURS"] = -9999
        else:
            scores["COMPAGNONS_BATISSEURS"] += 100
                
        # Remise à zéro/pénalisation extrême pour les structures exclues
        for s in excluded_structures:
            if s in scores:
                scores[s] = -9999
                
        # Étape 4 : Règles métier complémentaires
        
        # 4.1 : UTS vs CCAS
        # Si UTS et CCAS et besoin social complexe ➡️ UTS l'emporte sur CCAS (besoin d'assistante sociale)
        # Sinon, simple aide alimentaire / courses / isolement ➡️ CCAS l'emporte sur UTS
        if scores.get("UTS", 0) > 0 and scores.get("CCAS", 0) > 0:
            has_complex_social_need = False
            complex_social_keywords = ["évaluation sociale", "evaluation sociale", "droits sociaux", "ouverture", "accompagnement social", "logement", "surendettement", "budget"]
            for need in identified_needs:
                if need["categorie"] == "Social / droits / budget":
                    if any(kw in need["detaille"].lower() for kw in complex_social_keywords):
                        has_complex_social_need = True
                        break
                        
            # Si senior (>= 60 ans), le CCAS est privilégié pour l'accompagnement social de proximité et les aides seniors (ex: ASH)
            age = eval_context.get("usager.identite.age_estime")
            if age is not None and age >= 60:
                scores["CCAS"] = max(scores["UTS"], scores["CCAS"]) + 1
                scores["UTS"] = scores["UTS"] - 1
            elif has_complex_social_need:
                scores["UTS"] = max(scores["UTS"], scores["CCAS"]) + 1
                scores["CCAS"] = scores["CCAS"] - 1
            else:
                scores["CCAS"] = max(scores["UTS"], scores["CCAS"]) + 1
                scores["UTS"] = scores["UTS"] - 1
                
        # 4.2 : CRT vs CLIC
        # CRT (Centre de Ressources Territorial) : accompagnement renforcé à domicile, alternative à l'entrée en EHPAD
        crt_triggers = [
            "retarder l'entrée en ehpad" in text_lower or "retarder l'ehpad" in text_lower or "retarder entree en ehpad" in text_lower,
            "éviter l'entrée en ehpad" in text_lower or "eviter l'ehpad" in text_lower or "alternative à l'ehpad" in text_lower or "alternative a l'ehpad" in text_lower,
            "accompagnement plus global des équipes" in text_lower or "accompagnement renforcé" in text_lower or "accompagnement renforce" in text_lower,
            ("a déjà des aides" in text_lower or "déjà des aides" in text_lower or "aides déjà en place" in text_lower or "équipes qui sont déjà en place" in text_lower or "equipes qui sont deja en place" in text_lower or "équipes déjà en place" in text_lower) and ("dégrade" in text_lower or "degrade" in text_lower or "insuffisant" in text_lower),
            ("refus de soins" in text_lower or "refus d'hospitalisation" in text_lower or "refus d’hospitalisation" in text_lower) and ("chutes" in text_lower or "épuisée" in text_lower or "epuisee" in text_lower or "conjugopathie" in text_lower),
            comid_results.get("score_total", 0) >= 6
        ]
        if any(crt_triggers) and "CRT" not in excluded_structures:
            scores["CRT"] = max(scores.get("CRT", 0), scores.get("CLIC", 0)) + 5
            if "CLIC" in scores:
                scores["CLIC"] = max(scores["CLIC"] - 2, 0)
        else:
            # Si demande d'aide à domicile pour un senior sans critère CRT -> CLIC prioritaire
            is_clic_aide_domicile = (
                ("aide à domicile" in text_lower or "aides à domicile" in text_lower or "aide a domicile" in text_lower or "aides a domicile" in text_lower) and
                "CLIC" not in excluded_structures
            )
            if is_clic_aide_domicile:
                scores["CLIC"] = max(scores.get("CLIC", 0), scores.get("CRT", 0) + 2, 6)
            
        # 4.3 : CLIC vs CCAS pour les seniors
        # Si senior isolé avec demande d'aide aux courses / portage repas / aide alimentaire sans réseau familial de proximité (ex: Cas 04)
        is_proximity_ccas = (
            ("courses" in text_lower or "portage de repas" in text_lower or "aide alimentaire" in text_lower) and
            ("isolé" in text_lower or "isole" in text_lower or "seul" in text_lower or "sans famille" in text_lower or "étranger" in text_lower or "etranger" in text_lower) and
            not any(kw in text_lower for kw in ["ehpad", "gir", "apa", "cognitif", "alzheimer", "démence", "demence", "crt", "chute", "chutes"])
        )
        if is_proximity_ccas and "CCAS" not in excluded_structures:
            scores["CCAS"] = max(scores.get("CCAS", 0), scores.get("CLIC", 0)) + 3
        elif scores.get("CLIC", 0) > 0 and scores.get("CCAS", 0) > 0:
            is_ash_request = (
                "hébergement" in text_lower or 
                "hebergement" in text_lower or 
                "ash" in text_lower.split()
            ) and (
                "aide sociale" in text_lower or 
                "aide social" in text_lower or 
                "payer" in text_lower or 
                "financ" in text_lower or 
                "moyen" in text_lower
            )
            has_geriatric_need = False
            geriatric_keywords = ["troubles cognitifs", "troubles cognitifs", "autonomie", "médico-sociale", "medico-sociale", "ehpad", "gir", "apa", "aménagement", "amenagement", "mobilité", "mobilite", "maintien"]
            for need in identified_needs:
                if any(kw in need["detaille"].lower() for kw in geriatric_keywords):
                    has_geriatric_need = True
                    break
            if has_geriatric_need and not is_ash_request:
                scores["CLIC"] = max(scores["CLIC"], scores["CCAS"]) + 1
                scores["CCAS"] = scores["CCAS"] - 1
                
        # 4.3 : Évaluation de la redirection vers le DAC
        person_cannot_move = (
            eval_context.get("vulnerabilites.autonomie.deplacements_exterieurs") == "impossibles" or
            eval_context.get("vulnerabilites.autonomie.mobilite") == "tres_limitee" or
            "ne peut pas se déplacer" in text_lower or
            "ne peut plus se déplacer" in text_lower or
            "déplacement impossible" in text_lower or
            "déplacements impossibles" in text_lower or
            "alité" in text_lower
        )
        
        refusal_by_establishment = (
            "refusé par l'établissement" in text_lower or
            "refusé par l'ehpad" in text_lower or
            "refus de l'établissement" in text_lower or
            "refus de l'ehpad" in text_lower or
            "refusé par la structure" in text_lower or
            "refuse par l'etablissement" in text_lower or
            "refuse par l'ehpad" in text_lower or
            "refuse par la structure" in text_lower
        )
        
        # Redirection refus établissement vers CLIC (si présent)
        if refusal_by_establishment and "CLIC" not in excluded_structures:
            scores["CLIC"] = max(scores.values()) + 1
            
        temp_winner = max(scores, key=scores.get)
        
        is_dac_situation = (
            "parcours de soins" in text_lower or
            ("santé mentale" in text_lower and ("précar" in text_lower or "expulsion" in text_lower or "surendettement" in text_lower or "toxico" in text_lower or "addiction" in text_lower)) or
            ("psychologique" in text_lower and ("social" in text_lower or "logement" in text_lower or "parano" in text_lower)) or
            ("signalement" in text_lower and ("seule professionnelle" in text_lower or "parano" in text_lower)) or
            (
                (
                    extracted_data.get("evaluation.comid.psychiatrie") is True or
                    extracted_data.get("evaluation.comid.addiction") is True or
                    extracted_data.get("evaluation.comid.depression") is True
                ) and (
                    extracted_data.get("evaluation.comid.precarite_financiere") is True or
                    extracted_data.get("evaluation.comid.logement_inadapte") is True or
                    "expulsion" in text_lower or "surendettement" in text_lower
                )
            )
        )

        redirection_dac = (
            is_dac_situation or
            (temp_winner == "UTS" and person_cannot_move) or
            (len(identified_needs) > 5 and comid_results.get("score_total", 0) >= 6) or
            (refusal_by_establishment and "CLIC" in excluded_structures) or
            (
                (
                    extracted_data.get("evaluation.comid.psychiatrie") is True or
                    extracted_data.get("evaluation.comid.addiction") is True or
                    extracted_data.get("evaluation.comid.depression") is True
                ) and len(identified_needs) >= 4
            )
        )
        
        # Exceptions à la redirection DAC
        if scores.get("POLICE", 0) >= 100 or scores.get("CEV", 0) >= 100:
            redirection_dac = False
        elif scores.get("CRT", 0) > 0 and not is_dac_situation and not (
            extracted_data.get("evaluation.comid.psychiatrie") is True or
            extracted_data.get("evaluation.comid.addiction") is True or
            extracted_data.get("evaluation.comid.depression") is True
        ):
            redirection_dac = False
            
        # Application de la redirection DAC
        if redirection_dac:
            scores["DAC"] = max(scores.values()) + 10
            if temp_winner == "UTS" and person_cannot_move:
                scores["UTS"] = -9999
        elif comid_results.get("score_total", 0) < 6 and not is_dac_situation:
            scores["DAC"] = -9999

        # 4.4 : Fil d'Argent est toujours une Ressource Complémentaire et ne crée jamais de carte principale
        scores["fil d'argent"] = -9999
        has_aidant_need = any(kw in text_lower for kw in ["aidant", "aidante", "aidants", "fatigue", "épuisé", "epuise", "surmené", "surmene", "répit", "repit", "soulager"])
        if has_aidant_need:
            v_aidant = self._extract_verbatim("Relais de l'aidant", "aidant, aidante, surmené, surmene, fatigué, épuisé, epuise, répit, repit, soulager", original_text)
            fil_text = "Se rapprocher du Fil d'Argent - Relais et écoute des aidants"
            if not any(item["text"] == fil_text for item in identified_conseils_detail):
                identified_conseils_detail.append({
                    "text": fil_text,
                    "verbatim": v_aidant
                })

        # 4.5 : Règle CPTS pour la recherche de médecin traitant
        cpts_section_obj = None
        has_primary_medecin_need = (
            (
                eval_context.get("demande.motif_principal") == "recherche_medecin" or
                ("retraite" in text_lower and ("médecin" in text_lower or "medecin" in text_lower or "mt" in text_lower or "patientèle" in text_lower or "patientele" in text_lower)) or
                ("n'a plus de médecin" in text_lower or "plus de médecin" in text_lower or "pas de médecin" in text_lower or "sans médecin" in text_lower) or
                ("visites au domicile" in text_lower or "visite au domicile" in text_lower or "visite à domicile" in text_lower or "certificat mdph" in text_lower)
            ) and not redirection_dac
        )
        has_medecin_search = (
            has_primary_medecin_need or
            eval_context.get("vulnerabilites.sante.suivi_medical.medecin_traitant") in ["absent", "non_identifie_avec_certitude"] or
            "médecin" in text_lower or
            "medecin" in text_lower or
            "traitant" in text_lower or
            "retraite" in text_lower
        )
        if has_primary_medecin_need:
            # La recherche de médecin traitant / accès aux soins est la demande N°1
            current_max = max([s for s in scores.values() if s > -9000] or [0])
            scores["CPTS"] = max(current_max + 10, 25)
            # Ne pas exclure la CPTS même si patient < 60 ans car la CPTS s'adresse à tout âge
            if "CPTS" in excluded_structures:
                excluded_structures.remove("CPTS")
            cpts_section_obj = None
        elif has_medecin_search and "CPTS" not in excluded_structures:
            v_med = self._extract_verbatim("Recherche de médecin traitant", "médecin, medecin, traitant, docteur, soins, retraite", original_text)
            cpts_section_obj = {
                "structure_type": "CPTS",
                "label": self._get_structure_label("CPTS"),
                "mission_structure": self.structure_missions.get("CPTS"),
                "elements_recit_detail": [{
                    "titre": "Recherche de médecin traitant / Accès aux soins de premier recours",
                    "verbatim": v_med
                }]
            }
            # La CPTS est intégrée en section 2 du cube unique et ne génère pas de cube principal distinct
            scores["CPTS"] = -9999

        # Étape 5 : Mise en forme des candidats avec tri par niveau de priorité et hierarchie par défaut
        hierarchy = ["POLICE", "CEV", "SERVICE_SOCIAL_HOPITAL", "CLIC", "CRT", "UTS", "CCAS", "CPTS", "DAC", "PSCG_SS_APA", "PRADO", "MISAS", "fil d'argent", "CONSULTATION MÉMOIRE", "COMPAGNONS_BATISSEURS"]
        hierarchy_dict = {struct: i for i, struct in enumerate(hierarchy)}
        
        candidates = [(s, score) for s, score in scores.items() if score > 0]
        candidates.sort(key=lambda x: (x[1], -hierarchy_dict.get(x[0], 99)), reverse=True)
        
        final_structures = []
        for struct_type, score in candidates:
            # Pertinence selon les points
            if score >= 3:
                pertinence = "eleve"
            else:
                pertinence = "moyenne"
                
            # Confection de l'objectif d'orientation en montrant uniquement le besoin principal
            besoin_p = eval_context.get("demande.besoin_principal", "indetermine")
            if besoin_p and besoin_p != "indetermine":
                # On vérifie si ce besoin principal est lié à cette structure
                is_linked = False
                for need in self.needs_mapping:
                    if need["detaille"] == besoin_p and struct_type in need["structures_cochees"]:
                        is_linked = True
                        break
                if is_linked:
                    objectif = f"Besoin identifié : {besoin_p}"
                else:
                    objectif = f"Besoin principal : {besoin_p} (Structure complémentaire)"
            else:
                # Si pas de besoin principal trouvé
                objectif = "Aucun besoin principal trouvé."
                
            label = self._get_structure_label(struct_type)
            
            seen_titles = set()
            seen_verbatims = set()
            elements_detail = []

            for n in identified_needs:
                if struct_type in n.get("structures_cochees", []):
                    t = n["detaille"]
                    v = n.get("verbatim", "")
                    t_norm = t.lower().strip()
                    
                    if t_norm not in seen_titles:
                        seen_titles.add(t_norm)
                        final_v = ""
                        if v and v not in seen_verbatims:
                            final_v = v
                            seen_verbatims.add(v)
                        elements_detail.append({
                            "titre": t,
                            "verbatim": final_v
                        })

            if not elements_detail:
                besoin_p = eval_context.get("demande.besoin_principal")
                if besoin_p and besoin_p != "indetermine":
                    elements_detail = [{"titre": f"Demande en lien avec : {besoin_p}", "verbatim": self._extract_verbatim(besoin_p, "", original_text)}]
                else:
                    elements_detail = [{"titre": "Éléments cliniques généraux rapportés dans votre saisie", "verbatim": ""}]

            # Règle d'explicabilité : si usager < 60 ans et orienté vers le DAC, l'expliquer explicitement
            age_val = eval_context.get("usager.identite.age_estime")
            if struct_type == "DAC" and age_val is not None:
                try:
                    if float(age_val) < 60:
                        v_age = self._extract_verbatim("Âge de la personne", f"{int(float(age_val))} ans, {int(float(age_val))}, ans, âge, age", original_text)
                        elements_detail.insert(0, {
                            "titre": f"Usager âgé de moins de 60 ans ({int(float(age_val))} ans) : le DAC assure l'accompagnement et la coordination (le CLIC intervenant uniquement à partir de 60 ans)",
                            "verbatim": v_age
                        })
                except Exception:
                    pass

            struct_elements_titles = [e["titre"] for e in elements_detail]
            conseils_simple_texts = [c["text"] for c in identified_conseils_detail]

            dom_info = self.structure_domains.get(struct_type, {"id": "autre", "label": "Accompagnement Complémentaire"})

            struct_obj = {
                "structure_type": struct_type,
                "label": label,
                "domaine_id": dom_info["id"],
                "domaine_label": dom_info["label"],
                "priorite": score,
                "pertinence": pertinence,
                "objectif": objectif,
                "score_confiance": 100,
                "explication_confiance": f"Calculé par points. Score : {score} point(s).",
                "conseils": conseils_simple_texts,
                "ressources": identified_conseils_detail,
                "mission_structure": self.structure_missions.get(struct_type, "Structure d'accompagnement et d'orientation."),
                "elements_recit": struct_elements_titles,
                "elements_recit_detail": elements_detail,
                "cpts_section": cpts_section_obj.copy() if (cpts_section_obj and struct_type in ["CLIC", "DAC", "CRT", "CCAS", "UTS"]) else None
            }
            final_structures.append(struct_obj)
            
        # Fallback par défaut si rien n'est éligible
        if not final_structures:
            age = eval_context.get("usager.identite.age_estime")
            is_senior = False
            try:
                if age is not None and float(age) >= 60:
                    is_senior = True
            except:
                pass
                
            conseils_simple_texts = [c["text"] for c in identified_conseils_detail]

            if is_senior:
                final_structures.append({
                    "structure_type": "CLIC",
                    "label": self._get_structure_label("CLIC"),
                    "domaine_id": "medico_social",
                    "domaine_label": "Accompagnement & Maintien à Domicile (Médico-Social)",
                    "priorite": 0,
                    "pertinence": "faible",
                    "objectif": "Aucun besoin spécifique identifié. Orientation vers le CLIC sénior par défaut.",
                    "score_confiance": 50,
                    "explication_confiance": "Orientation par défaut pour senior.",
                    "conseils": conseils_simple_texts,
                    "ressources": identified_conseils_detail,
                    "mission_structure": self.structure_missions.get("CLIC"),
                    "elements_recit": ["Demande d'information et d'orientation globale pour personne âgée de 60 ans ou plus."],
                    "elements_recit_detail": [{"titre": "Demande d'information et d'orientation globale pour personne âgée de 60 ans ou plus", "verbatim": original_text[:120] if original_text else ""}],
                    "cpts_section": cpts_section_obj.copy() if cpts_section_obj else None
                })
            else:
                v_age = ""
                age_str = ""
                if age is not None:
                    try:
                        age_str = f" ({int(float(age))} ans)"
                        v_age = self._extract_verbatim("Âge de la personne", f"{int(float(age))} ans, {int(float(age))}, ans, âge, age", original_text)
                    except Exception:
                        pass

                final_structures.append({
                    "structure_type": "DAC",
                    "label": self._get_structure_label("DAC"),
                    "domaine_id": "medico_social",
                    "domaine_label": "Coordination des Parcours Complexes (Médico-Social)",
                    "priorite": 0,
                    "pertinence": "faible",
                    "objectif": "Orientation vers le DAC pour accompagnement et coordination.",
                    "score_confiance": 50,
                    "explication_confiance": "Orientation pour usager de moins de 60 ans.",
                    "conseils": conseils_simple_texts,
                    "ressources": identified_conseils_detail,
                    "mission_structure": self.structure_missions.get("DAC"),
                    "elements_recit": ["Usager de moins de 60 ans : accompagnement et coordination par le DAC (le CLIC étant réservé aux personnes de 60 ans et plus)."],
                    "elements_recit_detail": [
                        {
                            "titre": f"Usager âgé de moins de 60 ans{age_str} : le DAC assure l'accompagnement et la coordination (le CLIC intervenant uniquement à partir de 60 ans)",
                            "verbatim": v_age if v_age else (original_text[:120] if original_text else "")
                        }
                    ],
                    "cpts_section": cpts_section_obj.copy() if cpts_section_obj else None
                })
            
        # Stocke les métriques d'explicabilité pour le front
        priorisations_declenchees = []
        for rule in self.prioritization_rules:
            detail = rule["detail"]
            if detail in self.condition_map:
                checker = self.condition_map[detail]
                try:
                    if checker(eval_context, eval_context, text_lower):
                        priorisations_declenchees.append(rule["structure"])
                except Exception as e:
                    print(f"Error checking prio rule {detail}: {e}")
                    
        extracted_data["evaluation.moteur_points.active_matrix"] = self.active_matrix_id
        extracted_data["evaluation.moteur_points.active_matrix_label"] = self.available_matrices[self.active_matrix_id]["label"]
        extracted_data["evaluation.moteur_points.priorisations_declenchees"] = priorisations_declenchees
        extracted_data["evaluation.moteur_points.scores"] = {s: int(score) if score > -9000 else -9999 for s, score in scores.items()}
        extracted_data["evaluation.moteur_points.besoins_identifies"] = [
            {
                "detaille": need["detaille"],
                "categorie": need["categorie"],
                "cassi_problematique": need.get("cassi_problematique", ""),
                "cassi_besoin": need.get("cassi_besoin", ""),
                "cassi_prestation": need.get("cassi_prestation", ""),
                "structures_cochees": need["structures_cochees"]
            }
            for need in identified_needs
        ]
        extracted_data["evaluation.moteur_points.exclusions_declenchees"] = excluded_structures
        
        return final_structures

    def _evaluate_condition_list(self, condition_list: list, data: dict) -> bool:
        for cond in condition_list:
            if not self._evaluate_condition(cond, data):
                return False
        return True

    def _evaluate_condition(self, condition: dict, data: dict) -> bool:
        field = condition.get("field")
        operator = condition.get("operator")
        target_value = condition.get("value")
        
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
        elif operator == "<=":
            try:
                return float(actual_value) <= float(target_value)
            except:
                return False
        elif operator == "!=":
            return str(actual_value) != str(target_value)
        elif operator == "in":
            if isinstance(target_value, list):
                return str(actual_value) in [str(v) for v in target_value]
            return str(actual_value) in str(target_value)
        elif operator == "contains_any":
            if isinstance(target_value, list):
                if isinstance(actual_value, list):
                    return any(str(item) in [str(v) for v in actual_value] for item in target_value)
                return any(str(item) in str(actual_value) for item in target_value)
            return str(target_value) in str(actual_value)
        
        return False

    def _is_need_identified(self, need: dict, data: dict, text: str) -> bool:
        criteria_str = need["moteur_criteria"].lower()
        if not criteria_str or criteria_str == "nan":
            return self._is_need_identified_textual(need, text)
            
        criteria_list = [c.strip() for c in criteria_str.split(",") if c.strip()]
        
        # Enforce COMID/precarity factors if they are present in the criteria list.
        comid_precarity_keys = [
            "troubles_cognitifs", "trouble_cognitif_aigu", "perte_autonomie_recente", 
            "degradation_recente", "epuisement_aidant", "precarite_sociale", 
            "precarite_financiere", "douleurs"
        ]
        
        has_comid_in_criteria = False
        comid_matched = False
        for c in criteria_list:
            if c in comid_precarity_keys:
                has_comid_in_criteria = True
                if c in ["troubles_cognitifs", "trouble_cognitif_aigu"]:
                    if self._match_single_criterion("troubles_cognitifs", data) or self._match_single_criterion("trouble_cognitif_aigu", data):
                        comid_matched = True
                else:
                    if self._match_single_criterion(c, data):
                        comid_matched = True
                        
        if has_comid_in_criteria and not comid_matched:
            return self._is_need_identified_textual(need, text)
            
        # Si un des critères techniques correspond (relation OR), le besoin est identifié
        tech_matched = False
        for c in criteria_list:
            if self._match_single_criterion(c, data):
                tech_matched = True
                break
                
        if tech_matched:
            # Pour les besoins spécifiques et sensibles, on exige aussi que le texte contienne les mots-clés lexicaux associés
            detail_lower = need["detaille"].lower()
            needs_requiring_lexical = [
                "logement", "financière", "financiere", "kinésithérapeute", "kinesitherapeute",
                "infirmier", "médecin", "medecin", "spoliation", "violence", "maltraitance",
                "abus", "négligence", "negligence", "droits", "budget", "facture",
                "accompagnement", "social", "évaluation", "evaluation", "veille", "suivi",
                "secours", "urgence", "administrative", "administratives",
                "diogène", "diogene", "incurie", "insalubre", "insalubrité", "nettoyage", "réhabilitation", "rehabilitation"
            ]
            if any(kw in detail_lower for kw in needs_requiring_lexical):
                return self._is_need_identified_textual(need, text)
            return True
            
        # Fallback lexical si la correspondance technique échoue
        return self._is_need_identified_textual(need, text)

    def _is_need_identified_textual(self, need: dict, text: str) -> bool:
        if not text:
            return False
            
        detail_lower = need["detaille"].lower().replace("’", "'").strip()
        text = text.replace("’", "'")

        # Helper flags pour aides et maintien à domicile
        has_aide_phrases = [
            "aide à domicile", "aide a domicile", "aides à domicile", "aides a domicile",
            "aides au domicile", "aide au domicile", "auxiliaire de vie", "saad", "ssiad",
            "mal à sortir", "du mal à sortir", "ne peut plus sortir", "plus sortir",
            "mal à se déplacer", "perte d'autonomie", "perte de mobilité", "difficulté à sortir",
            "difficultés à sortir", "seule à la maison", "seule chez elle", "au quotidien",
            "courses", "ménage", "menage", "accompagnement médicaux", "sorties"
        ]
        has_aide = any(p in text for p in has_aide_phrases) or "ad" in text.split()
        has_maintien = "maintien" in text and "domicile" in text or "maintien à domicile" in text or "maintien a domicile" in text or "rester à domicile" in text or "rester a domicile" in text
        has_refus = "refus" in text or "refusé" in text or "refuse" in text or "ne veut pas" in text or "ne veut plus" in text or "opposition" in text

        # Addictions / Alcool / Drogues / Médicaments
        if "addiction" in detail_lower or "addictions" in detail_lower or "alcool" in detail_lower or "drogue" in detail_lower or "médicament" in detail_lower or "medicament" in detail_lower or "toxicomanie" in detail_lower:
            addiction_kws = ["addiction", "addictions", "alcool", "alcoolisme", "drogue", "drogues", "substance", "toxico", "toxicomanie", "toxicomane", "addictologie", "arcasud", "dépendance", "dependance", "boit", "boit trop", "bouteille", "médicament", "médicaments", "medicament", "medicaments"]
            if any(kw in text for kw in addiction_kws):
                return True

        # Protection Juridique / Tutelle / Curatelle / Signalement
        if "protection" in detail_lower or "tutelle" in detail_lower or "curatelle" in detail_lower or "signalement" in detail_lower:
            protection_kws = [
                "tutelle", "curatelle", "protection juridique", "sauvegarde de justice", 
                "mandataire", "mandataire judiciaire", "mjpm", "inapte", "incapable",
                "ne peut plus décider", "ne peut plus decider", "ne peut plus gérer", "ne peut plus gerer",
                "juges des contentieux", "juge des tutelles", "tribunal de proximité", "tribunal de proximite",
                "habilitation familiale", "mise sous tutelle", "mise sous curatelle", "sous tutelle", "sous curatelle",
                "autonomie décisionnelle", "autonomie decisionnelle", "gestion des comptes", "spoliation", "signalement", "protéger", "proteger"
            ]
            if any(kw in text for kw in protection_kws):
                return True

        # Correspondance directe par prestation CASSI spécifique si présente
        cassi_p = need.get("cassi_prestation", "")
        if cassi_p and cassi_p not in ["x", "-", "nan"]:
            cassi_p_norm = cassi_p.lower().replace("’", "'").replace("(", " ").replace(")", " ")
            stopwords = {"dans", "pour", "avec", "sans", "sous", "vers", "chez", "leur", "plus", "tout", "tous", "toute", "toutes", "prise", "charge", "cadre", "appui", "recherche", "dispositif", "aide"}
            p_words = [w for w in re.findall(r'\b\w{4,}\b', cassi_p_norm) if w not in stopwords]
            if p_words:
                matching = [w for w in p_words if w in text]
                if len(matching) >= 2 or (len(p_words) == 1 and matching):
                    return True

        # Nettoyage extrême / Diogène / Incurie / Insalubrité (Sociétés de nettoyage spécialisées / Compagnons Bâtisseurs - UNIQUEMENT SI INSALUBRITÉ SÉVÈRE)
        if "diogène" in detail_lower or "diogene" in detail_lower or "incurie" in detail_lower or "insalubrité" in detail_lower or "insalubre" in detail_lower:
            diogene_kws = ["diogène", "diogene", "incurie", "insalubre", "insalubrité", "nettoyage extrême", "nettoyage extreme", "très sale", "tres sale", "désinfection", "desinfection", "désencombrement", "desencombrement", "auto-réhabilitation", "auto-rehabilitation"]
            if any(kw in text for kw in diogene_kws):
                return True

        # 1. Urgent / Danger
        if "danger vital" in detail_lower or "secours d’urgence" in detail_lower or "secours d'urgence" in detail_lower:
            if re.search(r'\b(secours|urgence|danger|agression|agressions)\b', text):
                return True
        if "violence conjugale" in detail_lower:
            has_v_kw = re.search(r'\b(violence|violences|frappe|frapper|battu|battre|coups?)\b', text)
            has_c_kw = re.search(r'\b(conjugale?|conjoint|mari|épouse|epouse|femme|voisin)\b', text)
            if has_v_kw and has_c_kw:
                return True
        if "violence" in detail_lower or "violences" in detail_lower:
            if re.search(r'\b(violence|violences|agression|agressions|coups?|ecchymoses|bleus?|frappe|frapper|battu|battre)\b', text):
                return True
        if "maltraitance" in detail_lower or "négligence" in detail_lower or "negligence" in detail_lower:
            if re.search(r'\b(maltraitance|maltraitant|maltraiter|maltraité|maltraitée|négligence|negligence)\b', text):
                return True
        if "sécurité du domicile" in detail_lower or "securite du domicile" in detail_lower:
            if "sécurité" in text or "securite" in text or "danger" in text or "effondre" in text or "délabré" in text:
                return True

        # 2. Santé / Accès aux soins
        if "recherche de médecin" in detail_lower or "recherche de medecin" in detail_lower:
            if ("cherche" in text or "recherche" in text or "trouver" in text or "besoin" in text or "n'a plus" in text or "n’a plus" in text or "pas de" in text or "sans" in text or "plus de" in text) and ("médecin" in text or "medecin" in text or "traitant" in text):
                return True
        if "visite à domicile" in detail_lower or "visite a domicile" in detail_lower or "vad" in detail_lower:
            if ("médecin" in text or "medecin" in text or "docteur" in text) and ("visite" in text or "déplace" in text or "deplace" in text or "vad" in text.split()):
                return True
        if "kinésithérapeute" in detail_lower or "kinesitherapeute" in detail_lower:
            if ("cherche" in text or "recherche" in text or "besoin" in text or "trouver" in text or "demande" in text) and ("kiné" in text or "kine" in text or "kinésithérapeute" in text or "kinesitherapeute" in text):
                return True
        if "infirmier" in detail_lower or "idel" in detail_lower:
            if ("cherche" in text or "recherche" in text or "besoin" in text or "trouver" in text or "demande" in text) and ("infirmier" in text or "infirmière" in text or "infirmiere" in text or "idel" in text):
                return True
        if "recherche de professionnels" in detail_lower:
            if ("cherche" in text or "recherche" in text) and ("santé mentale" in text or "sante mentale" in text or "psychiatre" in text or "psychologue" in text):
                return True
        if "accès aux soins" in detail_lower or "acces aux soins" in detail_lower:
            if "accès" in text or "acces" in text or "soins" in text or "médical" in text or "medical" in text:
                return True
        if "renoncement aux soins" in detail_lower or "renoncement aux soins" in detail_lower:
            if "renonce" in text or "renoncement" in text or "refuse de se soigner" in text:
                return True
        if "retour à domicile" in detail_lower or "retour a domicile" in detail_lower or "post-hospitalisation" in detail_lower:
            if "retour" in text and ("hospitalisation" in text or "hôpital" in text or "hopital" in text or "sortie" in text):
                return True
        if "besoin paramédical" in detail_lower or "besoin paramedical" in detail_lower:
            if "paramédical" in text or "paramedical" in text or "soins" in text or "pansement" in text:
                return True

        # 3. Autonomie / Aidants
        if "portage de repas" in detail_lower or "portage de repas" in detail_lower:
            if "portage" in text or "repas" in text:
                return True
        if "téléalarme" in detail_lower or "telealarme" in detail_lower or "alarme" in detail_lower:
            if "téléalarme" in text or "telealarme" in text or "alarme" in text or "bracelet" in text:
                return True
        if "évaluation sociale" in detail_lower or "evaluation sociale" in detail_lower:
            if "social" in text and ("évaluation" in text or "evaluation" in text):
                return True
        if "évaluation globale" in detail_lower or "evaluation globale" in detail_lower or "médico-sociale" in detail_lower or "medico-sociale" in detail_lower:
            if "point global" in text or "évaluation" in text or "evaluation" in text or "médico-sociale" in text or "medico-sociale" in text:
                return True
        if ("aménagement" in detail_lower or "amenagement" in detail_lower or "adaptation" in detail_lower) and "diogène" not in detail_lower and "diogene" not in detail_lower:
            if "aménagement" in text or "amenagement" in text or "aménager" in text or "amenager" in text or "adapter" in text or "adaptation" in text or "barre" in text or "douche" in text or "chute" in text or "chutes" in text:
                return True
        if "maintien renforcé" in detail_lower or "maintien renforce" in detail_lower or "maintien intensif" in detail_lower:
            if "renforc" in text or "intensif" in text or ("refus" in text and "soin" in text) or ("déjà des aides" in text and ("dégrade" in text or "insuffisant" in text)):
                return True
        if "alternative à l’ehpad" in detail_lower or "alternative a l'ehpad" in detail_lower:
            if "ehpad" in text or "maison de retraite" in text or "retarder l'entrée" in text or "retarder l'entree" in text:
                return True
        if "relais" in detail_lower or "aidant" in detail_lower:
            if "relais" in text or "épuisement" in text or "epuisement" in text or "aidant" in text or "famille" in text:
                return True
        if "troubles cognitifs" in detail_lower:
            if "cognitive" in text or "cognitif" in text or "mémoire" in text or "memoire" in text or "alzheimer" in text or "désorienté" in text:
                return True
        if "perte d’autonomie" in detail_lower or "perte d'autonomie" in detail_lower or "perte autonomie" in detail_lower:
            if "autonomie" in text or "se dégrade" in text or "se degrade" in text or "dégradation" in text or "degradation" in text:
                return True
        if "réévaluation" in detail_lower or "reevaluation" in detail_lower:
            if "réévaluation" in text or "reevaluation" in text or "revoir" in text or "réévaluer" in text or "reevaluer" in text:
                return True
        if "adaptation" in detail_lower and "plan d'aide" in detail_lower:
            if "adaptation" in text or "adapter" in text:
                return True
        if "suivi médical" in detail_lower or "suivi medical" in detail_lower:
            if "suivi" in text or "médical" in text or "medical" in text:
                return True

        # 4. Social / Droits / Budget
        if "droits sociaux" in detail_lower or "ouverture des droits" in detail_lower:
            if "droits" in text or "ouverture" in text or "dossier" in text or "aide sociale" in text or "hébergement" in text or "hebergement" in text:
                return True
        if "accompagnement social" in detail_lower:
            if "accompagnement social" in text or ("accompagnement" in text and "social" in text) or "assistante sociale" in text or "assistant social" in text:
                return True
        if "budget" in detail_lower or "évaluation budgétaire" in detail_lower or "evaluation budgetaire" in detail_lower:
            if "budget" in text or "budgétaire" in text or "budgetaire" in text or "dette" in text or "dettes" in text or "surendettement" in text:
                return True
        if "aide financière" in detail_lower or "aide financiere" in detail_lower:
            if "aide financière" in text or "aide financiere" in text or "financier" in text or "financière" in text or "moyens" in text or "payer" in text or "hébergement" in text or "hebergement" in text or "aide sociale" in text:
                return True
        if "démarches" in detail_lower or "demarches" in detail_lower or "administrative" in detail_lower:
            if "démarches" in text or "demarches" in text or "paperasse" in text or "courrier" in text or "dossier" in text or "administration" in text:
                return True
        if "aide alimentaire" in detail_lower or "alimentaire" in detail_lower:
            if "alimentaire" in text or "manger" in text or "nourriture" in text or "courses" in text or "frigo" in text:
                return True
        if "facture" in detail_lower or "factures" in detail_lower:
            if "facture" in text or "factures" in text or "dette" in text or "dettes" in text or "payer" in text:
                return True
        if "logement" in detail_lower or "rechercher un logement" in detail_lower:
            if "logement" in text or "appartement" in text or "maison" in text or "déménagement" in text or "demenagement" in text:
                return True
        if "isolement" in detail_lower or "rompre l’isolement" in detail_lower:
            if "isolement" in text or "isolé" in text or "isole" in text or "seul" in text or "seule" in text:
                return True
        if "veille" in detail_lower or "suivi social régulier" in detail_lower:
            if "veille" in text or "suivi social" in text or "suivi régulier" in text or "suivi regulier" in text or "visite régulière" in text or "visite reguliere" in text:
                return True
        if "diogène" in detail_lower or "diogene" in detail_lower or "incurie" in detail_lower or "insalubre" in detail_lower or "insalubrité" in detail_lower:
            if "diogène" in text or "diogene" in text or "incurie" in text or "insalubre" in text or "insalubrité" in text or "nettoyage extrême" in text or "nettoyage extreme" in text or "désinfection" in text or "desinfection" in text or "très sale" in text or "tres sale" in text:
                return True

        # 5. Maintien et Aides à domicile (core triggers)
        if detail_lower == "maintien à domicile" or detail_lower == "maintien a domicile":
            return (has_maintien or has_aide) and not has_refus
        if detail_lower == "mise en place d’aide à domicile" or detail_lower == "mise en place d'aide à domicile" or "mise en place de la pscg" in detail_lower or "plan d'aide" in detail_lower:
            return has_aide and not has_refus
        if "refus d’aide à domicile" in detail_lower or "refus d'aide à domicile" in detail_lower:
            return has_aide and has_refus
            
        return False

    def _match_single_criterion(self, c: str, data: dict) -> bool:
        comid_key = f"evaluation.comid.{c}"
        if data.get(comid_key) is True:
            # Si la confiance du critère COMID est nulle (exclu par post-traitement), on renvoie False
            confidences = data.get("evaluation.confiance.comid", {})
            if confidences.get(c, 100) == 0:
                return False
            return True
            
        conf_vars = data.get("evaluation.confiance.variables", {})
        
        # Nettoyage de la clé pour éviter les espaces et majuscules
        c_clean = c.lower().strip()
        
        # Mappings des nouveaux critères moteurs de tableau_oria.xlsx
        if c_clean in ["evaluation_globale", "reevaluation_globale"]:
            return data.get("demande.motif_principal") in ["evaluation_globale", "reevaluation_globale"] and conf_vars.get("motif", 100) > 0
            
        elif c_clean in ["hospitalisation.statut", "en_cours", "recente", "récente"]:
            return data.get("vulnerabilites.sante.hospitalisation.statut") in ["en_cours", "recente"] and conf_vars.get("hospitalisation", 100) > 0
            
        elif c_clean in ["aide_a_domicile"]:
            return data.get("demande.motif_principal") in ["maintien_a_domicile", "refus_aide_domicile"] and conf_vars.get("motif", 100) > 0
            
        elif c_clean in ["information_aides"]:
            return data.get("demande.motif_principal") == "information_aides" and conf_vars.get("motif", 100) > 0
            
        elif c_clean in ["refus_aide_domicile"]:
            return data.get("demande.motif_principal") == "refus_aide_domicile" and conf_vars.get("motif", 100) > 0
            
        elif c_clean in ["refus_de_soins"]:
            return data.get("demande.motif_principal") == "refus_de_soins" and conf_vars.get("motif", 100) > 0
            
        elif c_clean in ["precarite_financiere"]:
            return data.get("evaluation.comid.precarite_financiere") is True and data.get("evaluation.confiance.comid", {}).get("precarite_financiere", 100) > 0
            
        elif c_clean in ["secours_urgence"]:
            return data.get("demande.motif_principal") == "secours_urgence" and conf_vars.get("motif", 100) > 0
            
        elif c_clean in ["aide_alimentaire"]:
            return data.get("demande.motif_principal") == "aide_alimentaire" and conf_vars.get("motif", 100) > 0
            
        elif c_clean in ["diogene"]:
            return data.get("usager.cadre_de_vie.etat_logement") == "diogene" and conf_vars.get("etat_logement", 100) > 0
            
        elif c_clean in ["incurie"]:
            return data.get("usager.cadre_de_vie.etat_logement") == "incurie" and conf_vars.get("etat_logement", 100) > 0
            
        elif c_clean in ["violence_conjugale", "violence conjugale"]:
            return data.get("usager.situation_actuelle.suspicion_malveillance") in ["violences_physiques", "violences_psychologiques"] and conf_vars.get("malveillance", 100) > 0
            
        # Mappings pour les aides sociales, budget, logement et droits
        elif c_clean in ["foyer_logement", "foyer logement"]:
            return data.get("demande.motif_principal") == "recherche_logement" or data.get("evaluation.comid.logement_inadapte") is True
            
        elif c_clean in ["veille_sociale", "veille sociale", "suivi_regulier", "suivi regulier", "rupture_isolement", "rupture isolement"]:
            return data.get("evaluation.comid.isolement_social") is True or data.get("vulnerabilites.social.isolement_relationnel") in ["possible", "probable", "critique"]
            
        elif c_clean in ["precarite_sociale", "precarite sociale", "precarite_financiere", "precarite financiere", "evaluation_sociale", "evaluation sociale", "aide_financiere", "aide financiere", "aides_existantes", "aides existantes", "ressources", "aide_financiere_ponctuelle", "aide financiere ponctuelle", "factures", "paiement_factures", "paiement factures"]:
            precarite_sociale = data.get("vulnerabilites.social.precarite") in ["possible", "probable", "averee"]
            precarite_financiere = data.get("evaluation.comid.precarite_financiere") is True and data.get("evaluation.confiance.comid", {}).get("precarite_financiere", 100) > 0
            motif_precarite = data.get("demande.motif_principal") in ["dettes", "factures", "aide_alimentaire"]
            return precarite_sociale or precarite_financiere or motif_precarite

        # Mappings pour la santé et le suivi médical
        elif c_clean in ["acces_aux_soins", "acces aux soins"]:
            return data.get("vulnerabilites.sante.acces_soins") not in [None, "aucun", "non_mentionne"]
            
        elif c_clean in ["renoncement_aux_soins", "renoncement aux soins"]:
            return data.get("vulnerabilites.sante.suivi_medical.renoncement_soins") == "oui"
            
        elif c_clean in ["suivi_medical", "suivi médical"]:
            val = data.get("vulnerabilites.sante.suivi_medical.medecin_traitant")
            return val not in [None, "non_mentionne"] and conf_vars.get("medecin_traitant", 100) > 0
            
        elif c_clean in ["vad", "visite à domicile", "visite a domicile"]:
            return data.get("vulnerabilites.sante.suivi_medical.medecin_traitant") == "absent" and conf_vars.get("medecin_traitant", 100) > 0
            
        elif c_clean in ["paramedical"]:
            return data.get("vulnerabilites.sante.professionnels_domicile") == "oui" and conf_vars.get("professionnels_domicile", 100) > 0
            
        # Fallback pour les anciennes clés techniques
        if False:
            pass
        
        if c == "secours_urgence":
            return data.get("demande.motif_principal") == "secours_urgence" and conf_vars.get("motif", 100) > 0
        elif c == "violences_physiques":
            return data.get("usager.situation_actuelle.suspicion_malveillance") == "violences_physiques" and conf_vars.get("malveillance", 100) > 0
        elif c == "violences_psychologiques":
            return data.get("usager.situation_actuelle.suspicion_malveillance") == "violences_psychologiques" and conf_vars.get("malveillance", 100) > 0
        elif c == "violences_sexuelles":
            return data.get("usager.situation_actuelle.suspicion_malveillance") == "violences_sexuelles" and conf_vars.get("malveillance", 100) > 0
        elif c == "spoliation_financiere":
            return data.get("usager.situation_actuelle.suspicion_malveillance") == "spoliation_financiere" and conf_vars.get("malveillance", 100) > 0
        elif c == "negligence":
            return data.get("usager.situation_actuelle.suspicion_malveillance") == "negligence" and conf_vars.get("malveillance", 100) > 0
        elif c == "abus_de_confiance_ou_faiblesse":
            return data.get("usager.situation_actuelle.suspicion_malveillance") == "abus_de_confiance_ou_faiblesse" and conf_vars.get("malveillance", 100) > 0
        elif c == "privation_de_droits":
            return data.get("usager.situation_actuelle.suspicion_malveillance") == "privation_de_droits" and conf_vars.get("malveillance", 100) > 0
        elif c == "maltraitance_institutionnelle":
            return data.get("usager.situation_actuelle.suspicion_malveillance") == "maltraitance_institutionnelle" and conf_vars.get("malveillance", 100) > 0
        elif c == "securite_du_domicile":
            val = data.get("vulnerabilites.habitat.securite_du_domicile")
            malveillance_ok = data.get("usager.situation_actuelle.suspicion_malveillance") == "violences_physiques" and conf_vars.get("malveillance", 100) > 0
            return val in ["problematique", "critique", "danger_imminent"] or malveillance_ok
        elif c == "recherche_medecin":
            return data.get("demande.motif_principal") == "recherche_medecin" and conf_vars.get("motif", 100) > 0
        elif c == "medecin_traitant":
            val = data.get("vulnerabilites.sante.suivi_medical.medecin_traitant")
            return val not in [None, "non_mentionne"] and conf_vars.get("medecin_traitant", 100) > 0
        elif c == "absent":
            return data.get("vulnerabilites.sante.suivi_medical.medecin_traitant") == "absent" and conf_vars.get("medecin_traitant", 100) > 0
        elif c == "non_identifie_avec_certitude":
            # N'est vrai que si explicitement mentionné incertain/absent avec confiance
            return data.get("vulnerabilites.sante.suivi_medical.medecin_traitant") in ["incertain", "absent"] and conf_vars.get("medecin_traitant", 100) > 0
        elif c == "en_cours":
            return data.get("vulnerabilites.sante.hospitalisation.statut") == "en_cours" and conf_vars.get("hospitalisation", 100) > 0
        elif c == "recente":
            return data.get("vulnerabilites.sante.hospitalisation.statut") == "recente" and conf_vars.get("hospitalisation", 100) > 0
        elif c == "sortie_hospitalisation":
            return data.get("demande.motif_principal") == "sortie_hospitalisation" and conf_vars.get("motif", 100) > 0
        elif c == "maintien_a_domicile":
            return data.get("demande.motif_principal") == "maintien_a_domicile" and conf_vars.get("motif", 100) > 0
        elif c == "aide_a_domicile":
            motif_ok = data.get("demande.motif_principal") in ["maintien_a_domicile", "refus_aide_domicile"] and conf_vars.get("motif", 100) > 0
            return motif_ok
        elif c == "information_aides":
            return data.get("demande.motif_principal") == "information_aides" and conf_vars.get("motif", 100) > 0
        elif c == "refus_aide_domicile":
            return data.get("demande.motif_principal") == "refus_aide_domicile" and conf_vars.get("motif", 100) > 0
        elif c == "refus_de_soins":
            return data.get("demande.motif_principal") == "refus_de_soins" and conf_vars.get("motif", 100) > 0
        elif c == "opposition_soins":
            return data.get("evaluation.comid.opposition_soins") is True and data.get("evaluation.confiance.comid", {}).get("opposition_soins", 100) > 0
        elif c == "gir":
            gir_val = data.get("usager.situation_actuelle.GIR")
            try:
                if gir_val is not None and conf_vars.get("gir", 100) > 0:
                    gir_num = int(str(gir_val).replace("GIR", "").strip())
                    return 1 <= gir_num <= 4
            except:
                pass
            return False
        elif c == "apa":
            return data.get("usager.situation_actuelle.APA") == "oui" and conf_vars.get("apa", 100) > 0
        elif c == "pch":
            return data.get("usager.situation_actuelle.PCH") == "oui" and conf_vars.get("pch", 100) > 0
        elif c == "epuisement_aidant":
            return data.get("evaluation.comid.epuisement_aidant") is True and data.get("evaluation.confiance.comid", {}).get("epuisement_aidant", 100) > 0
        elif c == "troubles_cognitifs":
            return data.get("evaluation.comid.troubles_cognitifs") is True and data.get("evaluation.confiance.comid", {}).get("troubles_cognitifs", 100) > 0
        elif c == "trouble_cognitif_aigu":
            return data.get("evaluation.comid.trouble_cognitif_aigu") is True and data.get("evaluation.confiance.comid", {}).get("trouble_cognitif_aigu", 100) > 0
        elif c == "perte_autonomie_recente":
            return data.get("evaluation.comid.perte_autonomie_recente") is True and data.get("evaluation.confiance.comid", {}).get("perte_autonomie_recente", 100) > 0
        elif c == "degradation_recente":
            return data.get("evaluation.comid.degradation_recente") is True and data.get("evaluation.confiance.comid", {}).get("degradation_recente", 100) > 0
        elif c == "75":
            age = data.get("usager.identite.age_estime")
            try:
                return age is not None and float(age) >= 75 and conf_vars.get("age", 100) > 0
            except:
                return False
        elif c == "60":
            age = data.get("usager.identite.age_estime")
            try:
                return age is not None and float(age) <= 60 and conf_vars.get("age", 100) > 0
            except:
                return False
        elif c == "douleurs":
            return data.get("evaluation.comid.douleurs") is True and data.get("evaluation.confiance.comid", {}).get("douleurs", 100) > 0
        elif c == "multimorbidite":
            return data.get("evaluation.comid.multimorbidite") is True and data.get("evaluation.confiance.comid", {}).get("multimorbidite", 100) > 0
        elif c == "polymedication":
            return data.get("evaluation.comid.polymedication") is True and data.get("evaluation.confiance.comid", {}).get("polymedication", 100) > 0
        elif c == "imprevisibilite":
            return data.get("evaluation.comid.imprevisibilite") is True and data.get("evaluation.confiance.comid", {}).get("imprevisibilite", 100) > 0
        elif c == "precarite":
            precarite_val = data.get("vulnerabilites.social.precarite")
            return (precarite_val in ["possible", "probable", "averee"]) or (data.get("evaluation.comid.precarite_financiere") is True and data.get("evaluation.confiance.comid", {}).get("precarite_financiere", 100) > 0)
        elif c == "precarite_financiere":
            return data.get("evaluation.comid.precarite_financiere") is True and data.get("evaluation.confiance.comid", {}).get("precarite_financiere", 100) > 0
        elif c == "rsa":
            return data.get("demande.motif_principal") == "rsa" and conf_vars.get("motif", 100) > 0
        elif c == "aide_alimentaire":
            return data.get("demande.motif_principal") == "aide_alimentaire" and conf_vars.get("motif", 100) > 0
        elif c == "diogene":
            return data.get("usager.cadre_de_vie.etat_logement") == "diogene" and conf_vars.get("etat_logement", 100) > 0
        elif c == "incurie":
            return data.get("usager.cadre_de_vie.etat_logement") == "incurie" and conf_vars.get("etat_logement", 100) > 0
        elif c == "complexe":
            return data.get("complexite.niveau") == "complexe"
        elif c == "psychiatrie":
            return data.get("evaluation.comid.psychiatrie") is True and data.get("evaluation.confiance.comid", {}).get("psychiatrie", 100) > 0
        elif c == "addiction":
            return data.get("evaluation.comid.addiction") is True and data.get("evaluation.confiance.comid", {}).get("addiction", 100) > 0
        elif c == "logement":
            insalubre_ok = data.get("usager.cadre_de_vie.etat_logement") in ["insalubre", "diogene", "incurie"] and conf_vars.get("etat_logement", 100) > 0
            logement_inadapte_ok = data.get("evaluation.comid.logement_inadapte") is True and data.get("evaluation.confiance.comid", {}).get("logement_inadapte", 100) > 0
            return insalubre_ok or logement_inadapte_ok
            
        return False

    def _get_structure_label(self, struct_type: str) -> str:
        labels = {
            "POLICE": "Police / Gendarmerie (Urgence Vitale & Intervention)",
            "CEV": "CEV - Cellule Écoute et Vigilance (Violences & Danger)",
            "SERVICE_SOCIAL_HOPITAL": "Service Social de l'Hôpital",
            "CPTS": "CPTS - Communauté Professionnelle Territoriale de Santé",
            "CLIC": "CLIC - Centre Local d'Information et de Coordination (Sénior)",
            "CRT": "CRT - Centre de Ressources Territorial (Accompagnement Renforcé)",
            "DAC": "DAC - Dispositif d'Appui à la Coordination",
            "UTS": "UTS - Unité Territoriale Sociale",
            "CCAS": "CCAS - Secours d'Urgence (Alimentaire & Factures)",
            "COMPAGNONS_BATISSEURS": "Les Compagnons Bâtisseurs (Rénovation & Diogène)",
            "PSCG_SS_APA": "PSCG SS APA - Pôle Social Autonomie",
            "PRADO": "PRADO - Programme d'Accompagnement au Retour à Domicile",
            "MISAS": "MISAS - Mission d'Appui en Santé Mentale",
            "fil d'argent": "Fil d'Argent - Relais et écoute des aidants",
            "CONSULTATION MÉMOIRE": "Consultation Mémoire - Évaluation cognitive"
        }
        return labels.get(struct_type, struct_type)

    def _extract_verbatim(self, detail: str, criteria: str, original_text: str) -> str:
        if not original_text:
            return ""
        import re
        sentences = [s.strip() for s in re.split(r'[.!?\n]+', original_text) if s.strip()]
        if not sentences:
            return ""

        # 1. Découpage en sub-clauses (propositions) sur les connecteurs logiques majeurs ("parce que", "car", "afin de")
        clauses = []
        for sentence in sentences:
            parts = re.split(r'\b(parce que|parce qu\'|car)\b', sentence, flags=re.IGNORECASE)
            current = ""
            for p in parts:
                if p.lower() in ["parce que", "parce qu'", "car"]:
                    if current.strip():
                        clauses.append(current.strip())
                    current = ""
                else:
                    current += " " + p
            if current.strip():
                clauses.append(current.strip())

        kws = []
        if criteria and str(criteria) != "nan":
            raw_kws = re.split(r'[,;/]+', str(criteria))
            for k in raw_kws:
                cleaned = k.strip().lower()
                if len(cleaned) >= 3 and cleaned not in ["oui", "non", "nan", "true", "false"]:
                    kws.append(cleaned)
                    
        if detail:
            words = [w.lower() for w in detail.split() if len(w) >= 4 and w.lower() not in ["besoin", "mise", "place", "dans", "pour", "avec", "cette", "adaptation", "choix", "d'un", "d'une", "perte", "rapide"]]
            kws.extend(words)

        # Target-specific keyword focus & tuning for Aidants vs Domicile
        detail_lower = (detail + " " + str(criteria)).lower()
        if any(w in detail_lower for w in ["aidant", "aidants", "répit", "repit", "fil d'argent"]):
            kws = ["surmené", "surmenée", "surmenés", "surmenages", "surmenage", "épuisé", "épuisée", "épuisement", "fatigué", "aidant", "aidante", "aidants", "répit", "repit", "soulager", "souffle"]
        elif any(w in detail_lower for w in ["domicile", "saad", "ssiad", "ménage", "repas", "prestataire"]):
            kws = ["aides à domicile", "aide à domicile", "aides a domicile", "aide a domicile", "auxiliaire de vie", "saad", "ssiad", "prestataire", "domicile"]
        elif any(w in detail_lower for w in ["violence", "3919", "maltraitance", "frappe", "bleu", "danger"]):
            kws = ["violence", "violences", "frappe", "frappé", "bleu", "bleus", "maltraitance", "peur", "danger", "menace", "insulte"]

        # Évaluation d'abord sur les clauses ciblées
        best_clause = ""
        best_score = 0

        for clause in clauses:
            c_lower = clause.lower()
            score = 0
            for kw in kws:
                if kw in c_lower:
                    score += len(kw) * 2
            if score > best_score:
                best_score = score
                best_clause = clause

        if best_score >= 4:
            cleaned = best_clause.strip()
            # Nettoyage pour les aides à domicile si la clause se termine par "pour nous soulager"
            if any(w in detail_lower for w in ["domicile", "saad", "ssiad", "prestataire"]):
                cleaned = re.sub(r'\s+pour nous soulager.*$', '', cleaned, flags=re.IGNORECASE)
            return cleaned.strip()

        # Fallback au niveau de la phrase complète si la clause n'est pas suffisante
        best_sentence = ""
        best_score = 0
        for sentence in sentences:
            s_lower = sentence.lower()
            score = 0
            for kw in kws:
                if kw in s_lower:
                    score += len(kw)
            if score > best_score:
                best_score = score
                best_sentence = sentence

        if best_score >= 4:
            return best_sentence.strip()

        return ""
