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
  - Sépare TOUJOURS le prénom et le nom de famille. 
  - RÈGLE ABSOLUE SUR "ORIA" : "ORIA" (ou "Oria") est le nom du logiciel. Il est STRICTEMENT INTERDIT de l'utiliser comme prénom ou nom, que ce soit pour le patient (`nom_usage`, `prenoms`) ou pour l'émetteur (`emetteur_nom`, `emetteur_prenom`). Si l'émetteur n'est pas clairement identifié, laisse vide.
  - Dans `nom_usage`, mets UNIQUEMENT le nom de famille DU PATIENT (souvent écrit en majuscules ou cité en dernier). Ne mets JAMAIS le prénom ici. Ne mets JAMAIS les titres (Monsieur, Madame, Veuve, etc). Si un seul mot est donné après Monsieur/Madame, c'est TOUJOURS le nom de famille, mets-le dans `nom_usage`.
  - Dans `prenoms`, mets UNIQUEMENT le prénom du patient. N'y mets JAMAIS le nom de famille. Si le texte dit "Emile ELLA", "ELLA" va dans `nom_usage` et "Emile" va dans `prenoms`. Si aucun prénom n'est donné, laisse STRICTEMENT vide `""`.
  - Dans `date_naissance`, si une date de naissance exacte est donnée, utilise le format JJ/MM/AAAA. Si seul un âge est donné (ex: 80), écris simplement cet âge en chiffres suivi de "ans" (ex: "80 ans"). Ne te trompe pas avec d'autres durées mentionnées dans le texte (ex: "depuis 20 ans"). Si aucun âge ni date n'est donné, laisse strictement vide `""`.
  - Pour le `sexe`, tu es EXCEPTIONNELLEMENT AUTORISÉ À DÉDUIRE l'information. Si le texte parle d'un homme (ex: "Monsieur", "il", "le patient", ou adjectifs masculins comme "précarisé", "toxicomane"), mets "M". Si le texte parle d'une femme (ex: "Madame", "elle", "la patiente"), mets "F". ATTENTION : Ne te fie JAMAIS au nom de famille (ex: "ELLA") pour déduire le sexe. Base-toi uniquement sur "Monsieur/Madame" et les accords grammaticaux. En cas de doute, laisse vide `""`.
  - Analyse le SENS RÉEL des phrases. Ne confonds pas la ville de résidence avec la ville de naissance : si la personne "habite à Toulon", cela va dans `adresse_complete`, et `commune_naissance` reste vide `""`. 
  - RÈGLE ABSOLUE SUR `commune_naissance` : Une commune est EXCLUSIVEMENT un nom de ville (ex: "Paris", "Marseille"). Il est STRICTEMENT INTERDIT d'y mettre une nationalité, une origine, un pays, ou une phrase (ex: "Afghane", "France", "d'origine afghane", "en France depuis..."). Si le texte dit "d'origine Afghane", on ne connait pas la ville de naissance. Tu DOIS laisser `commune_naissance` STRICTEMENT vide `""`. N'extrapole pas.
  - Pour l'adresse, n'invente rien. Si seule la ville est donnée (ex: "Toulon"), mets juste "Toulon".
  - Pour `vit_seul`, mets "true" si elle vit seule, et "false" si le texte indique clairement que la personne est accompagnée (ex: "habite avec moi", "vit avec son fils"). S'il n'y a aucune précision, laisse strictement vide `""`. Ne déduis rien.
  - Pour `lieu_actuel`, si le texte ne contient pas EXPLICITEMENT les mots "domicile", "chez lui", "appartement", "maison" ou "établissement", laisse STRICTEMENT vide `""`. Ne déduis JAMAIS "domicile" juste parce qu'il vit dans une ville ou a une "expulsion locative".
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
- description_situation (chaîne, résumé détaillé)
- actions_entreprises (chaîne, qu'est-ce qui a déjà été fait ?)
- motif_or_description (chaîne, RECOPIE INTÉGRALEMENT PRESQUE TOUS LES DÉTAILS UTILES DU TEXTE. La description doit être très longue et complète. Reprends tous les éléments factuels.)
- attentes_dac (chaîne, DÉDUIS ET DÉCRIS EN DÉTAIL les attentes envers le DAC pour aider la personne, ex: "Accompagnement global, coordination médicale et aide administrative")

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
                if age < 120:
                    parsed["date_naissance"] = f"{age} ans"
                
        nom = parsed.get("nom_usage", "")
        # Nettoyage des noms anonymes
        if any(x in nom.lower() for x in ["ans", "monsieur", "dame", "patient", "usager", "homme", "femme"]):
            parsed["nom_usage"] = ""
            nom = ""
            
        prenom = parsed.get("prenoms", "")
        if any(x in prenom.lower() for x in ["ans", "monsieur", "dame", "patient", "usager", "homme", "femme", "m.", "mme", "afghan", "origine"]):
            parsed["prenoms"] = ""
            prenom = ""
            
        # Hardcode block against ORIA
        if parsed.get("prenoms", "").lower() == "oria": parsed["prenoms"] = ""
        if parsed.get("nom_usage", "").lower() == "oria": parsed["nom_usage"] = ""
        if parsed.get("emetteur_prenom", "").lower() == "oria": parsed["emetteur_prenom"] = ""
        if parsed.get("emetteur_nom", "").lower() == "oria": parsed["emetteur_nom"] = ""
        
        # Hardcode block against Nationalities in commune
        commune = parsed.get("commune_naissance", "").lower()
        if any(nat in commune for nat in ["afghan", "français", "francais", "origine", "depuis", "italien", "espagnol", "marocain", "algerien", "tunisien"]):
            parsed["commune_naissance"] = ""
            
        # Hardcode gender fallback
        if "monsieur" in text_lower and "madame" not in text_lower:
            parsed["sexe"] = "M"
        elif "madame" in text_lower and "monsieur" not in text_lower:
            parsed["sexe"] = "F"
            
        # Clean up "none" or "null" strings that might come from the AI
        for field in ["gir", "apa", "mdph", "ald"]:
            val = parsed.get(field)
            if val is None or str(val).lower() in ["none", "null"]:
                parsed[field] = ""
            
        # Anti-collision globale (DAC)
        em_prenom = str(parsed.get("emetteur_prenom", "")).lower().strip()
        us_prenom = str(parsed.get("prenoms", "")).lower().strip()
        em_tel = str(parsed.get("emetteur_telephone", "")).strip()
        us_tel = str(parsed.get("telephone", "")).strip()
        em_email = str(parsed.get("emetteur_mail", "")).strip()
        
        if em_prenom and em_prenom == us_prenom:
            parsed["prenoms"] = ""
        if em_tel and em_tel == us_tel:
            parsed["telephone"] = ""
            
        # Anti-hallucination : si le nom ou prénom n'est même pas dans le texte original, c'est une invention (souvent copié du prompt) !
        if nom and nom.lower() not in text_lower:
            parsed["nom_usage"] = ""
            nom = ""
            
        # Anti-hallucination : l'IA met parfois la ville à la place du nom
        if nom and any(ville in nom.lower() for ville in ["seyne", "toulon", "hyeres", "hyères", "marseille", "frejus", "fréjus"]):
            parsed["nom_usage"] = ""
            nom = ""
            
        if prenom and prenom.lower() not in text_lower:
            parsed["prenoms"] = ""
            prenom = ""
            
        # Correction si le LLM a mis le seul nom dans "prenoms" au lieu de "nom_usage"
        if prenom and not nom:
            # S'il y a un seul mot et pas de nom, c'est sûrement le nom de famille
            if len(prenom.split()) == 1:
                parsed["nom_usage"] = prenom.upper()
                parsed["prenoms"] = ""
                nom = prenom.upper()
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
            
        if parsed.get("attentes_dac") and "qu'attend-on" in parsed.get("attentes_dac").lower():
            parsed["attentes_dac"] = "Besoin d'accompagnement et de coordination pour la prise en charge globale."
            
        vit_seul = parsed.get("vit_seul", "")
        if vit_seul:
            if not any(x in text_lower for x in ["seul", "seule", "vit avec", "habite avec", "mari", "femme", "épouse", "epouse", "enfant", "fils", "fille", "conjoint", "famille"]):
                parsed["vit_seul"] = ""
                
        lieu_actuel = parsed.get("lieu_actuel", "")
        if "domicile" in lieu_actuel.lower():
            if not any(x in text_lower for x in ["domicile", "chez", "appartement", "maison", "logement"]):
                parsed["lieu_actuel"] = ""
            
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
            parsed["alertes"]["isolement_social"] = any(x in text_lower for x in ["isolé", "isole", "pas de famille", "rupture", "besoin d’être accompagné", "besoin d'être accompagné", "sans appui"])
                
        return parsed

    async def extract_for_clic(self, raw_text: str):
        prompt = f"""
### EXPERT ORIA - EXTRACTION FICHE CLIC
Analyse le récit suivant pour remplir précisément une Fiche d'Orientation CLIC.

### INSTRUCTIONS DE REMPLISSAGE
- Si une information n'est pas mentionnée dans le texte, laisse-la STRICTEMENT vide (`""`).
- **NE DÉDUIS RIEN** : N'invente aucune information. Si ce n'est pas écrit noir sur blanc, laisse vide `""`.
- **RÈGLES STRICTES** :
  - Dans `usager_nom_usage`, mets le nom de famille DU PATIENT. Ne mets JAMAIS les titres (Monsieur, Madame, Veuve, etc).
  - Dans `usager_prenoms`, mets UNIQUEMENT le vrai prénom du patient.
  - Si un âge est donné pour le patient, écris simplement cet âge dans `usager_date_naissance`. ATTENTION: Ne te trompe pas avec d'autres durées mentionnées dans le texte (ex: "depuis 4 ans", "depuis 20 ans"). L'âge doit se rapporter au patient. Si aucun âge n'est donné, laisse vide `""`.
  - Ne confonds pas la ville de résidence avec la ville de naissance : si la personne "habite à Toulon", cela va dans `usager_adresse`. `usager_ville_naissance` n'existe pas, mais si la ville est donnée pour son lieu de vie actuel, c'est `usager_adresse`.
  - Pour `usager_adresse`, si seule la ville est donnée (ex: "la Seyne sur Mer"), mets la ville ici. N'invente pas de rue.
  - Pour `usager_vit_seul`, mets "true" si elle vit seule, et "false" si le texte indique clairement que la personne est accompagnée (ex: "habite avec moi", "vit avec son fils"). S'il n'y a aucune précision, laisse null.

RÉCIT : "{raw_text}"

### ADRESSEUR / ÉMETTEUR (Celui qui écrit la demande)
- emetteur_structure (chaîne, ex: "Hôpital Sainte Musse", "CCAS")
- emetteur_service (chaîne, le service, ou le lien de parenté si c'est un proche ex: "Fille", "Fils", "Voisin")
- emetteur_fonction (chaîne, ex: "Assistante sociale", "Médecin traitant")
- emetteur_nom (chaîne, nom de famille de l'émetteur)
- emetteur_prenom (chaîne)
- emetteur_telephone (chaîne)
- emetteur_mail (chaîne)

Identité du patient :
- usager_nom_usage (chaîne, le nom de famille de l'usager, ou vide)
- usager_nom_naissance (chaîne)
- usager_prenoms (chaîne, le prénom de l'usager. ATTENTION: ne confondez pas avec le prénom du demandeur/proche. Laissez vide si non précisé)
- usager_sexe (chaîne: "femme" ou "homme" ou "")
- usager_date_naissance (chaîne, la date de naissance OU simplement l'âge s'il est donné, ex: "82 ans")
- usager_adresse (chaîne, l'adresse ou simplement la ville si l'adresse exacte n'est pas connue)
- usager_telephone (chaîne)
- usager_email (chaîne)
- usager_vit_seul (booléen: true, false, ou null)

Motif de la demande :
- motif_1 (chaîne, reformule le besoin principal de manière professionnelle et neutre (ex: "Mise en place d'un portage de repas", "Évaluation globale de la situation"). Ne jamais utiliser "je" ni "ma/mon")
- motif_2 (chaîne, autre problème ou besoin, reformulé de manière professionnelle. Ex: "Soutien psychologique pour l'aidant")
- motif_3 (chaîne, autre motif ou vide)
IMPORTANT : Rédigez tous les motifs de manière impersonnelle ou à l'infinitif. Bannissez les formulations du type "pour ma mère" ou "pour moi-même".

Famille / Aidant à contacter :
- aidant_nom (chaîne, ou vide)
- aidant_lien (chaîne, ex: "fille", "fils", "épouse". Si l'émetteur est un proche, recopie ce lien ici même si le nom n'est pas connu)
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
        text_lower = raw_text.lower()
        
        # POST-PROCESSING
        import re
        
        # Nettoyage usager_nom_usage et usager_prenoms
        nom = parsed.get("usager_nom_usage", "")
        prenom = parsed.get("usager_prenoms", "")
        
        # Enlever les titres
        for titre in ["monsieur", "madame", "mme", "m.", "veuve", "vve"]:
            nom = re.sub(r'(?i)\b' + titre + r'\b', "", nom)
            prenom = re.sub(r'(?i)\b' + titre + r'\b', "", prenom)
            
        # Anti-hallucination : l'IA invente ou copie "L'usager"
        if nom and nom.lower() in ["l'usager", "usager"]:
            nom = ""
            
        # Anti-hallucination : si le nom ou prénom n'est pas dans le texte
        if nom and nom.lower() not in text_lower:
            nom = ""
            
        # Anti-hallucination : ville dans le nom
        if nom and any(ville in nom.lower() for ville in ["seyne", "toulon", "hyeres", "hyères", "marseille", "frejus", "fréjus"]):
            nom = ""
            
        if prenom and prenom.lower() not in text_lower:
            prenom = ""
            
        # Anti-hallucination prénom ("la fille de...")
        if prenom and ("fille" in prenom.lower() or "fils" in prenom.lower() or len(prenom.split()) > 3):
            prenom = ""
            
        # Si le prénom est dans le nom, l'enlever
        if prenom and prenom.lower() in nom.lower():
            nom = re.sub(r'(?i)' + re.escape(prenom), "", nom)
            
        parsed["usager_nom_usage"] = nom.replace(",", "").strip()
        parsed["usager_prenoms"] = prenom.replace(",", "").strip()
        
        # Fallback python ultra-robuste pour vit_seul
        if parsed.get("usager_vit_seul") is None:
            if any(x in text_lower for x in ["vit seul", "vit seule", "habite seul", "habite seule"]):
                parsed["usager_vit_seul"] = True
                
        # Fallback python pour la ville si l'IA l'a ratée
        if not parsed.get("usager_adresse"):
            for ville in ["la seyne sur mer", "la seyne-sur-mer", "toulon", "hyères", "hyeres", "marseille", "fréjus", "frejus"]:
                if ville in text_lower:
                    parsed["usager_adresse"] = ville.title()
                    break
        
        # Anti-hallucination pour l'émetteur
        emetteur_nom = parsed.get("emetteur_nom", "")
        emetteur_prenom = parsed.get("emetteur_prenom", "")
        for titre in ["monsieur", "madame", "mme", "m.", "veuve", "vve"]:
            emetteur_nom = re.sub(r'(?i)\b' + titre + r'\b', "", emetteur_nom)
            emetteur_prenom = re.sub(r'(?i)\b' + titre + r'\b', "", emetteur_prenom)
            
        parsed["emetteur_nom"] = emetteur_nom.strip()
        parsed["emetteur_prenom"] = emetteur_prenom.strip()
            
        if parsed["emetteur_nom"] and parsed["emetteur_nom"].lower() not in text_lower:
            parsed["emetteur_nom"] = ""
            
        # Securité anti-hallucination pour l'émetteur : si pas de nom, on vide le prénom
        if not parsed.get("emetteur_nom"):
            parsed["emetteur_prenom"] = ""
            parsed["emetteur_telephone"] = ""
            parsed["emetteur_email"] = ""
            
        # Anti-hallucination : téléphones inventés
        text_no_space = text_lower.replace(" ", "").replace(".", "")
        for t_field in ["usager_telephone", "emetteur_telephone", "aidant_tel"]:
            t_val = str(parsed.get(t_field, "")).replace(" ", "").replace(".", "")
            if t_val and t_val not in text_no_space:
                parsed[t_field] = ""
                
        # Anti-collision globale : Si l'émetteur est un proche/aidant, on empêche l'IA de copier ses infos dans l'usager
        em_prenom = str(parsed.get("emetteur_prenom", "")).lower().strip()
        us_prenom = str(parsed.get("usager_prenoms", "")).lower().strip()
        em_tel = str(parsed.get("emetteur_telephone", "")).strip()
        us_tel = str(parsed.get("usager_telephone", "")).strip()
        em_email = str(parsed.get("emetteur_email", "")).strip()
        us_email = str(parsed.get("usager_email", "")).strip()
        
        if em_prenom and em_prenom == us_prenom:
            parsed["usager_prenoms"] = ""
        if em_tel and em_tel == us_tel:
            parsed["usager_telephone"] = ""
        if em_email and em_email == us_email:
            parsed["usager_email"] = ""
                
        # Age -> Année de naissance (comme affiné ce matin)
        age_str = str(parsed.get("usager_date_naissance", ""))
        if "depuis" in age_str.lower() or ("4" in age_str and "troubles" in text_lower) or "?" in age_str:
            parsed["usager_date_naissance"] = ""
        elif age_str and "/" not in age_str:
            match = re.search(r'\b(\d{1,3})\b', age_str)
            if match:
                age = int(match.group(1))
                if age < 130:
                    year = datetime.datetime.now().year - age
                    parsed["usager_date_naissance"] = str(year)
            
        # Fallback Python ultra-robuste pour Aidant / Proche si l'IA l'a manqué
        if not parsed.get("aidant_nom"):
            m_aidant = re.search(r'(?:proche\s+aidant(?:\s+principal)?\s*:\s*)?(?:sa|son)?\s*(fille|fils|mari|épouse|epouse|conjoint|soeur|frère|aidant|aidante)?\s*([A-ZÀ-ÿ][a-zÀ-ÿ\-]+(?:\s+[A-ZÀ-ÿ][a-zÀ-ÿ\-]+)?)\s*(?:au|tél|tel|\,)?\s*(0[1-9][\s\.\-]?\d{2}[\s\.\-]?\d{2}[\s\.\-]?\d{2}[\s\.\-]?\d{2})?', text, re.IGNORECASE)
            if m_aidant and m_aidant.group(2):
                if m_aidant.group(1):
                    parsed["aidant_lien"] = m_aidant.group(1).strip()
                parsed["aidant_nom"] = m_aidant.group(2).strip()
                if m_aidant.group(3) and not parsed.get("aidant_tel"):
                    parsed["aidant_tel"] = m_aidant.group(3).strip()

        # Chercher le numéro de tel de l'aidant si présent et pas encore capturé
        if parsed.get("aidant_nom") and not parsed.get("aidant_tel"):
            tel_aid_m = re.search(re.escape(parsed["aidant_nom"]) + r'.*?(0[1-9][\s\.\-]?\d{2}[\s\.\-]?\d{2}[\s\.\-]?\d{2}[\s\.\-]?\d{2})', text, re.IGNORECASE | re.DOTALL)
            if tel_aid_m:
                parsed["aidant_tel"] = tel_aid_m.group(1).strip()

        # Anti-collision Cercle de Soins vs Aidant Familial :
        # Si l'IA a mis une personne physique (ex: Sophie DUPONT ou sa fille) en SSIAD, HAD ou SAAD,
        # il s'agit d'un aidant familial et NON d'un organisme professionnel (un service SSIAD/SAAD n'est pas un prénom/nom d'une personne) !
        aid_nom = str(parsed.get("aidant_nom", "")).lower().strip()
        cleaned_cercle = []
        for pro in parsed.get("cercle_de_soins", []):
            pro_nom = str(pro.get("nom", "")).strip()
            pro_nom_lower = pro_nom.lower()
            pro_type = str(pro.get("type", "")).lower()

            is_personne_aidante = False
            if aid_nom and pro_nom_lower and (pro_nom_lower in aid_nom or aid_nom in pro_nom_lower):
                is_personne_aidante = True
            elif any(k in pro_nom_lower or k in pro_type for k in ["fille", "fils", "enfant", "mari", "épouse", "epouse", "conjoint", "aidant", "famille", "proche"]):
                is_personne_aidante = True
            elif pro_type in ["ssiad_had", "saad", "aide_a_domicile"] and pro_nom and not any(org in pro_nom_lower for org in ["ssiad", "saad", "had", "admr", "ccas", "asso", "service", "agence", "centre", "domus", "senior", "presence", "présence"]):
                # Si classé par erreur par le LLM en SSIAD/SAAD mais avec un nom de personne physique (ex: Sophie DUPONT)
                is_personne_aidante = True

            if is_personne_aidante:
                if not parsed.get("aidant_nom"):
                    parsed["aidant_nom"] = pro_nom
                    aid_nom = pro_nom_lower
                if not parsed.get("aidant_tel") and pro.get("tel"):
                    parsed["aidant_tel"] = pro.get("tel")
                # On ne l'ajoute pas aux services pros SSIAD/SAAD
                continue
            cleaned_cercle.append(pro)
        parsed["cercle_de_soins"] = cleaned_cercle
                
        # Fallback python pour les aides à domicile ratées par l'IA
        if not parsed.get("aide_1"):
            if "infirmi" in text_lower or "idel" in text_lower:
                freq = ""
                if "matin" in text_lower:
                    freq = " le matin"
                elif "soir" in text_lower:
                    freq = " le soir"
                elif "jour" in text_lower or "quotidien" in text_lower:
                    freq = " tous les jours"
                parsed["aide_1"] = f"Infirmière{freq}"
            
        # Toujours forcer la date d'émission au jour J
        parsed["emetteur_date"] = datetime.datetime.now().strftime("%d/%m/%Y")
        parsed["raw_text"] = raw_text
            
        return parsed
