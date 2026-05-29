import json
import datetime
from infrastructure.llm_client import OllamaClient

class FicheExtractor:
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
- adresse_complete (chaîne, ex: "10 rue des Lilas, Toulon")
- telephone (chaîne, téléphone personnel du patient UNIQUEMENT. N'y mets JAMAIS le numéro d'un médecin ou professionnel)
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
- type (chaîne STRICTE parmi : "medecin_traitant", "specialiste", "infirmier", "ssiad_had", "saad" (UNIQUEMENT pour aide à domicile, ménage, ADMR), "palliatifs", "pharmacien", "kine", "repas" (pour le portage de repas), "telealarme", "social", "autre")
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
                
        # Nettoyage des téléphones dupliqués (IA zélée qui copie le tel du pro dans le tel du patient)
        patient_tel = parsed.get("telephone", "")
        if patient_tel:
            for pro in cercle:
                if pro.get("tel") == patient_tel:
                    parsed["telephone"] = ""
                    break
        
        # POST-PROCESSING DE SÉCURITÉ :
        # L'IA a tendance à halluciner des hospitalisations. On force à False si les mots clés sont absents ou si négation.
        if parsed.get("alertes"):
            text_for_hospit = text_lower
            if "hospit" not in text_for_hospit and "urgence" not in text_for_hospit and "clinique" not in text_for_hospit:
                parsed["alertes"]["hospit_recente"] = False
            elif "n'a pas été hospit" in text_for_hospit or "pas d'hospit" in text_for_hospit or "sans hospit" in text_for_hospit or "non hospit" in text_for_hospit:
                parsed["alertes"]["hospit_recente"] = False
            elif "jamais été hospit" in text_for_hospit:
                parsed["alertes"]["hospit_recente"] = False
                
            if not parsed["alertes"].get("hospit_recente", True):
                parsed["alertes"]["hospit_date"] = ""
                parsed["alertes"]["hospit_motif"] = ""
                
        # L'IA hallucine souvent l'APA pour les personnes âgées. On force à vide si le mot n'y est pas.
        if "apa" not in text_lower:
            parsed["apa"] = ""
                
        return parsed

    async def extract_for_clic(self, raw_text: str):
        prompt = f"""
### EXPERT ORIA - EXTRACTION FICHE CLIC
Analyse le récit suivant pour remplir précisément une Fiche d'Orientation CLIC.

### INSTRUCTIONS DE REMPLISSAGE
- Si une information n'est pas mentionnée dans le texte, laisse-la STRICTEMENT vide (`""`).
- Ne déduis rien.
- NE JAMAIS mettre le nom du patient dans la section Emetteur. L'émetteur est la personne qui FAIT la demande (ex: une assistante sociale, un médecin, un proche). Si le texte décrit juste le patient sans préciser qui écrit la demande, laisse TOUTE la section Emetteur (nom, prenom, service, email, telephone) STRICTEMENT vide `""`. L'IA ne doit JAMAIS mettre le nom de l'usager dans "emetteur_nom".
- "usager_vit_seul": booléen (true, false, ou null)

RÉCIT : "{raw_text}"

### DONNÉES À EXTRAIRE :
Emetteur :
- emetteur_nom (chaîne, nom de famille, ou vide)
- emetteur_prenom (chaîne)
- emetteur_service (chaîne, profession ou service)
- emetteur_telephone (chaîne)
- emetteur_email (chaîne)

Identité du patient :
- usager_nom_usage (chaîne, le nom de famille de l'usager, ex: "Dupont")
- usager_nom_naissance (chaîne)
- usager_prenoms (chaîne, le prénom de l'usager, ex: "Michèle")
- usager_sexe (chaîne: "femme" ou "homme" ou "")
- usager_date_naissance (chaîne)
- usager_adresse (chaîne)
- usager_telephone (chaîne)
- usager_email (chaîne)
- usager_vit_seul (booléen: true, false, ou null)

Motif de la demande :
- motif_1 (chaîne, ce que la personne demande ou recherche, ex: "mise en place portage de repas")
- motif_2 (chaîne, autre problème ou besoin)
- motif_3 (chaîne)

Famille / Aidant à contacter :
- aidant_nom (chaîne)
- aidant_lien (chaîne, ex: "fille", "fils", "épouse")
- aidant_tel (chaîne)
- aidant_email (chaîne)
- aidant_adresse (chaîne)

Aides relatives au maintien à domicile :
- aide_1 (chaîne, les aides DÉJÀ EN PLACE actuellement. Si aucune, laisse STRICTEMENT vide)
- aide_2 (chaîne)

### FORMAT JSON (STRICT)
Réponds UNIQUEMENT par ce JSON complet :
{{
  "emetteur_nom": "",
  "emetteur_prenom": "",
  "emetteur_service": "",
  "emetteur_telephone": "",
  "emetteur_email": "",
  "usager_nom_usage": "",
  "usager_nom_naissance": "",
  "usager_prenoms": "",
  "usager_sexe": "",
  "usager_date_naissance": "",
  "usager_adresse": "",
  "usager_telephone": "",
  "usager_email": "",
  "usager_vit_seul": null,
  "motif_1": "",
  "motif_2": "",
  "motif_3": "",
  "aidant_nom": "",
  "aidant_lien": "",
  "aidant_tel": "",
  "aidant_email": "",
  "aidant_adresse": "",
  "aide_1": "",
  "aide_2": ""
}}
"""
        parsed = await self.client.generate_json(prompt)
        
        # POST-PROCESSING
        import re
        
        # Nettoyage usager_nom_usage
        nom = parsed.get("usager_nom_usage", "")
        prenom = parsed.get("usager_prenoms", "")
        
        # Enlever les titres
        for titre in ["monsieur", "madame", "mme", "m.", "veuve", "vve"]:
            nom = re.sub(r'(?i)\b' + titre + r'\b', "", nom)
            
        # Si le prénom est dans le nom, l'enlever
        if prenom and prenom.lower() in nom.lower():
            nom = re.sub(r'(?i)' + re.escape(prenom), "", nom)
            
        parsed["usager_nom_usage"] = nom.replace(",", "").strip()
        
        # Securité anti-hallucination pour l'émetteur : si pas de nom, on vide le reste
        if not parsed.get("emetteur_nom"):
            parsed["emetteur_prenom"] = ""
            parsed["emetteur_service"] = ""
            parsed["emetteur_telephone"] = ""
            parsed["emetteur_email"] = ""
            
        # Toujours forcer la date d'émission au jour J
        parsed["emetteur_date"] = datetime.datetime.now().strftime("%d/%m/%Y")
            
        return parsed
