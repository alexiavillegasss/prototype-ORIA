import json
import os
from infrastructure.llm_client import OllamaClient

class SignalExtractor:
    def __init__(self, schema_path: str, comid_path: str, model="llama3", base_url="http://localhost:11434"):
        self.client = OllamaClient(model=model, base_url=base_url)
        self.schema_path = schema_path
        self.comid_path = comid_path
        self._comid_items = self._load_comid_items()

    def _load_comid_items(self):
        with open(self.comid_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data.get("items", [])

    async def extract(self, text: str):
        # Construction dynamique de la liste des critères avec leurs exemples, l'IA prefere lire une liste donc on la transforme sous cette forme, on l'utilisera ligne 45.
        comid_reference = ""
        for item in self._comid_items:
            exemples = f" (Exemples: {', '.join(item['exemples'])})" if 'exemples' in item else ""
            comid_reference += f"- {item['label']} (Code: `{item['code']}`){exemples}\n"

        prompt = f"""
### EXPERT ORIA - ÉVALUATION CLINIQUE ET SOCIALE
Analyse la situation suivante pour structurer un dossier d'orientation.

SITUATION : "{text}"

### ÉTAPE 1 : EXTRACTION DES DONNÉES DE BASE
- Âge de la personne (ex: 82)
- Ville de résidence (ex: Toulon)
- "apa": Statut de l'APA (choisir parmi: "oui", "non", "en_cours", "inconnu")
- "pch": Statut de la PCH (choisir parmi: "oui", "non", "en_cours", "inconnu")
- "medecin_traitant": Statut du médecin traitant (choisir parmi: "identifie", "absent", "incertain")
- "malveillance": Suspicion de malveillance (IMPORTANT: choisir "spoliation_financiere" si argent extorqué ou demandé avec insistance, "violences_physiques" si coups/marques, "negligence" si manque de nourriture/hygiène, "aucune" sinon)
- "urgence": Urgence perçue (choisir parmi: "faible", "modere", "eleve", "critique")
- "hospitalisation": Statut hospitalisation (IMPORTANT: choisir "en_cours" si la personne est à l'hôpital, "recente" si elle vient de sortir, sinon "aucun")
- "motif": Motif principal de la demande (choisir parmi: "recherche_medecin", "maintien_a_domicile", "sortie_hospitalisation", "aide_alimentaire", "secours_urgence", "information_aides", "maltraitance")
- "gir": GIR estimé de la personne si mentionné (choisir parmi: 1, 2, 3, 4, 5, 6, ou null si non précisé)
- "professionnels_domicile": Présence de professionnels au domicile comme infirmiers ou aides à domicile (choisir parmi: "oui", "non", "inconnu")
- "aidant_regulier": Présence d'un proche aidant régulier (choisir parmi: "oui", "non", "inconnu")


        
### ÉTAPE 2 : ÉVALUATION DES CRITÈRES COMID (OUI/NON)
Utilise ce référentiel :
{comid_reference}

### ÉTAPE 3 : FORMAT JSON (STRICT)
{{
  "age": 82,
  "ville": "Toulon",
  "apa": "non",
  "gir": 4,
  "professionnels_domicile": "oui",
  "aidant_regulier": "non",
  "medecin_traitant": "absent",
  "malveillance": "aucune",
  "urgence": "modere",
  "motif": "recherche_medecin",
  "comid": {{
    "multimorbidite": true,
    ...
  }},
  "raisonnement_expert": "Résumé synthétique"
}}

REPONDS UNIQUEMENT PAR LE JSON :
"""
        # raw = brut, il s'agit de la réponse brute telle quelle sort de l'IA, on renomme les clefs pour que les noms correspondent au schéma. raw_result = raw_data -> ce sont les mêmes données (résultats de l'IA qui sont les données entrantes après dans la fonction map_to_schema)
        raw_result = await self.client.generate_json(prompt)
        
        print("\n--- DEBUG : ANALYSE EXPERTE ---")
        print(raw_result.get("raisonnement_expert", "Analyse manquante"))
        print(f"Ville extraite : {raw_result.get('ville')}")
        print(f"Médecin : {raw_result.get('medecin_traitant')}")
        print(f"Malveillance : {raw_result.get('malveillance')}")
        print(f"Hospitalisation : {raw_result.get('hospitalisation')}")
        print("--- FIN DEBUG ---\n")
        
        return self._map_to_schema(raw_result)

    def _map_to_schema(self, raw_data: dict):
        mapped = {
            "usager.identite.age_estime": raw_data.get("age"),
            "usager.localisation.commune_residence": raw_data.get("ville"),
            "usager.situation_actuelle.APA": str(raw_data.get("apa", "non")).lower(),
            "usager.situation_actuelle.PCH": str(raw_data.get("pch", "non")).lower(),
            "usager.situation_actuelle.GIR": raw_data.get("gir"),
            "vulnerabilites.sante.suivi_medical.medecin_traitant": raw_data.get("medecin_traitant", "incertain"),
            "usager.situation_actuelle.suspicion_malveillance": raw_data.get("malveillance", "aucune"),
            "adresseur.degre_urgence_percu": raw_data.get("urgence", "faible"),
            "vulnerabilites.sante.hospitalisation.statut": raw_data.get("hospitalisation", "aucun"),
            "demande.motif_principal": raw_data.get("motif", "maintien_a_domicile"),
            "vulnerabilites.sante.professionnels_domicile": str(raw_data.get("professionnels_domicile", "inconnu")).lower(),
            "usager.cadre_de_vie.aidant_regulier": str(raw_data.get("aidant_regulier", "inconnu")).lower(),
        }

        # Mapping flexible (cherche dans "comid" ou à la racine). On formate le résultat de l'IA : true ou false dans le dictionnaire final
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
