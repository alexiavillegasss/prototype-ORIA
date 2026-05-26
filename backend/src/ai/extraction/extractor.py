import json
import os
from infrastructure.llm_client import OllamaClient

class SignalExtractor:
    last_extracted_data = None
    last_text = None

    def __init__(self, schema_path: str, comid_path: str, model="llama3.2", base_url="http://localhost:11434", temperature=0.1):
        self.client = OllamaClient(model=model, base_url=base_url, temperature=temperature)
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

### INSTRUCTIONS DE RIGUEUR CLINIQUE :
1. Extrais UNIQUEMENT les données présentes ou directement déductibles du texte de la SITUATION ci-dessus.
2. Si une variable administrative n'est PAS du tout évoquée dans le texte, réponds "inconnu" (pour les textes) ou null (pour les nombres). 
3. IMPORTANT : Ne copie PAS les valeurs de l'exemple fictif ci-dessous (Marseille, Albert, 75, etc.). Remplace-les obligatoirement par les données réelles de la SITUATION (ex: Antoinette, 92, La Garde, APA oui, GIR 2).

### DISTINCTION CRITIQUE PRÉCARITÉ VS MALVEILLANCE :
- "precarite_financiere" (critère COMID) = le patient a des difficultés économiques (ex: mal à payer son loyer, ses factures, pauvreté).
- "malveillance" / "spoliation_financiere" = un tiers (proche, abuseur, voleur) extorque ou vole de l'argent au patient.
- REGLE ABSOLUE : Si le patient a simplement du mal à payer son loyer ou ses factures sans qu'un tiers ne l'ait volé ou exploité, tu dois mettre la malveillance à "aucune" (et la précarité financière à true). Il est STRICTEMENT INTERDIT de choisir "spoliation_financiere" pour désigner des difficultés financières ordinaires ou des dettes.

### ÉTAPE 1 : EXTRACTION DES DONNÉES DE BASE
- Âge de la personne (chiffre entier, ou null si non mentionné)
- Ville de résidence (ex: "La Garde", ou null si non mentionné)
- "apa": Statut de l'APA (choisir parmi: "oui", "non", "en_cours", "inconnu")
- "pch": Statut de la PCH (choisir parmi: "oui", "non", "en_cours", "inconnu")
- "medecin_traitant": Statut du médecin traitant (choisir parmi: "identifie", "absent", "incertain")
- "malveillance": Suspicion de malveillance (choisir "spoliation_financiere" si argent extorqué, "violences_physiques" si coups, "negligence" si délaissement ou privations VOLONTAIRES et actives de l'entourage (ex: abandon, privation d'hygiène ou de repas), ou "aucune" sinon. Note critique 1 : Ne choisis JAMAIS 'spoliation_financiere' si le patient est simplement pauvre ou à découvert sans qu'un tiers lui ait volé de l'argent. Note critique 2 : Ne choisis JAMAIS 'negligence' si la personne fait face à un manque de médecin traitant, une désertification médicale, ou une rupture accidentelle de soins — ce sont des problèmes d'accès aux soins, pas de la maltraitance. Seul un abandon intentionnel ou une privation volontaire par l'entourage justifie 'negligence').
- "urgence": Urgence perçue (choisir parmi: "faible", "modere", "eleve", "critique")
- "hospitalisation": Statut hospitalisation (choisir "en_cours" si la personne est actuellement admise et hospitalisée dans un établissement, "recente" si elle a été hospitalisée et est sortie depuis moins de 10 jours, "aucun" sinon. Note critique : Ne choisis JAMAIS "en_cours" ou "recente" si la personne cherche simplement un médecin, manque de médicaments, ou a une rupture de suivi médical — ce n'est pas une hospitalisation).
- "motif": Motif principal de la demande (choisir parmi: "recherche_medecin", "maintien_a_domicile", "sortie_hospitalisation", "aide_alimentaire", "secours_urgence", "information_aides", "maltraitance", "refus_de_soins", "refus_aide_domicile")
- "gir": GIR officiel ou estimé si mentionné (choisir parmi: 1, 2, 3, 4, 5, 6, ou null si non précisé)
- "professionnels_domicile": Présence de professionnels au domicile (choisir parmi: "oui", "non", "inconnu")
- "aidant_regulier": Présence d'un proche aidant régulier (choisir parmi: "oui", "non", "inconnu")

        
### ÉTAPE 2 : ÉVALUATION DES CRITÈRES COMID (OUI/NON)
Utilise ce référentiel pour évaluer les 30 critères COMID sous forme de booléens (true / false) :
{comid_reference}
(Note clinique critique : Le critère 'opposition_soins' doit être évalué à true UNIQUEMENT si la personne refuse ou s'oppose activement à une aide ou un soin qui lui est proposé (ex: refuse que l'auxiliaire de vie entre, dit 'je n'ai besoin de rien', refuse les médicaments). Ce critère doit rester false si la personne CHERCHE activement de l'aide, cherche un médecin, ou fait des démarches pour obtenir des soins — même si elle n'y parvient pas encore.)

### ÉTAPE 3 : FORMAT JSON DE SORTIE (STRICT)
Voici le format de réponse attendu. Les valeurs fournies ici sont celles d'un EXEMPLE FICTIF (M. Albert, 75 ans, Marseille, qui n'a pas d'aidant). Tu dois l'adapter avec les données de ta SITUATION :
{{
  "age": 75,
  "ville": "Marseille",
  "apa": "non",
  "pch": "non",
  "gir": 5,
  "professionnels_domicile": "inconnu",
  "aidant_regulier": "non",
  "medecin_traitant": "identifie",
  "malveillance": "aucune",
  "urgence": "faible",
  "hospitalisation": "aucun",
  "motif": "maintien_a_domicile",
  "comid": {{
    "multimorbidite": false
  }},
  "raisonnement_expert": "Résumé court"
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
        
        result = self._map_to_schema(raw_result)
        SignalExtractor.last_extracted_data = result
        SignalExtractor.last_text = text
        return result

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
