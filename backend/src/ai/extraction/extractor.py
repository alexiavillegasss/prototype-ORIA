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
        self._excel_needs = self._load_excel_needs()

    def _load_comid_items(self):
        with open(self.comid_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data.get("items", [])

    def _load_excel_needs(self):
        try:
            import pandas as pd
            rules_dir = os.path.dirname(self.comid_path)
            excel_path = os.path.join(rules_dir, "tableau_oria.xlsx")
            df = pd.read_excel(excel_path, sheet_name="02_Besoins_x_structures (2)")
            needs = df["Besoin détaillé"].dropna().unique().tolist()
            return needs
        except Exception as e:
            print(f"Error loading needs from excel: {e}")
            return []

    async def extract(self, text: str):
        # Pseudonymisation du récit patient avant traitement
        safe_text = self.anonymizer.pseudonymize(text)

        # 1. PREMIER APPEL : EXTRACTION DES VARIABLES DE BASE
        prompt_base = f"""
### EXPERT ORIA - EXTRACTION DES VARIABLES CLÉS CLINIQUES ET ADMINISTRATIVES
Analyse la situation clinique ci-dessous pour extraire les variables clés sous forme de JSON.

SITUATION : "{safe_text}"

### DIRECTIVES D'EXTRACTION DE RIGUEUR CLINIQUE (ZERO-HALLUCINATION) :
1. "age" : Âge estimé ou mentionné de la personne (chiffre entier, ou null si non mentionné).
2. "ville" : Commune de résidence principale (ex: "Hyères", "Toulon", "La Valette", "La Valette-du-Var", "Sanary-sur-Mer", "La Seyne-sur-Mer", "La Garde", "Ollioules", ou null si non mentionné).
3. "apa" : Choisir "oui" si la personne bénéficie de l'APA. Choisir "non" si elle n'en bénéficie pas. Choisir "inconnu" si non mentionné.
4. "pch" : Choisir "oui" si bénéficie de la PCH, "non" si non, ou "inconnu" si non mentionné.
5. "gir" : Chiffre officiel de 1 à 6 si précisé (ex: "GIR 2", "GIR 3"), ou null si non précisé.
6. "medecin_traitant" : Choisir "identifie" si elle a un médecin traitant, "absent" si elle n'a plus de médecin ou cherche un médecin, ou "non_mentionne" si non mentionné dans le récit.
7. "malveillance" : Choisir impérativement une seule valeur :
   - "violences_physiques" s'il y a des ecchymoses suspectes, coups ou violences physiques SUBIS par l'usager de la part d'un tiers.
   - "spoliation_financiere" si vol, extorsion d'argent ou chantage par un proche.
   - "negligence" si privation volontaire de repas ou de soins par l'entourage.
   - "aucune" s'il n'y a aucune maltraitance active subie de la part d'un tiers.
   - EXCLUSION MAJEURE : Si l'usager lui-même est agressif, confus ou crie sur les soignants à cause de sa maladie, ce n'est PAS de la malveillance subie. De même, si l'usager se retrouve seul ou en difficulté parce que son conjoint ou aidant est hospitalisé ou absent, ce n'est PAS de la négligence ou de la malveillance subie (choisir "aucune").
   - PRIORITÉ : Si l'usager subit à la fois des violences physiques et du vol d'argent, choisissez "violences_physiques".
8. "urgence" : Choisir "critique" en cas d'agression physique active en cours ou détresse vitale médicale immédiate. Choisir "eleve" ou "modere" si situation tendue ou menaçante sans agression physique active. Choisir "faible" sinon.
9. "hospitalisation" : Choisir "en_cours" si actuellement hospitalisée, "recente" si sortie de l'hôpital depuis moins de 10 jours, ou "aucun" sinon.
 10. "besoin_principal" : Choisir la clé du besoin principal de l'usager parmi :
        - "aide_alimentaire" : pour le besoin 'Aide alimentaire' (dénutrition, frigo vide ou budget insuffisant pour manger).
        - "refus_de_soins" : pour le besoin 'Renoncement aux soins' (opposition active/hostile à la prise en charge ou aux soignants).
        - "maintien_a_domicile" : pour le besoin 'Besoin de mise en place ou d'adaptation des aides à domicile' (demande d'aide pour le ménage, la toilette, les repas, etc.).
        - "sortie_hospitalisation" : pour le besoin 'Retour à domicile après une hospitalisation'.
        - "recherche_medecin" : pour le besoin 'Recherche de médecin traitant'.
        - "secours_urgence" : pour le besoin 'Danger vital imminent ou agression physique active avec demande de secours d'urgence'.
        - "information_aides" : pour le besoin 'Information sur les aides'.
        - "evaluation_globale" : pour le besoin 'Évaluation globale / Évaluation médico-sociale' (difficultés cliniques/de vie sans demande précise).
        - "recherche_logement" : pour le besoin 'rechercher un logement'.
        - "indetermine" : si la situation est stable/suivi de routine (aucun besoin marquant), OU si au moins 2 besoins de même importance se chevauchent de manière complexe (la barrière étant trop fine ou trop complexe pour trancher).
 11. "professionnels_domicile" : Choisir "oui" si des professionnels (infirmiers, kinés, aides) passent régulièrement, ou "non" sinon.
 12. "aidant_regulier" : Choisir "oui" si présence régulière et stable d'un aidant familial, ou "non" sinon.
 13. "etat_logement" : Choisir "diogene" si syndrome de Diogène, "incurie" si logement très sale, "insalubre" si pas d'eau ou plafond menace de s'effondrer, "propre" si propre, ou "non_renseigne" sinon.
 14. "proposition_mail" : Rédiger un court brouillon d'e-mail professionnel (3-4 phrases maximum), écrit à la 3ème personne, prêt à être envoyé par le professionnel à la structure d'orientation pour résumer la situation et la demande. NE PAS INCLURE de formules de politesse ("Bonjour", "Cordialement"), générer uniquement le corps du texte.

### EXEMPLES DE CLASSIFICATION DU BESOIN PRINCIPAL :
- Exemple 1 : "M. Raymond, 82 ans, vit dans un grand dénuement. Son frigo est vide. Il refuse l'aide à domicile et refuse de prendre ses médicaments." 
  => "besoin_principal" doit être "indetermine" car il y a coexistence d'une situation d'Aide alimentaire critique ET d'un Besoin de mise en place ou d'adaptation des aides à domicile ET d'un Renoncement aux soins.
- Exemple 2 : "Mme Yvonne, 85 ans, stable, pas de demande d'aide ni de problème de santé ou financier."
  => "besoin_principal" doit être "indetermine".
- Exemple 3 : "M. Jean s'oppose activement aux pansements de l'infirmière."
  => "besoin_principal" doit être "refus_de_soins".

### DIRECTIVES DE CONFIANCE (TRÈS IMPORTANT) :
Pour chaque variable extraite ci-dessus, attribue un score de confiance (nombre entier de 0 à 100) dans l'objet "confiance_variables" :
- 100 : Si la donnée est mentionnée explicitement et sans ambiguïté dans le texte (ex: "79 ans", "Toulon", "déjà l'APA").
- 70 à 90 : Si la donnée est déduite logiquement avec une grande certitude à partir du contexte clinique ou sémantique.
- 40 à 69 : S'il y a de l'ambiguïté, du doute, ou des contradictions dans le récit.
- 0 : Si la donnée est totalement absente ou inconnue du récit (la variable correspondante est null, "inconnu" ou "non_renseigne").

Format JSON attendu :
{{
  "age": "Âge de l'usager (chiffre entier ou null)",
  "ville": "Nom de la ville de résidence (ou null)",
  "apa": "oui / non / en_cours / inconnu",
  "pch": "oui / non / en_cours / inconnu",
  "gir": "1 / 2 / 3 / 4 / 5 / 6 ou null",
  "professionnels_domicile": "oui / non / inconnu",
  "aidant_regulier": "oui / non / inconnu",
  "medecin_traitant": "identifie / absent / non_mentionne",
  "malveillance": "spoliation_financiere / violences_physiques / negligence / aucune",
  "urgence": "faible / modere / eleve / critique",
  "hospitalisation": "en_cours / recente / aucun",
  "besoin_principal": "aide_alimentaire / refus_de_soins / maintien_a_domicile / sortie_hospitalisation / recherche_medecin / secours_urgence / information_aides / evaluation_globale / recherche_logement / indetermine",
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
    "besoin_principal": "Score entier de 0 à 100",
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
7. **anxiete** : Doit être True si le texte mentionne explicitement que l'usager est anxieux ou très angoissé pour sa santé.
8. **douleurs** : Concerne uniquement les douleurs physiques chroniques (ex: souffre en permanence, arthrose douloureuse). Un risque de chute, une fatigue ou un malaise n'est pas une douleur.
9. **depression** : Concerne uniquement la dépression clinique (moral au plus bas, idées noires, ne veut plus vivre). Être angoissée suite à des violences n'est pas de la dépression.

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

Exemple :
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
        # Regex age extraction post-processing
        age = raw_data.get("age")
        if age is None or str(age).lower() in ["null", "none", "inconnu", "nan"]:
            import re
            age_match = re.search(r'(?:âgé\s+de\s+|âgée\s+de\s+|de\s+)?(\d{1,3})\s*ans', text, re.IGNORECASE)
            if age_match:
                age = int(age_match.group(1))

        # Regex city extraction post-processing
        ville = raw_data.get("ville")
        if ville is None or str(ville).lower() in ["null", "none", "inconnu", "nan"]:
            import re
            cities = ["toulon", "la seyne-sur-mer", "la seyne", "six-fours", "six fours", "bandol", "hyères", "hyeres", "la valette", "la valette-du-var", "sanary-sur-mer", "sanary", "la garde", "ollioules", "le pradet", "carqueiranne"]
            for city in cities:
                if re.search(r'\b' + re.escape(city) + r'\b', text, re.IGNORECASE):
                    if city in ["la seyne", "la seyne-sur-mer"]:
                        ville = "La Seyne-sur-Mer"
                    elif city in ["six fours", "six-fours"]:
                        ville = "Six-Fours"
                    elif city in ["la valette", "la valette-du-var"]:
                        ville = "La Valette-du-Var"
                    elif city in ["sanary", "sanary-sur-mer"]:
                        ville = "Sanary-sur-Mer"
                    elif city in ["la garde"]:
                        ville = "La Garde"
                    elif city in ["le pradet"]:
                        ville = "Le Pradet"
                    else:
                        ville = city.title()
                    break

        # Rapprochement flou ou direct de la clé de besoin principal extraite
        besoin_brut = raw_data.get("besoin_principal", raw_data.get("motif", "indetermine"))
        
        # Mapping de la clé courte vers le libellé de besoin Excel officiel
        key_to_excel = {
            "aide_alimentaire": "Aide alimentaire",
            "refus_de_soins": "Renoncement aux soins",
            "maintien_a_domicile": "Besoin de mise en place ou d'adaptation des aides à domicile",
            "sortie_hospitalisation": "Retour à domicile après une hospitalisation",
            "recherche_medecin": "Recherche de médecin traitant",
            "secours_urgence": "Danger vital imminent ou agression physique active avec demande de secours d'urgence",
            "information_aides": "Information sur les aides",
            "evaluation_globale": "Évaluation globale / Évaluation médico-sociale",
            "recherche_logement": "rechercher un logement",
            "indetermine": "indetermine"
        }
        
        besoin_principal = "indetermine"
        if besoin_brut in key_to_excel:
            besoin_principal = key_to_excel[besoin_brut]
        else:
            # Fallback en cas de libellé textuel direct ou flou
            import difflib
            import unicodedata
            
            def norm_str(s):
                s = str(s).strip().lower()
                s = s.replace("’", "'").replace("`", "'").replace("‘", "'")
                s = "".join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn')
                return " ".join(s.split())
                
            normalized_excel_needs = {norm_str(n): n for n in self._excel_needs}
            norm_b = norm_str(besoin_brut)
            if norm_b in normalized_excel_needs:
                besoin_principal = normalized_excel_needs[norm_b]
            else:
                closest = difflib.get_close_matches(norm_b, list(normalized_excel_needs.keys()), n=1, cutoff=0.6)
                if closest:
                    besoin_principal = normalized_excel_needs[closest[0]]

        # Mapping du besoin principal Excel vers le motif technique correspondant
        besoin_to_motif = {
            "Danger vital imminent ou agression physique active avec demande de secours d'urgence": "secours_urgence",
            "Violences physiques actives ou menacées": "secours_urgence",
            "Sécurité du domicile problématique, critique ou danger imminent": "secours_urgence",
            "Recherche de médecin traitant": "recherche_medecin",
            "Médecin traitant ne fait pas de visite à domicile": "recherche_medecin",
            "Mise en place d'aide à domicile": "maintien_a_domicile",
            "Besoin de mise en place ou d'adaptation des aides à domicile": "maintien_a_domicile",
            "Portage de repas": "maintien_a_domicile",
            "Mise en place de Téléalarme": "maintien_a_domicile",
            "Retour à domicile après une hospitalisation": "sortie_hospitalisation",
            "Retour à domicile après une hostitalisation ": "sortie_hospitalisation",
            "Information sur les aides": "information_aides",
            "évaluation globale / évaluation médico-sociale": "evaluation_globale",
            "Évaluation globale / Évaluation médico-sociale": "evaluation_globale",
            "rechercher un logement": "recherche_logement",
            "Aide alimentaire": "aide_alimentaire",
            "Besoin d'aide pour le paiement des factures": "aide_alimentaire",
            "Besoin d'évaluation d'une aide financière ponctuelle": "aide_alimentaire",
            "Secours d'urgence alimentaire ou financier": "aide_alimentaire",
            "Aide financière": "aide_alimentaire",
            "Renoncement aux soins": "refus_de_soins",
            "Accès aux soins": "refus_de_soins",
            "indetermine": "indetermine"
        }
        
        motif_principal = besoin_to_motif.get(besoin_principal, "indetermine")

        # Validation anti-hallucination de la suspicion de malveillance
        malveillance_val = str(raw_data.get("malveillance", "aucune")).lower()
        if malveillance_val != "aucune":
            has_violence_kw = re.search(r'\b(violence|violences|maltraitance|frappe|frapper|bleus?|coups?|menace|agression|agressions|abus|spoliation|vol|volé|vols|privation|danger)\b', text, re.IGNORECASE)
            if not has_violence_kw:
                malveillance_val = "aucune"

        mapped = {
            "usager.identite.age_estime": age,
            "usager.localisation.commune_residence": ville,
            "usager.situation_actuelle.APA": str(raw_data.get("apa", "non")).lower(),
            "usager.situation_actuelle.PCH": str(raw_data.get("pch", "non")).lower(),
            "usager.situation_actuelle.GIR": raw_data.get("gir"),
            "vulnerabilites.sante.suivi_medical.medecin_traitant": raw_data.get("medecin_traitant", "non_mentionne"),
            "usager.situation_actuelle.suspicion_malveillance": malveillance_val,
            "adresseur.degre_urgence_percu": raw_data.get("urgence", "faible"),
            "vulnerabilites.sante.hospitalisation.statut": raw_data.get("hospitalisation", "aucun"),
            "demande.motif_principal": motif_principal,
            "demande.besoin_principal": besoin_principal,
            "vulnerabilites.sante.professionnels_domicile": str(raw_data.get("professionnels_domicile", "inconnu")).lower(),
            "usager.cadre_de_vie.aidant_regulier": str(raw_data.get("aidant_regulier", "inconnu")).lower(),
            "usager.cadre_de_vie.etat_logement": raw_data.get("etat_logement", "non_renseigne"),
            "demande.proposition_mail": raw_data.get("proposition_mail", ""),
            "demande.resume_structuré": raw_data.get("raisonnement_expert", "")
        }

        # --- GESTION DE LA CONFIANCE DES VARIABLES DE BASE ---
        confiances_vars = raw_data.get("confiance_variables", {})
        base_vars = {
            "age": age,
            "ville": ville,
            "apa": raw_data.get("apa"),
            "pch": raw_data.get("pch"),
            "gir": raw_data.get("gir"),
            "professionnels_domicile": raw_data.get("professionnels_domicile"),
            "aidant_regulier": raw_data.get("aidant_regulier"),
            "medecin_traitant": raw_data.get("medecin_traitant"),
            "malveillance": raw_data.get("malveillance"),
            "urgence": raw_data.get("urgence"),
            "hospitalisation": raw_data.get("hospitalisation"),
            "motif": raw_data.get("besoin_principal"),
            "etat_logement": raw_data.get("etat_logement")
        }
        
        final_confiances_vars = {}
        for var, val in base_vars.items():
            if val is None or str(val).lower() in ["inconnu", "non_renseigne", "incertain"]:
                final_confiances_vars[var] = 0
            else:
                try:
                    conf_key = "besoin_principal" if var == "motif" else var
                    score = int(confiances_vars.get(conf_key, confiances_vars.get("motif", 100)))
                except:
                    score = 100
                if var in ["age", "ville"] and (raw_data.get(var) is None or str(raw_data.get(var)).lower() in ["null", "none", "inconnu", "nan"]):
                    score = 100
                final_confiances_vars[var] = min(max(score, 0), 100)
                
        mapped["evaluation.confiance.variables"] = final_confiances_vars

        # Mapping flexible (cherche dans "comid" ou à la racine)
        comid_data = raw_data.get("comid", raw_data)
        
        # 1. Extraction des codes positifs depuis une liste avec validation anti-hallucination stricte
        positive_codes = set()
        criteres_list = None
        if isinstance(comid_data, dict):
            if "criteres_presents" in comid_data:
                criteres_list = comid_data["criteres_presents"]
            elif "criteres" in comid_data:
                criteres_list = comid_data["criteres"]
        elif isinstance(comid_data, list):
            criteres_list = comid_data
            
        valid_criteres = []
        def clean_txt(t):
            return "".join(char.lower() for char in str(t) if char.isalnum())
        
        clean_text_original = clean_txt(text)
        
        if isinstance(criteres_list, list):
            for c in criteres_list:
                if isinstance(c, dict) and "code" in c:
                    code = str(c["code"]).strip().lower()
                    justification = c.get("justification", "")
                    
                    # Anti-hallucination : la justification doit exister dans le texte original
                    if justification and clean_txt(justification) in clean_text_original:
                        positive_codes.add(code)
                        valid_criteres.append(c)
                    elif not justification:
                        positive_codes.add(code)
                        valid_criteres.append(c)
                elif isinstance(c, str):
                    code = c.strip().lower()
                    positive_codes.add(code)
                    valid_criteres.append(c)
                    
        mapped["evaluation.comid.justifications"] = valid_criteres

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

        # --- LEXICAL OVERRIDES FOR COMID TO PREVENT LLM MISSES ---
        text_lower = text.lower() if text else ""
        overrides = {
            "psychiatrie": ["paranoia", "paranoïaque", "psychiatre", "CMP", "psychiatrique", "psychose", "schizophrène", "schizophrenie"],
            "depression": ["dépression", "depression", "dépressif", "depressif", "suicide", "suicidaire", "glissement"],
            "troubles_cognitifs": ["démence", "demence", "alzheimer", "mémoire", "memoire", "cognitif", "cognitive", "aphasie"],
            "addiction": ["alcool", "toxicoman", "toxico", "drogue", "addict", "trop de médicaments", "trop de medicaments", "doses qu'elle prend", "doses qu'il prend", "surdosage", "dépendance médicamenteuse", "dependance medicamenteuse", "antalgiques", "antidouleurs"],
            "degradation_recente": ["dégrade", "degrade", "dégradation", "degradation"],
            "perte_autonomie_recente": ["chute", "chutes", "perte d'autonomie", "perte d’autonomie", "perte autonomie"],
            "precarite_financiere": ["dette", "dettes", "surendettement", "surendetté", "surendette", "pas les moyens", "pas de moyens", "factures", "aide sociale à l'hébergement", "aide sociale a l'hebergement"],
            "isolement_social": ["seul", "seule", "isolé", "isole", "isolement"],
            "douleurs": ["douleur", "douleurs", "souffre", "souffrance", "chutes à répétition", "chutes repetees"]
        }
        
        # Épuisement aidant
        if "aidant" in text_lower or "épouse" in text_lower or "epouse" in text_lower or "femme" in text_lower or "mari" in text_lower:
            if any(w in text_lower for w in ["épuisé", "epuise", "épuisement", "epuisement", "bout", "fatigué", "fatigue"]):
                mapped["evaluation.comid.epuisement_aidant"] = True
                mapped["evaluation.confiance.comid"]["epuisement_aidant"] = 100
                
        for code, keywords in overrides.items():
            if any(w in text_lower for w in keywords):
                mapped[f"evaluation.comid.{code}"] = True
                mapped["evaluation.confiance.comid"][code] = 100

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

        # H. Force addiction si alcoolisme, alcool ou surdosage/dépendance médicamenteuse mentionné
        medication_addiction_kws = ["trop de médicaments", "trop de medicaments", "surdosage", "dépendance médicamenteuse", "dependance medicamenteuse", "doses qu'elle prend", "doses qu'il prend"]
        if "addiction à l'alcool" in text_lower or "alcoolisme" in text_lower or any(kw in text_lower for kw in medication_addiction_kws):
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

        # --- VALIDATIONS THÉMATIQUES SUPPLÉMENTAIRES (ANTI-EXTRAPOLATION DU LLM) ---
        # A. Multimorbidité : exige la mention d'au moins une pathologie
        if mapped.get("evaluation.comid.multimorbidite"):
            disease_keywords = [
                "diabète", "diabete", "hypertension", "hta", "cardiaque", "insuffisance", 
                "cancer", "arthrose", "alzheimer", "parkinson", "démence", "demence", 
                "dépression", "depression", "psychiatrique", "bpco", "pathologie", "maladie"
            ]
            if not any(kw in text_lower for kw in disease_keywords):
                mapped["evaluation.comid.multimorbidite"] = False
                if "multimorbidite" in mapped.get("evaluation.confiance.comid", {}):
                    mapped["evaluation.confiance.comid"]["multimorbidite"] = 0

        # B. Polymédication : exige la mention de médicaments
        if mapped.get("evaluation.comid.polymedication"):
            med_keywords = ["médicament", "medicament", "ordonnance", "traitement", "pilulier", "drogue", "médoc", "medoc"]
            if not any(kw in text_lower for kw in med_keywords):
                mapped["evaluation.comid.polymedication"] = False
                if "polymedication" in mapped.get("evaluation.confiance.comid", {}):
                    mapped["evaluation.confiance.comid"]["polymedication"] = 0

        # C. Troubles cognitifs : exige des mots-clés de cognition/mémoire
        if mapped.get("evaluation.comid.troubles_cognitifs"):
            cog_keywords = ["cognitif", "mémoire", "memoire", "oublie", "alzheimer", "démence", "demence", "perdu", "désorienté", "desoriente", "confusion", "cognitive"]
            if not any(kw in text_lower for kw in cog_keywords):
                mapped["evaluation.comid.troubles_cognitifs"] = False
                if "troubles_cognitifs" in mapped.get("evaluation.confiance.comid", {}):
                    mapped["evaluation.confiance.comid"]["troubles_cognitifs"] = 0

        # D. Épuisement de l'aidant : exige la mention de l'entourage
        if mapped.get("evaluation.comid.epuisement_aidant"):
            aidant_keywords = ["aidant", "fille", "fils", "épouse", "epouse", "mari", "conjoint", "proche", "famille", "frère", "soeur", "entourage"]
            if not any(kw in text_lower for kw in aidant_keywords):
                mapped["evaluation.comid.epuisement_aidant"] = False
                if "epuisement_aidant" in mapped.get("evaluation.confiance.comid", {}):
                    mapped["evaluation.confiance.comid"]["epuisement_aidant"] = 0

        # E. Perte d'autonomie récente : exige des mots-clés d'autonomie, chutes ou transferts physiques
        if mapped.get("evaluation.comid.perte_autonomie_recente"):
            autonomie_keywords = ["chute", "chuté", "chute", "tombe", "tombé", "autonomie", "paralysie", "fracture", "mobilité", "se lever", "marcher", "déplacement", "deplacement", "alité", "alitee", "fauteuil"]
            if not any(kw in text_lower for kw in autonomie_keywords):
                mapped["evaluation.comid.perte_autonomie_recente"] = False
                if "perte_autonomie_recente" in mapped.get("evaluation.confiance.comid", {}):
                    mapped["evaluation.confiance.comid"]["perte_autonomie_recente"] = 0

        # F. Nettoyage final des justifications COMID : on retire toutes les justifications invalidées ci-dessus
        if "evaluation.comid.justifications" in mapped and isinstance(mapped["evaluation.comid.justifications"], list):
            mapped["evaluation.comid.justifications"] = [
                j for j in mapped["evaluation.comid.justifications"]
                if isinstance(j, dict) and mapped.get(f"evaluation.comid.{j['code']}") is True
            ]

        return mapped
