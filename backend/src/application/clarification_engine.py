class ClarificationEngine:
    def __init__(self):
        # Liste des variables critiques dont l'absence ou l'inconnue bloque des orientations
        self.critical_fields = {
            "usager.situation_actuelle.APA": {
                "label": "APA (Allocation Personnalisée d'Autonomie)",
                "question": "Le patient bénéficie-t-il déjà de l'APA (oui/non/en cours) ?",
                "impact": "Indispensable pour orienter vers le Pôle Solidarité APA (si oui) ou vers le CLIC / CCAS (si non).",
                "trigger_values": ["inconnu", None]
            },
            "usager.situation_actuelle.GIR": {
                "label": "GIR (Niveau de dépendance)",
                "question": "Quel est le GIR (Groupe Iso-Ressources) estimé ou officiel du patient (1 à 6) ?",
                "impact": "Un GIR entre 1 et 4 permet de valider l'éligibilité au CRT (Accompagnement Renforcé) ou au DAC pour dépendance lourde.",
                "trigger_values": [None, "inconnu"]
            },
            "usager.identite.age_estime": {
                "label": "Âge du patient",
                "question": "Quel est l'âge exact ou estimé du patient ?",
                "impact": "Plusieurs structures (CRT, CLIC, CPTS) ont des conditions d'éligibilité liées à l'âge (ex: 60 ans et plus).",
                "trigger_values": [None, "inconnu"]
            },
            "usager.cadre_de_vie.aidant_regulier": {
                "label": "Présence d'un proche aidant",
                "question": "Le patient dispose-t-il d'un aidant régulier à proximité (famille, ami, voisin) ?",
                "impact": "L'absence d'aidant régulier pour un patient en perte d'autonomie importante (GIR 1-3) déclenche l'éligibilité prioritaire au DAC.",
                "trigger_values": ["inconnu", None]
            },
            "vulnerabilites.sante.suivi_medical.medecin_traitant": {
                "label": "Médecin traitant",
                "question": "Le patient a-t-il un médecin traitant identifié ?",
                "impact": "L'absence de médecin traitant est nécessaire pour déclencher un accompagnement par la CPTS (accès aux soins).",
                "trigger_values": ["inconnu", "incertain", None]
            }
        }

    def get_clarification_questions(self, extracted_data: dict, eligible_structures: list, text: str = None, scoring_engine = None, orientation_engine = None) -> list:
        """
        Détermine si des informations critiques sont manquantes dans les données extraites
        ou dans le texte original, et génère des questions ciblées UNIQUEMENT si y répondre
        a un impact réel sur la décision d'orientation finale.
        """
        questions = []
        
        # Mots-clés associés pour valider que le sujet a bien été abordé dans le récit
        keywords = {
            "usager.situation_actuelle.APA": ["apa", "allocation personnalisée d'autonomie", "allocation personnalisee d'autonomie"],
            "usager.situation_actuelle.GIR": ["gir", "groupe iso-ressources", "groupe iso ressources"],
            "usager.identite.age_estime": ["ans", "âge", "age"],
            "usager.cadre_de_vie.aidant_regulier": ["aidant", "famille", "proche", "fils", "fille", "épou", "epou", "mari", "voisin"],
            "vulnerabilites.sante.suivi_medical.medecin_traitant": ["médecin", "medecin", "docteur", "généraliste", "generaliste"]
        }

        # Valeurs alternatives de test pour vérifier l'impact sur l'orientation
        test_values = {
            "usager.situation_actuelle.APA": ["oui", "non"],
            "usager.situation_actuelle.GIR": [2, 6],
            "usager.identite.age_estime": [80, 45],
            "usager.cadre_de_vie.aidant_regulier": ["oui", "non"],
            "vulnerabilites.sante.suivi_medical.medecin_traitant": ["identifie", "absent"]
        }

        # On extrait la situation initiale des types recommandés et de leurs priorités
        initial_types = {s["structure_type"] for s in eligible_structures}
        initial_priorities = {s["structure_type"]: s["priorite"] for s in eligible_structures}

        for field_path, field_info in self.critical_fields.items():
            # Filtre intelligent pour éviter les questions d'autonomie hors-sujet
            if field_path == "usager.situation_actuelle.GIR" and scoring_engine:
                motif = extracted_data.get("demande.motif_principal")
                comid_results = scoring_engine.calculate_comid_score(extracted_data)
                
                has_cognitive = extracted_data.get("evaluation.comid.troubles_cognitifs") is True or extracted_data.get("evaluation.comid.trouble_cognitif_aigu") is True
                has_autonomie_loss = extracted_data.get("evaluation.comid.perte_autonomie_recente") is True
                
                is_purely_social = motif in ["aide_alimentaire", "secours_urgence", "information_aides"]
                
                if is_purely_social and not has_cognitive and not has_autonomie_loss and comid_results.get("score_total", 0) <= 3:
                    continue # On ignore la question du GIR pour les dossiers purement sociaux
            
            value = extracted_data.get(field_path)
            
            # Normalisation
            if isinstance(value, str):
                value = value.lower().strip()
                
            # Évaluation si la valeur est inconnue dans le dictionnaire
            is_missing = value in field_info["trigger_values"]
            
            # Validation par mot-clé dans le texte original (si disponible) :
            if text and not is_missing:
                text_lower = text.lower()
                field_keywords = keywords.get(field_path, [])
                if not any(kw in text_lower for kw in field_keywords):
                    is_missing = True
                    
            if is_missing:
                # VÉRIFICATION DYNAMIQUE DE L'IMPACT :
                # Si les moteurs sont passés en paramètre, on simule des réponses pour voir si l'orientation change
                has_impact = True
                if scoring_engine and orientation_engine:
                    has_impact = False
                    for test_val in test_values.get(field_path, []):
                        # On simule un changement de valeur
                        test_data = {**extracted_data}
                        test_data[field_path] = test_val
                        
                        # Recalcul des orientations
                        test_comid = scoring_engine.calculate_comid_score(test_data)
                        test_orientations = orientation_engine.evaluate_orientation(test_data, test_comid)
                        
                        # Extraction des résultats simulés
                        test_types = {s["structure_type"] for s in test_orientations}
                        test_priorities = {s["structure_type"]: s["priorite"] for s in test_orientations}
                        
                        # Si l'orientation simulée est différente de l'initiale, il y a un impact réel !
                        if initial_types != test_types or initial_priorities != test_priorities:
                            has_impact = True
                            break # Inutile de tester d'autres valeurs, l'impact est prouvé
                
                if has_impact:
                    questions.append({
                        "champ": field_path,
                        "libelle": field_info["label"],
                        "question": field_info["question"],
                        "impact": field_info["impact"],
                        "valeur_actuelle": "Non renseignée / Inconnue"
                    })
                
        return questions
