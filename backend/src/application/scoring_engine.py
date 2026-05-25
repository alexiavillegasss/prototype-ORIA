import json
import os

class ScoringEngine:
    def __init__(self, comid_rules_path: str):
        self.rules_path = comid_rules_path
        self.rules = self._load_rules()

    def _load_rules(self):
        with open(self.rules_path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def calculate_comid_score(self, extracted_data: dict):
        """
        Calcule le score COMID à partir des données extraites par l'IA.
        Chaque champ 'evaluation.comid.*' valant True ajoute 1 point.
        """
        score = 0
        positive_items = []

        # On parcourt les données extraites
        for key, value in extracted_data.items():
            if key.startswith("evaluation.comid.") and value is True:
                score += 1
                # On récupère juste le nom du critère pour la traçabilité
                item_code = key.replace("evaluation.comid.", "")
                positive_items.append(item_code)

        # Interprétation du niveau
        interpretation = self._get_interpretation(score)

        return {
            "score_total": score,
            "niveau": interpretation["niveau"],
            "label": interpretation["label"],
            "items_detectes": positive_items
        }

    def _get_interpretation(self, score: int):
        # On récupère les règles définies dans COMID.json
        levels = self.rules.get("interpretation_score", {}).get("regles_niveau_complexite", [])
        
        # Par défaut
        result = {"niveau": "indetermine", "label": "Score inconnu"}

        for level in levels:
            # On parse la condition simple (ex: "score_total >= 10")
            # Pour faire simple dans le prototype, on code les seuils en dur 
            # ou on pourrait utiliser eval() mais c'est moins safe.
            if "score_total >= 10" in level["condition"] and score >= 10:
                return level
            elif "score_total >= 6" in level["condition"] and 6 <= score <= 9:
                return level
            elif "score_total >= 0" in level["condition"] and 0 <= score <= 5:
                return level
        
        return result
