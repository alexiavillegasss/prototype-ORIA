import json
import os
from infrastructure.llm_client import OllamaClient
from ai.security.anonymizer import Anonymizer

class SignalExtractor:
    last_extracted_data = None
    last_text = None

    def __init__(self, schema_path: str, comid_path: str, model="llama3", base_url="http://localhost:11434", temperature=0):
        self.client = OllamaClient(model=model, base_url=base_url)
        self.anonymizer = Anonymizer()
        self.schema_path = schema_path
        self.comid_path = comid_path
        self._comid_items = self._load_comid_items()

    def _load_comid_items(self):
        with open(self.comid_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data.get("items", [])

    async def extract(self, text: str):
        # Pseudonymisation du récit patient avant traitement
        safe_text = self.anonymizer.pseudonymize(text)

        # 1. PREMIER APPEL : EXTRACTION DES VARIABLES DE BASE
        prompt_base = f"""
### EXPERT ORIA - EXTRACTION DES VARIABLES CLÉS CLINIQUES ET ADMINISTRATIVES
Analyse la situation clinique ci-dessous pour extraire les variables clés sous forme de JSON.

SITUATION : "{safe_text}"

### DIRECTIVES D'EXTRACTION DE RIGUEUR CLINIQUE (ZERO-HALLUCINATION) :
1. "age" : Âge mentionné de la personne (chiffre entier, ou null si non mentionné). Être extrêmement attentif aux mentions d'âge formulées en clair (ex: "Monsieur de 55 ans", "patiente de 80 ans", "âgé de 77 ans"). Ne jamais extraire null si l'âge est présent dans le texte.
2. "ville" : Commune de résidence principale (ex: "Hyères", "Toulon", "La Valette", "La Valette-du-Var", "Sanary-sur-Mer", "La Seyne-sur-Mer", "La Garde", "Ollioules", ou null si non mentionné).
3. "apa" : Choisir "oui" si la personne bénéficie de l'APA. Choisir "non" si elle n'en bénéficie pas. Choisir "inconnu" si non mentionné.
4. "pch" : Choisir "oui" si bénéficie de la PCH, "non" si non, ou "inconnu" si non mentionné.
5. "gir" : Chiffre officiel de 1 à 6 si précisé (ex: "GIR 4", "GIR 2", "GIR 3"), ou null si non précisé. Rechercher attentivement les termes "GIR X" et ne pas renvoyer null si présents.
6. "medecin_traitant" : Choisir "identifie" si elle a un médecin traitant, "absent" si elle n'a plus de médecin ou cherche un médecin, ou "incertain" si non mentionné.
7. "malveillance" : Choisir impérativement une seule valeur :
   - "violences_physiques" s'il y a des ecchymoses suspectes, coups ou violences physiques SUBIS par l'usager de la part d'un tiers.
   - "spoliation_financiere" si vol, extorsion d'argent ou chantage par un proche.
   - "negligence" si privation volontaire de repas ou de soins par l'entourage.
   - "aucune" s'il n'y a aucune maltraitance active subie de la part d'un tiers.
   - EXCLUSION MAJEURE : Si l'usager lui-même est agressif, confus ou crie sur les soignants à cause de sa maladie, ce n'est PAS de la malveillance subie. De même, si l'usager se retrouve seul ou en difficulté parce que son conjoint ou aidant est hospitalisé ou absent, ce n'est PAS de la négligence ou de la malveillance subie (choisir "aucune").
   - PRIORITÉ : Si l'usager subit à la fois des violences physiques et du vol d'argent, choisissez "violences_physiques".
8. "urgence" : Choisir "critique" en cas d'agression physique active en cours ou détresse vitale médicale immédiate. Choisir "eleve" ou "modere" si situation tendue ou menaçante sans agression physique active. Choisir "faible" sinon.
9. "hospitalisation" : Choisir "en_cours" si actuellement hospitalisée, "recente" si sortie de l'hôpital depuis moins de 10 jours, ou "aucun" sinon.
10. "motif" : Choisir le motif principal parmi :
    - "evaluation_globale" si le récit décrit simplement des difficultés cliniques ou de vie (ex: confusion, oublis, fatigue, perte d'autonomie, isolement) sans demande explicite d'aide, sans refus de soins, sans sortie d'hôpital et sans situation d'urgence. C'est la valeur par défaut pour les signalements descriptifs généraux.
    - "refus_de_soins" uniquement en cas d'opposition active, hostile ou de refus explicite et généralisé de se soigner ou de recevoir les professionnels. Si un patient refuse uniquement l'accueil de jour mais accepte d'autres aides à domicile, ce n'est PAS un refus de soins.
    - "refus_aide_domicile" uniquement si l'usager lui-même s'oppose activement à l'aide à domicile.
    - "sortie_hospitalisation" si retour à domicile post-hospitalisation récente.
    - "aide_alimentaire" si dénutrition sévère, frigo vide sans ressources, ou si la personne demande de l'aide pour s'acheter à manger ou faire ses courses par manque d'argent.
    - "secours_urgence" si danger vital imminent ou agression physique en cours.
    - "recherche_medecin" si recherche active de médecin traitant (ex: médecin à la retraite).
    - "maintien_a_domicile" si demande générale d'aide à domicile pour rester chez soi (ex: aides professionnelles, auxiliaire, portage de repas), ou adaptation d'équipement.
    - "logement" si la demande concerne principalement une recherche de logement social, d'hébergement d'urgence, d'entrée en EHPAD, de résidence autonomie ou de relogement.
    - "aide_administrative" si la demande concerne principalement l'aide pour des dossiers administratifs, de droits sociaux, d'aide sociale à l'hébergement (ASH), de renouvellement MDPH ou de mesures de protection.
    - "information_aides" si demande générale d'informations.
11. "professionnels_domicile" : Choisir "oui" si des professionnels (infirmiers, kinés, aides) passent régulièrement, ou "non" sinon.
12. "aidant_regulier" : Choisir "oui" si présence régulière et stable d'un aidant familial, ou "non" sinon.
13. "etat_logement" : Choisir "diogene" uniquement en cas de syndrome de Diogène avéré ou mentionné explicitement. Choisir "incurie" si le logement est décrit comme très sale, insalubre ou mal entretenu. Choisir "propre" si propre, ou "non_renseigne" sinon.
14. "proposition_mail" : Rédiger un court brouillon d'e-mail professionnel (3-4 phrases maximum), écrit à la 3ème personne, prêt à être envoyé par le professionnel à la structure d'orientation pour résumer la situation et la demande. NE PAS INCLURE de formules de politesse ("Bonjour", "Cordialement"), générer uniquement le corps du texte.

### EXEMPLES D'EXTRACTION CLINIQUE :

Exemple 1 :
SITUATION : "Bonjour, je suis infirmière libérale à Toulon. Je prends en charge un patient de 80 ans qui vit avec son épouse. Monsieur est en refus de soins, chutes à répétition, son épouse est épuisée. Pas d'APA."
JSON attendu :
{{
  "age": 80,
  "ville": "Toulon",
  "apa": "non",
  "pch": "inconnu",
  "gir": null,
  "professionnels_domicile": "oui",
  "aidant_regulier": "oui",
  "medecin_traitant": "identifie",
  "malveillance": "aucune",
  "urgence": "faible",
  "hospitalisation": "aucun",
  "motif": "refus_de_soins",
  "etat_logement": "propre",
  "raisonnement_expert": "Patient de 80 ans à Toulon, en refus de soins et sujet à des chutes répétées, avec épuisement de l'aidant (épouse).",
  "proposition_mail": "Monsieur, âgé de 80 ans et vivant à Toulon, présente une dégradation physique marquée par des chutes à répétition et refuse les soins prescrits. Son épouse, qui l'accompagne au quotidien, est épuisée. Nous sollicitons votre intervention pour une évaluation globale et un soutien à domicile.",
  "confiance_variables": {{
    "age": 100,
    "ville": 100,
    "apa": 100,
    "pch": 0,
    "gir": 0,
    "professionnels_domicile": 100,
    "aidant_regulier": 100,
    "medecin_traitant": 80,
    "malveillance": 90,
    "urgence": 90,
    "hospitalisation": 90,
    "motif": 100,
    "etat_logement": 80
  }}
}}

Exemple 2 :
SITUATION : "Je suis la sœur d’un homme de 44 ans, vivant à six fours, il a besoin d’un accompagnement pour des démarches administratives et une demande de logement social suite à la perte d’autonomie en lien avec un accident."
JSON attendu :
{{
  "age": 44,
  "ville": "Six-Fours",
  "apa": "inconnu",
  "pch": "inconnu",
  "gir": null,
  "professionnels_domicile": "non",
  "aidant_regulier": "non",
  "medecin_traitant": "incertain",
  "malveillance": "aucune",
  "urgence": "faible",
  "hospitalisation": "aucun",
  "motif": "logement",
  "etat_logement": "non_renseigne",
  "raisonnement_expert": "Patient de 44 ans à Six-Fours demandant un accompagnement social pour un logement social et des démarches administratives.",
  "proposition_mail": "Monsieur, âgé de 44 ans et habitant à Six-Fours, a perdu son autonomie suite à un accident. Sa sœur sollicite notre accompagnement pour l'aider dans ses démarches administratives et formuler une demande de logement social adapté.",
  "confiance_variables": {{
    "age": 100,
    "ville": 100,
    "apa": 0,
    "pch": 0,
    "gir": 0,
    "professionnels_domicile": 80,
    "aidant_regulier": 80,
    "medecin_traitant": 0,
    "malveillance": 90,
    "urgence": 95,
    "hospitalisation": 95,
    "motif": 100,
    "etat_logement": 0
  }}
}}

Format JSON attendu :
{{
  "age": "Âge de l'usager (chiffre entier ou null)",
  "ville": "Nom de la ville de résidence (ou null)",
  "apa": "oui / non / en_cours / inconnu",
  "pch": "oui / non / en_cours / inconnu",
  "gir": "1 / 2 / 3 / 4 / 5 / 6 ou null",
  "professionnels_domicile": "oui / non / inconnu",
  "aidant_regulier": "oui / non / inconnu",
  "medecin_traitant": "identifie / absent / incertain",
  "malveillance": "spoliation_financiere / violences_physiques / negligence / aucune",
  "urgence": "faible / modere / eleve / critique",
  "hospitalisation": "en_cours / recente / aucun",
  "motif": "evaluation_globale / refus_de_soins / sortie_hospitalisation / aide_alimentaire / secours_urgence / recherche_medecin / maintien_a_domicile / logement / aide_administrative / information_aides / refus_aide_domicile",
  "etat_logement": "diogene / incurie / insalubre / propre / non_renseigne",
  "raisonnement_expert": "Résumé court et raisonnement clinique",
  "proposition_mail": "Brouillon du mail de demande d'orientation",
  "confiance_variables": {{
    "age": "Score entier de 0 à 100",
    "ville": "Score entier de 0 à 100",
    "apa": "Score entier de 0 à 100",
    "pch": "Score entier de 0 à 100",
    "gir": "Score entier de 0 à 100",
    "professionnels_domicile": "Score entier de 0 à 100",
    "aidant_regulier": "Score entier de 0 à 100",
    "medecin_traitant": "Score entier de 0 à 100",
    "malveillance": "Score entier de 0 à 100",
    "urgence": "Score entier de 0 à 100",
    "hospitalisation": "Score entier de 0 à 100",
    "motif": "Score entier de 0 à 100",
    "etat_logement": "Score entier de 0 à 100"
  }}
}}
"""
        raw_base = await self.client.generate_json(prompt_base)

        # 2. DEUXIÈME APPEL : ÉVALUATION DES CRITÈRES COMID
        comid_reference = ""
        for item in self._comid_items:
            # Ne pas inclure les exemples pour éviter les fuites d'exemples dans les justifications
            comid_reference += f"- {item['label']} (Code: `{item['code']}`)\n"

        prompt_comid = f"""
### EXPERT ORIA - ÉVALUATION DES CRITÈRES COMID
Analyse la situation ci-dessous pour identifier les critères cliniques et médico-sociaux du référentiel COMID qui s'appliquent à l'usager.

SITUATION : "{safe_text}"

### LISTE DES CRITÈRES COMID DISPONIBLES :
{comid_reference}

### DIRECTIVES D'ÉVALUATION ET DE JUSTIFICATION CLINIQUE :
Vous devez retourner uniquement les critères COMID qui sont présents de manière logique et factuelle sous la forme d'un tableau JSON nommé "criteres_presents".
- Pour chaque critère considéré comme présent, indiquez son code et justifiez par une preuve textuelle sous forme d'une CITATION EXACTE (de 2 à 7 mots consécutifs tirée directement de la SITUATION sans modification ni paraphrase).
- Les citations justificatives doivent décrire l'état de l'USAGER lui-même, et non les sentiments ou les difficultés de l'intervenant/professionnel qui signale le cas (ex: "Je suis perdue" décrit l'infirmière, pas le patient. Donc `anxiete` doit rester False pour le patient).
- Soyez extrêmement factuel : si un critère n'est pas applicable et n'est pas mentionné, ne l'incluez pas.
- ATTENTION AUX SYNONYMES ÉVIDENTS : Associez les expressions équivalentes (ex: "perdre la tête" ou "oublis fréquents" ➡️ `troubles_cognitifs` ; "chute" ou "ne peut plus se lever" ➡️ `perte_autonomie_recente` ; "très angoissée" ➡️ `anxiete`).
- Pour chaque critère présent, ajoutez un score de confiance (nombre entier de 0 à 100) :
  - 95 à 100 : Si le critère est justifié par une citation mot à mot évidente.
  - 70 à 90 : Si le critère est basé sur un synonyme évident ou déduction forte.
  - 40 à 69 : S'il y a un doute important sur l'implication ou la présence.

### EXCLUSIONS ET RESTRICTIONS CLINIQUES REQUISES (TRÈS IMPORTANT) :
1. **multimorbidite** : Ne marquez ce critère à True QUE si le récit mentionne explicitement au moins 3 pathologies chroniques distinctes (ex: diabète + hypertension + insuffisance rénale). Avoir 1 ou 2 maladies (ex: diabète + hypertension, ou Parkinson seul), ou être âgé/vulnérable/agressif, n'est JAMAIS de la multimorbidité.
2. **litteratie_faible** : Concerne exclusivement l'incompréhension des consignes, l'illettrisme ou la barrière de la langue. La perte d'autonomie physique ou visuelle (ex: ne plus pouvoir préparer ses repas ou prendre ses médicaments) ne doit JAMAIS être qualifiée de faible littératie.
3. **epuisement_aidant** : S'applique uniquement si un aidant familial régulier montre des signes de fatigue ou est indisponible (hospitalisé). Si un proche est violent, agressif, crie ou vole de l'argent (spoliation), c'est de la maltraitance active et non de l'épuisement d'aidant.
4. **logement_inadapte** : Concerne uniquement l'inadaptation physique du logement (ex: 3ème étage sans ascenseur, insalubrité). Des difficultés financières pour payer les factures d'énergie ou le loyer ne rendent pas le logement physiquement inadapté.
5. **degradation_recente** : Concerne uniquement une dégradation brutale de l'état de santé physique ou psychique depuis moins d'un mois. Un découvert bancaire récent ou un impayé n'est pas une dégradation de santé.
6. **sollicitations_recurrentes** : Doit être True si l'usager appelle plusieurs fois par jour les professionnels (ex: cabinet infirmier) ou ses proches.
10. **psychiatrie** : Doit être True si l'usager présente des pathologies, diagnostics ou des troubles psychiatriques mentionnés dans le texte (ex: schizophrénie, bipolarité, psychose, paranoïa, comportement paranoïaque, délires, hallucinations, suivi psychiatrique).
11. **addiction** : Doit être True si l'usager a une dépendance ou une consommation excessive d'alcool, de drogues ou de médicaments (ex: consomme beaucoup d'alcool, état d'ébriété, éthylisme, ancien toxicomane, alcoolisme).
12. **anxiete** : Doit être True si le texte mentionne explicitement que l'usager est anxieux ou très angoissé pour sa santé.
13. **douleurs** : Concerne uniquement les douleurs physiques chroniques (ex: souffre en permanence, arthrose douloureuse). Un risque de chute, une fatigue ou un malaise n'est pas une douleur.
14. **depression** : Concerne uniquement la dépression clinique (moral au plus bas, idées noires, ne veut plus vivre). Être angoissée suite à des violences n'est pas de la dépression.

Format JSON attendu :
{{
  "criteres_presents": [
    {{
      "code": "code_du_critere_present_1",
      "justification": "Citation mot à mot ou synonyme direct prouvant la présence",
      "confiance": 95
    }}
  ]
}}

Exemples :
Exemple 1 :
SITUATION : "Mme A. de 80 ans vit seule. Elle oublie de manger et a fait une chute hier."
JSON attendu :
{{
  "criteres_presents": [
    {{
      "code": "troubles_cognitifs",
      "justification": "oublie de manger",
      "confiance": 95
    }},
    {{
      "code": "perte_autonomie_recente",
      "justification": "a fait une chute hier",
      "confiance": 95
    }}
  ]
}}

Exemple 2 :
SITUATION : "Mme X., 65 ans, vit seule dans un logement social. Elle consomme beaucoup d'alcool et se retrouve nue dehors. Son appartement est insalubre."
JSON attendu :
{{
  "criteres_presents": [
    {{
      "code": "addiction",
      "justification": "consomme beaucoup d'alcool",
      "confiance": 100
    }},
    {{
      "code": "psychiatrie",
      "justification": "nue dehors",
      "confiance": 95
    }}
  ]
}}
"""
        raw_comid = await self.client.generate_json(prompt_comid)

        # Fusion des résultats
        raw_result = {**raw_base}
        raw_result["comid"] = raw_comid
        
        print("\n--- DEBUG : ANALYSE EXPERTE ---")
        print(raw_result.get("raisonnement_expert", "Analyse manquante"))
        print(f"Ville extraite : {raw_result.get('ville')}")
        print(f"Médecin : {raw_result.get('medecin_traitant')}")
        print(f"Malveillance : {raw_result.get('malveillance')}")
        print(f"Hospitalisation : {raw_result.get('hospitalisation')}")
        print(f"État Logement : {raw_result.get('etat_logement')}")
        print("--- FIN DEBUG ---\n")
        
        result = self._map_to_schema(raw_result, text)
        SignalExtractor.last_extracted_data = result
        SignalExtractor.last_text = text
        return result

    def _map_to_schema(self, raw_data: dict, text: str = ""):
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
            "usager.cadre_de_vie.etat_logement": raw_data.get("etat_logement", "non_renseigne"),
            "demande.proposition_mail": raw_data.get("proposition_mail", ""),
            "demande.resume_structuré": raw_data.get("raisonnement_expert", "")
        }

        # --- GESTION DE LA CONFIANCE DES VARIABLES DE BASE ---
        confiances_vars = raw_data.get("confiance_variables", {})
        base_vars = {
            "age": raw_data.get("age"),
            "ville": raw_data.get("ville"),
            "apa": raw_data.get("apa"),
            "pch": raw_data.get("pch"),
            "gir": raw_data.get("gir"),
            "professionnels_domicile": raw_data.get("professionnels_domicile"),
            "aidant_regulier": raw_data.get("aidant_regulier"),
            "medecin_traitant": raw_data.get("medecin_traitant"),
            "malveillance": raw_data.get("malveillance"),
            "urgence": raw_data.get("urgence"),
            "hospitalisation": raw_data.get("hospitalisation"),
            "motif": raw_data.get("motif"),
            "etat_logement": raw_data.get("etat_logement")
        }
        
        final_confiances_vars = {}
        for var, val in base_vars.items():
            if val is None or str(val).lower() in ["inconnu", "non_renseigne", "incertain"]:
                final_confiances_vars[var] = 0
            else:
                try:
                    score = int(confiances_vars.get(var, 100))
                except:
                    score = 100
                final_confiances_vars[var] = min(max(score, 0), 100)
                
        mapped["evaluation.confiance.variables"] = final_confiances_vars

        # Mapping flexible (cherche dans "comid" ou à la racine)
        comid_data = raw_data.get("comid", raw_data)
        
        # 1. Extraction des codes positifs depuis une liste
        positive_codes = set()
        criteres_list = None
        if isinstance(comid_data, dict):
            if "criteres_presents" in comid_data:
                criteres_list = comid_data["criteres_presents"]
            elif "criteres" in comid_data:
                criteres_list = comid_data["criteres"]
        elif isinstance(comid_data, list):
            criteres_list = comid_data
            
        if isinstance(criteres_list, list):
            for c in criteres_list:
                if isinstance(c, dict) and "code" in c:
                    positive_codes.add(str(c["code"]).strip().lower())
                elif isinstance(c, str):
                    positive_codes.add(c.strip().lower())
        mapped["evaluation.comid.justifications"] = criteres_list if isinstance(criteres_list, list) else []

        # --- GESTION DE LA CONFIANCE DES CRITÈRES COMID ---
        comid_confiances = {}
        if isinstance(criteres_list, list):
            for c in criteres_list:
                if isinstance(c, dict) and "code" in c:
                    code = str(c["code"]).strip().lower()
                    try:
                        conf = int(c.get("confiance", 100))
                    except:
                        conf = 100
                    comid_confiances[code] = min(max(conf, 0), 100)
        mapped["evaluation.confiance.comid"] = comid_confiances

        # 2. Remplissage des items COMID
        for item in self._comid_items:
            code = item["code"]
            
            # Si le code est présent dans notre ensemble positif extrait
            if code in positive_codes:
                is_positive = True
            else:
                # Sinon, recherche classique par clé directe
                val = comid_data.get(code) if isinstance(comid_data, dict) else None
                if isinstance(val, dict):
                    val = val.get("presence")
                
                is_positive = False
                if isinstance(val, bool):
                    is_positive = val
                elif isinstance(val, str):
                    is_positive = val.lower() in ["oui", "yes", "true", "o", "1"]
            
            mapped[f"evaluation.comid.{code}"] = is_positive

        # --- RÈGLES DE SÉCURITÉ MÉTIER HYBRIDES & REDONDANCES LOGIQUES ---
        text_lower = text.lower() if text else ""

        # A. Force APA si mentionné explicitement dans le texte original
        if "déjà l'apa" in text_lower or "a l'apa" in text_lower or "bénéficie de l'apa" in text_lower:
            mapped["usager.situation_actuelle.APA"] = "oui"
            mapped["evaluation.confiance.variables"]["apa"] = 100

        # B. Force logement inadapté si l'état du logement est insalubre/diogène/incurie
        if mapped.get("usager.cadre_de_vie.etat_logement") in ["insalubre", "diogene", "incurie"]:
            mapped["evaluation.comid.logement_inadapte"] = True
            mapped["evaluation.confiance.comid"]["logement_inadapte"] = 100

        # C. Force opposition aux soins si le motif principal est le refus de soins ou d'aide
        if mapped.get("demande.motif_principal") in ["refus_de_soins", "refus_aide_domicile"]:
            mapped["evaluation.comid.opposition_soins"] = True
            # Si le critère n'a pas été détecté via citation par le LLM (confiance manquante),
            # on lui affecte une confiance de 0% pour indiquer l'absence de preuve textuelle.
            if "opposition_soins" not in mapped.get("evaluation.confiance.comid", {}):
                mapped["evaluation.confiance.comid"]["opposition_soins"] = 0

        # D. Force transition de parcours si hospitalisation récente et motif de sortie d'hôpital
        if mapped.get("vulnerabilites.sante.hospitalisation.statut") == "recente" and mapped.get("demande.motif_principal") == "sortie_hospitalisation":
            mapped["evaluation.comid.transition_parcours"] = True
            mapped["evaluation.confiance.comid"]["transition_parcours"] = 100

        # E. Force lourdeur réseau si suspicion de malveillance avérée
        if mapped.get("usager.situation_actuelle.suspicion_malveillance") != "aucune":
            mapped["evaluation.comid.lourdeur_reseau"] = True
            mapped["evaluation.confiance.comid"]["lourdeur_reseau"] = 100

        # F. Force isolement social si pas d'aidant régulier et isolement relationnel critique
        if mapped.get("usager.cadre_de_vie.aidant_regulier") == "non" and mapped.get("vulnerabilites.social.isolement_relationnel") == "critique":
            mapped["evaluation.comid.isolement_social"] = True
            mapped["evaluation.confiance.comid"]["isolement_social"] = 100

        # G. Force multimorbidité si "polypathologie" mentionnée ET qu'une autre pathologie est extraite
        # Pour éviter de forcer sur M. Pierre qui n'a qu'une seule maladie listée en plus du mot-clé
        if "polypathologie" in text_lower or "polypathologique" in text_lower:
            if len(positive_codes) > 1 or (len(positive_codes) == 1 and "multimorbidite" not in positive_codes):
                mapped["evaluation.comid.multimorbidite"] = True
                mapped["evaluation.confiance.comid"]["multimorbidite"] = 100

        # H. Force addiction si alcoolisme ou alcool mentionné de manière négative
        if "addiction à l'alcool" in text_lower or "alcoolisme" in text_lower:
            mapped["evaluation.comid.addiction"] = True
            mapped["evaluation.confiance.comid"]["addiction"] = 100

        # I. Sécurité Épuisement de l'aidant : si suspicion de malveillance active par un proche (agression, vol),
        # l'agresseur ne doit pas être considéré comme un aidant épuisé
        if mapped.get("usager.situation_actuelle.suspicion_malveillance") in ["spoliation_financiere", "violences_physiques"]:
            mapped["evaluation.comid.epuisement_aidant"] = False
            if "epuisement_aidant" in mapped["evaluation.confiance.comid"]:
                mapped["evaluation.confiance.comid"]["epuisement_aidant"] = 0

        # Cas particulier pour l'isolement (vulnerabilites.social.isolement_relationnel)
        if mapped.get("evaluation.comid.isolement_social") or raw_data.get("seule") == "oui":
            mapped["vulnerabilites.social.isolement_relationnel"] = "critique"
        else:
            mapped["vulnerabilites.social.isolement_relationnel"] = None

        return mapped
