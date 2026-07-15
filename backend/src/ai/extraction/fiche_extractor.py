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
  - Dans `nom_usage`, mets le nom de famille DU PATIENT. Ne mets JAMAIS les titres (Monsieur, Madame, Veuve, etc). Ne mets JAMAIS la profession ou le nom de l'émetteur (ex: si le texte dit "Je suis assistante sociale", ne mets pas ça dans le nom du patient). Si le texte décrit le patient de manière anonyme (ex: "un monsieur de 36 ans", "cette dame"), laisse vide `""` ! Si tu vois le prénom dedans, retire-le. Si le nom n'est pas donné, laisse vide `""`.
  - Dans `prenoms`, mets UNIQUEMENT le vrai prénom du patient. Si aucun prénom n'est donné, laisse STRICTEMENT vide `""`. N'utilise jamais les mots anonymes, titres, origines ou nationalités (ex: "Afghan").
  - Si un âge est donné pour le patient (ex: 36 ans), écris simplement cet âge (ex: "36") dans `date_naissance`. Ne te trompe pas avec d'autres durées mentionnées dans le texte (ex: "depuis 20 ans"). Si aucun âge ni date n'est donné, laisse strictement vide `""`.
  - Ne confonds pas la ville de résidence avec la ville de naissance : si la personne "habite à Toulon", cela va dans `adresse_complete`. `commune_naissance` reste vide `""`.
  - Pour l'adresse, n'invente rien. Si seule la ville est donnée (ex: "Toulon"), mets juste "Toulon".
  - Pour `vit_seul`, mets "Non" si le texte indique clairement que la personne est accompagnée (ex: "habite avec moi", "vit avec son fils"). S'il n'y a aucune précision, laisse strictement vide `""`. Ne déduis rien.
  - Pour `lieu_actuel`, si le texte ne précise pas explicitement s'il vit à domicile ou en établissement (ou s'il est à la rue/en cours d'expulsion), laisse STRICTEMENT vide `""`. Ne déduis JAMAIS "domicile" par défaut.
  - Pour `apa`, `gir`, `ald`, `mdph` : ne les déduis JAMAIS de l'âge ou de la situation. S'ils ne sont pas mentionnés, laisse vide `""` ou `null`.
  - Pour `hospit_recente` : mets `true` SI ET SEULEMENT SI le mot "hôpital", "hospitalisation", ou "urgences" est dans le texte. Sinon, mets `false` et laisse `hospit_date` et `hospit_motif` vides `""`. 
  - Si une hospitalisation est mentionnée mais que la date est floue (ex: "dimanche", "il y a 3 semaines"), écris cette phrase exacte dans `hospit_date`. Ne laisse pas vide si l'utilisateur a donné un repère temporel.

RÉCIT : "{raw_text}"

### DONNÉES À EXTRAIRE :
Emetteur (la personne qui fait la demande ou décrit la situation) :
- emetteur_nom (chaîne, nom de famille, ou vide)
- emetteur_prenom (chaîne, ou vide)
- emetteur_service (chaîne, profession ou service, ex: "assistante sociale", ou vide)
- emetteur_telephone (chaîne, ou vide)
- emetteur_email (chaîne, ou vide)

Identité du patient :
- nom_usage (chaîne)
- nom_naissance (chaîne)
- prenoms (chaîne)
- sexe (chaîne: "F", "M" ou "")
- date_naissance (chaîne JJ/MM/AAAA)
- commune_naissance (chaîne)
- adresse_complete (chaîne, ex: "Toulon" ou "12 avenue de la Gare, Nice" selon ce qui est écrit)
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
- motif_or_description (chaîne, FAIS UN RÉSUMÉ TRÈS DÉTAILLÉ ET COMPLET DE LA SITUATION ENTIÈRE, incluant tout le contexte, les problèmes, et l'histoire. Ne sois pas bref, reprends tous les éléments factuels pertinents.)
- attentes_dac (chaîne, qu'attend-on du DAC ?)

Alertes (mettre `true` si le problème est mentionné explicitement ou via des synonymes. Ne sois pas trop rigide) :
- pb_actes_essentiels (se nourrir, se vêtir, se laver, hygiène)
- pb_activites_domestiques (courses, ménage, repas)
- pathologies_chroniques (maladie grave, cancer, diabète, etc)
- pb_memoire_decision (oubli, Alzheimer, désorientation)
- troubles_comportement (agressivité, fugue, cris)
- conduites_addictives (ancien toxicomane, alcool, drogue, sevrage)
- medocs_plus_de_5
- troubles_psy (santé mentale, dépression, angoisse, psychiatrie)
- denutrition_perte_poids (maigreur, perte d'appétit)
- risque_chute (tombe souvent, équilibre instable)
- hospit_recente
- hospit_date (chaîne: format JJ/MM/AAAA ou date explicite)
- hospit_motif (chaîne: motif de l'hospitalisation)
- isolement_social (seul, pas de famille, pas d'amis)
- epuisement_aidant (famille fatiguée, aidant à bout)
- diff_gestion_admin_fin (soucis pour gérer l'administratif ou les finances générales)
- risque_precarite (situation précaire, très faible revenus)
- dettes_impayes (surendettement, dettes, impayés)
- perte_acces_droit (problème d'accès aux droits, papiers d'identité, droit d'asile)
- logement_inadapte (expulsion, sans-abri, insalubre, inadapté au handicap)
- incurie_insalubrite (logement très sale, accumulation)

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
  "emetteur_structure": "",
  "emetteur_service": "",
  "emetteur_fonction": "",
  "emetteur_nom": "",
  "emetteur_prenom": "",
  "emetteur_telephone": "",
  "emetteur_mail": "",
  "nom_usage": "",
  "nom_naissance": "",
  "prenoms": "",
  "sexe": "",
  "date_naissance": "",
  "commune_naissance": "",
  "adresse_complete": "",
  "telephone": "",
  "vit_seul": "",
  "lieu_actuel": "",
  "apa": "",
  "gir": "",
  "mdph": null,
  "ald": null,
  "description_situation": "",
  "actions_entreprises": "",
  "motif_or_description": "",
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
    "diff_gestion_admin_fin": false,
    "risque_precarite": false,
    "dettes_impayes": false,
    "perte_acces_droit": false,
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
        # Si on n'a pas de "/" c'est que ce n'est pas une date complète, c'est sûrement un âge
        if date_n and "/" not in date_n:
            match = re.search(r'\b(\d{1,3})\b', date_n)
            if match:
                age = int(match.group(1))
                if age < 130: # Eviter de transformer une vraie année genre "1990" en âge
                    year = datetime.datetime.now().year - age
                    parsed["date_naissance"] = str(year)
                
        nom = parsed.get("nom_usage", "")
        # Nettoyage des noms anonymes
        if any(x in nom.lower() for x in ["ans", "monsieur", "dame", "patient", "usager", "homme", "femme"]):
            parsed["nom_usage"] = ""
            nom = ""
            
        prenom = parsed.get("prenoms", "")
        if any(x in prenom.lower() for x in ["ans", "monsieur", "dame", "patient", "usager", "homme", "femme", "m.", "mme", "afghan", "origine"]):
            parsed["prenoms"] = ""
            prenom = ""
            
        # Anti-hallucination : si le prénom n'est même pas dans le texte original, c'est une invention !
        if prenom and prenom.lower() not in text_lower:
            parsed["prenoms"] = ""
            prenom = ""
            
        if prenom and prenom.lower() in nom.lower():
            nom = re.sub(r'(?i)' + re.escape(prenom), "", nom).replace(",", "").strip()
            parsed["nom_usage"] = nom
            
        # Correction automatique Service vs Fonction pour l'émetteur
        service = parsed.get("emetteur_service", "").lower()
        if "assistant" in service or "medecin" in service or "médecin" in service or "infirmier" in service:
            if not parsed.get("emetteur_fonction"):
                parsed["emetteur_fonction"] = parsed["emetteur_service"]
                parsed["emetteur_service"] = ""
            
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
                
        # L'IA hallucine souvent l'APA pour les personnes âgées. On force à vide si le mot exact n'y est pas.
        # \bapa\b permet de s'assurer qu'on ne matche pas "capacités" par erreur !
        if not re.search(r'\bapa\b', text_lower):
            parsed["apa"] = ""
            
        # POST-PROCESSING ALERTES (Fallback Regex si le LLM a raté l'info)
        if "alertes" not in parsed:
            parsed["alertes"] = {}
        
        if not parsed["alertes"].get("troubles_psy"):
            parsed["alertes"]["troubles_psy"] = any(x in text_lower for x in ["santé mentale", "sante mentale", "psy", "dépression", "depression", "angoisse", "suicide", "bipolaire", "schizo"])
        
        if not parsed["alertes"].get("diff_gestion_admin_fin"):
            parsed["alertes"]["diff_gestion_admin_fin"] = any(x in text_lower for x in ["soucis administratifs", "gestion administrative", "financier", "budget"])
            
        if not parsed["alertes"].get("risque_precarite"):
            parsed["alertes"]["risque_precarite"] = any(x in text_lower for x in ["précarité", "precarite", "précaris", "precaris", "ressources très faibles"])
            
        if not parsed["alertes"].get("dettes_impayes"):
            parsed["alertes"]["dettes_impayes"] = any(x in text_lower for x in ["dette", "impayé", "impaye", "surendettement"])
            
        if not parsed["alertes"].get("perte_acces_droit"):
            parsed["alertes"]["perte_acces_droit"] = any(x in text_lower for x in ["droit d'asile", "accès aux droits", "acces aux droits", "sans papier", "faire valoir ses droits"])
            
        if not parsed["alertes"].get("logement_inadapte"):
            parsed["alertes"]["logement_inadapte"] = any(x in text_lower for x in ["expulsion", "sans abri", "sdf", "insalubre", "logement inadapté", "logement inadapte", "rue"])
            
        if not parsed["alertes"].get("conduites_addictives"):
            parsed["alertes"]["conduites_addictives"] = any(x in text_lower for x in ["toxico", "addict", "alcool", "drogue", "sevrage", "stupéfiant", "stupefiant"])
            
        if not parsed["alertes"].get("isolement_social"):
            parsed["alertes"]["isolement_social"] = any(x in text_lower for x in ["isolé", "isole", "pas de famille", "rupture"])
                
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

### ADRESSEUR / ÉMETTEUR (Celui qui écrit la demande)
- emetteur_structure (chaîne, ex: "Hôpital Sainte Musse", "CCAS")
- emetteur_service (chaîne, le service exact de l'émetteur)
- emetteur_fonction (chaîne, ex: "Assistante sociale", "Médecin traitant")
- emetteur_nom (chaîne, nom de famille de l'émetteur)
- emetteur_prenom (chaîne)
- emetteur_telephone (chaîne)
- emetteur_mail (chaîne)

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
