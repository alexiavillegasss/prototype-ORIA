import json
import os
from infrastructure.llm_client import OllamaClient

class SignalExtractor:
    def __init__(self, schema_path: str, comid_path: str, model="llama3"):
        self.client = OllamaClient(model=model)
        self.schema_path = schema_path
        self.comid_path = comid_path
        self._comid_items = self._load_comid_items()

    def _load_comid_items(self):
        with open(self.comid_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data.get("items", [])

    async def extract(self, text: str):
        # On regroupe les critères par domaine pour aider l'IA à se structurer
        prompt = f"""
### EXPERT ORIA - ÉVALUATION DE COMPLEXITÉ
Analyse la situation suivante et évalue les critères COMID.

SITUATION : "{text}"

### ÉTAPE 1 : SYNTHÈSE CLINIQUE
Identifie les problèmes de santé (physique/mental), l'environnement social et les risques.

### ÉTAPE 2 : ÉVALUATION DES CRITÈRES (OUI/NON)
Utilise ce lexique pour tes déductions :
- **Troubles cognitifs** : confusion, oublis, désorientation, Alzheimer, démence, radotage, déambulation.
- **Agressivité** : colère, cris, insultes, coups, agitation, hostilité, mutisme.
- **Résistance aux soins** : refus d'entrée, opposition, "ne veut rien faire", négociation, rejette l'aide.
- **Isolement** : vit seul, pas de famille, voisins inquiets, pas de visites.
- **Instabilité/Danger** : chute, déambulation nocturne, situation dangereuse, "ça ne peut plus durer", risque.
- **Épuisement aidant** : fatigue, inquiétude, "à bout", burnout de la famille.

Évalue chaque critère ci-dessous. 
ATTENTION : Si un synonyme est présent, coche OUI.

### ÉTAPE 3 : FORMAT JSON (STRICT)
{{
  "age": 88,
  "ville": "Hyères",
  "apa": "oui",
  "comid": {{
    "troubles_cognitifs": true,
    "agressivite_ou_mutisme": true,
    "resistance_ou_opposition_aux_soins": true,
    "fonctions_mentales_variant_au_cours_de_la_journee": true,
    "changement_global_du_degre_d_independance_dans_le_dernier_mois": true,
    "isolement_social": true,
    "non_previsibilite_de_l_etat_de_sante": true,
    ... (tous les autres critères ici avec true/false)
  }},
  "raisonnement_expert": "Texte court expliquant la complexité"
}}

LISTE DES CODES À UTILISER :
{", ".join([item['code'] for item in self._comid_items])}

REPONDS UNIQUEMENT PAR LE JSON :
"""
        raw_result = await self.client.generate_json(prompt)
        
        print("\n--- DEBUG : ANALYSE EXPERTE ---")
        print(raw_result.get("raisonnement_expert", "Analyse manquante"))
        print("--- FIN DEBUG ---\n")
        
        return self._map_to_schema(raw_result)

    def _map_to_schema(self, raw_data: dict):
        mapped = {
            "usager.identite.age_estime": raw_data.get("age"),
            "usager.localisation.commune_residence": raw_data.get("ville"),
            "usager.situation_actuelle.APA": str(raw_data.get("apa", "non")).lower(),
            "demande.motif_principal": raw_data.get("motif", "maintien_a_domicile"),
        }

        # Mapping flexible (cherche dans "comid" ou à la racine)
        comid_data = raw_data.get("comid", raw_data)
        for item in self._comid_items:
            code = item["code"]
            val = comid_data.get(code)
            
            is_positive = False
            if isinstance(val, bool):
                is_positive = val
            elif isinstance(val, str):
                is_positive = val.lower() in ["oui", "yes", "true", "o", "1"]
            
            mapped[f"evaluation.comid.{code}"] = is_positive

        # Cas particulier pour l'isolement (vulnerabilites.social.isolement_relationnel)
        if mapped.get("evaluation.comid.isolement_social") or raw_data.get("seule") == "oui":
            mapped["vulnerabilites.social.isolement_relationnel"] = "critique"
        else:
            mapped["vulnerabilites.social.isolement_relationnel"] = None

        return mapped
