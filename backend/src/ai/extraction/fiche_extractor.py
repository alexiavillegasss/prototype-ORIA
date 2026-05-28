import json
import datetime
from infrastructure.llm_client import OllamaClient

class FicheDACExtractor:
    def __init__(self, model="llama3.2", base_url="http://localhost:11434"):
        self.client = OllamaClient(model=model, base_url=base_url)

    async def extract_for_dac(self, raw_text: str):
        prompt = f"""
### EXPERT ORIA - EXTRACTION FICHE DAC
Analyse le récit suivant pour remplir précisément une Fiche d'Orientation DAC.

### INSTRUCTIONS DE REMPLISSAGE
- Tous les champs sont obligatoires dans le JSON.
- Si une information n'est pas mentionnée dans le texte, laisse-la STRICTEMENT vide (`""` pour une chaîne, `false` pour un booléen).
- RÈGLE POUR "INCONNU" : Mets la valeur exacte `"INCONNU"` UNIQUEMENT SI l'utilisateur précise expressément avec des mots qu'il ne possède pas l'information (ex: "je n'ai pas son adresse", "c'est inconnu", "je ne sais pas"). Ne déduis pas "INCONNU" par toi-même juste parce que l'info manque. S'il ne dit rien, mets `""`.
- **NE DÉDUIS RIEN** : N'invente aucune information. Si ce n'est pas écrit noir sur blanc, laisse vide `""`.
- **RÈGLES STRICTES** : 
  - Dans `nom_usage`, mets le nom de famille. Ne mets JAMAIS les titres (Monsieur, Madame, Veuve, etc). Si tu vois le prénom dedans, retire-le.
  - Dans `prenoms`, mets UNIQUEMENT le prénom. Si aucun prénom n'est donné, laisse vide `""`. N'utilise jamais les titres.
  - Si un âge est donné (ex: 85 ans), écris simplement cet âge (ex: "85 ans") dans `date_naissance`. Si ni date ni âge ne sont donnés, laisse strictement vide `""`.
  - Ne confonds pas la ville de résidence avec la ville de naissance : si la personne "habite à Toulon", cela va dans `adresse_complete`. `commune_naissance` reste vide `""`.
  - Pour `vit_seul`, mets "Non" si le texte indique clairement que la personne est accompagnée (ex: "habite avec moi", "vit avec son fils").
  - Pour `apa`, `gir`, `ald`, `mdph` : ne les déduis JAMAIS de l'âge ou de la situation. S'ils ne sont pas mentionnés, laisse vide `""` ou `null`.
  - Pour `hospit_recente` : mets `true` SI ET SEULEMENT SI le mot "hôpital", "hospitalisation", ou "urgences" est dans le texte. Sinon, mets `false` et laisse `hospit_date` et `hospit_motif` vides `""`. 
  - Si une hospitalisation est mentionnée mais que la date est floue (ex: "dimanche", "il y a 3 semaines"), écris cette phrase exacte dans `hospit_date`. Ne laisse pas vide si l'utilisateur a donné un repère temporel.

RÉCIT : "{raw_text}"

### DONNÉES À EXTRAIRE :
Identité :
- nom_usage (chaîne)
- nom_naissance (chaîne)
- prenoms (chaîne)
- sexe (chaîne: "F", "M" ou "")
- date_naissance (chaîne JJ/MM/AAAA)
- commune_naissance (chaîne)
- adresse_complete (chaîne)
- telephone (chaîne)
- vit_seul (chaîne: "Oui", "Non", "INCONNU", ou "")
- lieu_actuel (chaîne: "domicile", "etablissement", ou autre texte)

Situation :
- apa (chaîne: "Oui", "Non", "INCONNU", ou "")
- gir (chaîne ou null)
- mdph (booléen ou null)
- ald (booléen ou null)
- description_situation (chaîne, résumé très clair des faits et de la situation)
- actions_entreprises (chaîne, qu'est-ce qui a déjà été fait ?)
- attentes_dac (chaîne, qu'attend-on du DAC ?)

Alertes (mettre `true` si le problème est mentionné, sinon `false`) :
- pb_actes_essentiels (se nourrir, se vêtir, se laver)
- pb_activites_domestiques (courses, ménage, repas)
- pathologies_chroniques
- pb_memoire_decision
- troubles_comportement
- conduites_addictives
- medocs_plus_de_5
- troubles_psy
- denutrition_perte_poids
- risque_chute
- hospit_recente
- hospit_date (chaîne: format JJ/MM/AAAA ou date explicite)
- hospit_motif (chaîne: motif de l'hospitalisation)
- isolement_social
- epuisement_aidant
- diff_financieres
- logement_inadapte
- incurie_insalubrite

### PROFESSIONNELS ET INTERVENANTS (CERCLE DE SOINS / AIDES)
Extraire TOUS les intervenants et professionnels EXPLICITEMENT mentionnés dans le récit (ex: médecin, infirmier, aide à domicile, ADMR, kiné, etc.) sous forme d'une liste `cercle_de_soins`. Il est TRÈS IMPORTANT d'inclure les aides à domicile. N'INVENTE PAS de professionnel.
Chaque élément doit être un objet avec :
- type (chaîne STRICTE parmi : "medecin_traitant", "specialiste", "infirmier", "ssiad_had", "saad" (pour aide à domicile, ADMR), "palliatifs", "pharmacien", "kine", "repas", "telealarme", "social", "autre")
- nom (chaîne, sans AUCUN titre. Retire "docteur", "Dr", "le docteur")
- tel (chaîne)
- email (chaîne, laisse STRICTEMENT vide `""` si non précisé. N'invente JAMAIS d'exemple)

### FORMAT JSON (STRICT)
Réponds UNIQUEMENT par ce JSON complet :
{{
  "nom_usage": "",
  "nom_naissance": "",
  "prenoms": "",
  "sexe": "",
  "date_naissance": "",
  "commune_naissance": "",
  "adresse_complete": "",
  "telephone": "",
  "vit_seul": "",
  "lieu_actuel": "domicile",
  "apa": "",
  "gir": "",
  "mdph": null,
  "ald": null,
  "description_situation": "",
  "actions_entreprises": "",
  "attentes_dac": "",
  "alertes": {{
    "pb_actes_essentiels": false,
    "pb_activites_domestiques": false,
    "pathologies_chroniques": false,
    "pb_memoire_decision": false,
    "troubles_comportement": false,
    "conduites_addictives": false,
    "medocs_plus_de_5": false,
    "troubles_psy": false,
    "denutrition_perte_poids": false,
    "risque_chute": false,
    "hospit_recente": false,
    "hospit_date": "",
    "hospit_motif": "",
    "isolement_social": false,
    "epuisement_aidant": false,
    "diff_financieres": false,
    "logement_inadapte": false,
    "incurie_insalubrite": false
  }},
  "cercle_de_soins": [
    {{
      "type": "remplacer_par_le_bon_type",
      "nom": "",
      "tel": "",
      "email": ""
    }}
  ]
}}
(Note: La liste cercle_de_soins doit être vide `[]` si aucun professionnel n'est mentionné.)
"""
        parsed = await self.client.generate_json(prompt)
        text_lower = raw_text.lower()
        
        # POST-PROCESSING POUR L'AGE ET LES NOMS :
        import re
        date_n = parsed.get("date_naissance", "")
        if "ans" in date_n.lower():
            match = re.search(r'(\d+)', date_n)
            if match:
                age = int(match.group(1))
                year = datetime.datetime.now().year - age
                parsed["date_naissance"] = str(year)
                
        nom = parsed.get("nom_usage", "")
        prenom = parsed.get("prenoms", "")
        if prenom and prenom.lower() in nom.lower():
            nom = re.sub(r'(?i)' + re.escape(prenom), "", nom).replace(",", "").strip()
            parsed["nom_usage"] = nom
            
        adresse = parsed.get("adresse_complete", "")
        if " à " in adresse:
            parsed["adresse_complete"] = adresse.replace(" à ", ", ")
            
        cercle = parsed.get("cercle_de_soins", [])
        for pro in cercle:
            # Nettoyage des titres dans le nom
            pro_nom = pro.get("nom", "")
            for titre in ["le docteur", "docteur", "dr.", "dr", "monsieur", "madame"]:
                # On utilise regex pour remplacer le titre entier sans toucher aux autres lettres
                pro_nom = re.sub(r'(?i)\b' + titre + r'\b', "", pro_nom)
            pro["nom"] = pro_nom.replace(",", "").strip()
            
            # Nettoyage des emails hallucinés
            pro_email = pro.get("email", "")
            if "exemple" in pro_email.lower() or "example" in pro_email.lower():
                pro["email"] = ""
        
        # POST-PROCESSING DE SÉCURITÉ :
        # L'IA a tendance à halluciner des hospitalisations. On force à False si les mots clés sont absents.
        if parsed.get("alertes"):
            if not any(word in text_lower for word in ["hospit", "urgenc"]):
                parsed["alertes"]["hospit_recente"] = False
                parsed["alertes"]["hospit_date"] = ""
                parsed["alertes"]["hospit_motif"] = ""
                
        # L'IA hallucine souvent l'APA pour les personnes âgées. On force à vide si le mot n'y est pas.
        if "apa" not in text_lower:
            parsed["apa"] = ""
                
        return parsed
