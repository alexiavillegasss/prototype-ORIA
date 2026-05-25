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

    def get_clarification_questions(self, extracted_data: dict, eligible_structures: list, text: str = None) -> list:
        """
        Détermine si des informations critiques sont manquantes dans les données extraites
        ou dans le texte original, et génère des questions ciblées.
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

        for field_path, field_info in self.critical_fields.items():
            value = extracted_data.get(field_path)
            
            # Normalisation
            if isinstance(value, str):
                value = value.lower().strip()
                
            # Évaluation si la valeur est inconnue dans le dictionnaire
            is_missing = value in field_info["trigger_values"]
            
            # Validation par mot-clé dans le texte original (si disponible) :
            # Si le sujet n'est pas du tout évoqué dans le texte, on considère l'info manquante.
            if text and not is_missing:
                text_lower = text.lower()
                field_keywords = keywords.get(field_path, [])
                if not any(kw in text_lower for kw in field_keywords):
                    is_missing = True
                    
            if is_missing:
                questions.append({
                    "champ": field_path,
                    "libelle": field_info["label"],
                    "question": field_info["question"],
                    "impact": field_info["impact"],
                    "valeur_actuelle": "Non renseignée / Inconnue"
                })
                
        return questions
