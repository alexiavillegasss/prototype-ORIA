import json
import os
from infrastructure.llm_client import OllamaClient

class SignalExtractor:
    last_extracted_data = None
    last_text = None

    def __init__(self, schema_path: str, comid_path: str, model="llama3", base_url="http://localhost:11434", temperature=0.1):
        self.client = OllamaClient(model=model, base_url=base_url, temperature=temperature)
        self.schema_path = schema_path
        self.comid_path = comid_path
        self._comid_items = self._load_comid_items()

    def _load_comid_items(self):
        with open(self.comid_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data.get("items", [])

    async def extract(self, text: str):
        # 1. PREMIER APPEL : EXTRACTION DES VARIABLES DE BASE
        prompt_base = f"""
### EXPERT ORIA - EXTRACTION DES VARIABLES CLÉS CLINIQUES ET ADMINISTRATIVES
Analyse la situation clinique ci-dessous pour extraire les variables clés sous forme de JSON.

SITUATION : "{text}"

### DIRECTIVES D'EXTRACTION DE RIGUEUR CLINIQUE (ZERO-HALLUCINATION) :
1. "age" : Âge estimé ou mentionné de la personne (chiffre entier, ou null si non mentionné).
2. "ville" : Commune de résidence principale (ex: "Hyères", "Toulon", "Sanary-sur-Mer", "La Seyne-sur-Mer", "La Garde", "Ollioules", ou null si non mentionné).
3. "apa" : Choisir "oui" si le texte mentionne explicitement que la personne en bénéficie déjà (ex: "Elle a déjà l'APA", "On a déjà l'APA"). Choisir "non" si le texte mentionne ou sous-entend explicitement qu'elle n'en bénéficie pas (ex: "Elle n'a pas l'APA"), OU si la personne est décrite comme autonome sans dépendance (ex: fuite active, pas de perte d'autonomie/GIR mentionnée). Choisir "inconnu" s'il y a un besoin d'aide ou de maintien à domicile décrit (perte d'autonomie) mais que le statut de l'APA n'est pas du tout précisé.
4. "pch" : Choisir "oui" si bénéficie de la PCH, "non" si non, ou "inconnu" si non mentionné.
5. "gir" : Chiffre officiel de 1 à 6 si précisé (ex: "GIR 2", "GIR 3"), ou null si non précisé.
6. "medecin_traitant" : Choisir "identifie" si elle a un médecin, "absent" si elle n'a plus de médecin depuis des mois ou cherche un médecin, ou "incertain" si non mentionné.
7. "malveillance" : Choisir impérativement :
   - "spoliation_financiere" si un tiers (fils, petit-fils, proche, etc.) lui vole, extorque, prend son argent, ou s'il lui demande de l'argent de façon très insistante (ex: fils agressif qui crie et demande de l'argent de façon très insistante à sa mère alors qu'elle semble terrorisée).
   - "violences_physiques" si coups, ecchymoses suspectes ou sévices physiques SUBIS de la part d'un tiers.
   - "negligence" si l'entourage délaisse volontairement la personne (privation volontaire d'hygiène/repas).
   - "aucune" s'il n'y a aucune maltraitance active commise par un tiers.
   - EXCLUSIONS MAJEURES :
     * Si l'usager lui-même est confus, crie ou est agressif envers les soignants à cause de sa maladie (démence, diabète), ce n'est PAS de la malveillance subie. Mets "aucune".
     * Si l'usager se retrouve seul ou en difficulté car son conjoint/aidant est hospitalisé ou absent, ce n'est PAS de la malveillance ou de la négligence. Mets "aucune".
8. "urgence" : Choisir "critique" s'il y a une agression physique active et en cours (en train de se produire), ou si l'usager a dû fuir/quitter son domicile en urgence suite à des violences physiques graves et a besoin d'une protection immédiate, ou s'il y a un danger vital médical immédiat nécessitant les secours (arrêt cardiaque, incendie). Si la situation est précaire ou menaçante mais que l'usager est à l'abri à domicile sans agression physique active en cours, choisir "eleve" ou "modere".
9. "hospitalisation" : Choisir "en_cours" si la personne est actuellement hospitalisée ou admise à l'hôpital. Choisir "recente" si elle est sortie de l'hôpital depuis moins de 10 jours. Choisir "aucun" sinon.
   - EXCLUSION CRITIQUE : Si le CONJOINT ou l'AIDANT de l'usager est hospitalisé mais que l'usager lui-même reste à domicile, l'hospitalisation de l'usager est "aucun".
10. "motif" : Choisir impérativement le motif principal :
    - "refus_de_soins" uniquement si la personne refuse activement de manière hostile d'ouvrir sa porte aux soignants/aides, s'oppose aux soins, ou dit expressément qu'elle n'en veut pas. Les oublis de médicaments dus à des troubles cognitifs ou de la mémoire ne sont PAS du refus de soins. De plus, si le cas décrit des maltraitances (spoliation, cris, violence, chantage) commises par un fils ou proche et signalées par un tiers (kiné, médecin, assistante sociale), le motif principal est "secours_urgence" ou "maintien_a_domicile" et JAMAIS "refus_de_soins".
    - "sortie_hospitalisation" si la demande concerne l'organisation de sa sortie d'hôpital ou le retour/maintien à domicile post-hospitalisation (récente de moins d'un mois, ex: suite AVC récent il y a 3 semaines).
    - "aide_alimentaire" si elle n'a plus rien à manger.
    - "secours_urgence" uniquement en cas d'agression physique active en cours (coups en train d'être portés), d'incendie, de détresse vitale médicale immédiate (arrêt cardiaque), ou de fuite active du domicile en cours pour échapper à des violences physiques graves. Pour des menaces (mêmes physiques) d'un propriétaire ou marchand de sommeil, ou pour l'insalubrité du logement, choisissez impérativement "maintien_a_domicile".
    - "recherche_medecin" si recherche active de médecin traitant.
    - "maintien_a_domicile" si demande générale d'aide à domicile pour rester chez soi, ou si la situation concerne de l'insalubrité, un litige/menace de propriétaire, ou un besoin d'adaptation du logement. EXCLUSION CRITIQUE : Si la situation fait suite à une hospitalisation récente ou un AVC récent (moins d'un mois, ex: AVC il y a 3 semaines), choisissez impérativement "sortie_hospitalisation" au lieu de "maintien_a_domicile".
    - "information_aides" si demande générale d'informations sur les aides.
11. "professionnels_domicile" : Choisir "oui" si des infirmiers, kinés ou aides passent régulièrement à domicile. Choisir "non" ou "inconnu" sinon.
12. "aidant_regulier" : Choisir "oui" si elle a un conjoint ou un enfant aidant très disponible et présent au quotidien. Choisir "non" si elle vit seule, est très isolée ou n'a pas d'aidant régulier stable.
13. "etat_logement" : Choisir "diogene" si syndrome de Diogène (appartement insalubre encombré de déchets et d'objets accumulés). Choisir "incurie" si logement très sale sans accumulation. Choisir "non_renseigne" si absolument aucune information n'est fournie sur l'état de son logement.

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
  "motif": "refus_de_soins / sortie_hospitalisation / aide_alimentaire / secours_urgence / recherche_medecin / maintien_a_domicile / information_aides / refus_aide_domicile",
  "etat_logement": "diogene / incurie / insalubre / propre / non_renseigne",
  "raisonnement_expert": "Résumé court et raisonnement clinique"
}}
"""
        raw_base = await self.client.generate_json(prompt_base)

        # 2. DEUXIÈME APPEL : ÉVALUATION DES CRITÈRES COMID
        comid_reference = ""
        for item in self._comid_items:
            exemples = f" (Exemples: {', '.join(item['exemples'])})" if 'exemples' in item else ""
            comid_reference += f"- {item['label']} (Code: `{item['code']}`){exemples}\n"

        prompt_comid = f"""
### EXPERT ORIA - ÉVALUATION DES CRITÈRES COMID (ZÉRO-HALLUCINATION)
Analyse la situation ci-dessous pour identifier uniquement les critères cliniques et médico-sociaux du référentiel COMID qui sont présents avec une certitude absolue.

SITUATION : "{text}"

### LISTE DES CRITÈRES COMID DISPONIBLES :
{comid_reference}

### DIRECTIVES DE RIGUEUR ET DE JUSTIFICATION CLINIQUE :
Vous devez retourner uniquement un JSON contenant les codes des critères COMID qui sont explicitement et indubitablement présents dans la situation.
- Pour chaque critère que vous considérez comme présent, vous devez impérativement justifier sa présence par une courte phrase citant ou s'appuyant rigoureusement sur le texte.
- Si un critère n'est pas mentionné, s'il y a le moindre doute, ou s'il n'est pas présent, vous ne devez PAS l'inclure dans le JSON (il restera à false).
- Ne faites aucune supposition ou extrapolation. Ne devinez pas.

DIRECTIVES SPÉCIFIQUES POUR ÉVITER LES HALLUCINATIONS COURANTES :
1. "multimorbidite" : DANGER D'HALLUCINATION ! N'inclure que si l'usager souffre de STRICTEMENT PLUS de 2 maladies chroniques distinctes (c'est-à-dire 3 maladies ou plus, par exemple : diabète + hypertension + insuffisance rénale). Si le texte ne mentionne qu'une seule maladie (ex: hypertension uniquement, ou arthrose uniquement), ou deux maladies seulement, laissez rigoureusement ABSENT.
2. "opposition_soins" : DANGER D'HALLUCINATION ! Inclure uniquement si l'usager lui-même s'oppose ou refuse activement et avec hostilité les soins ou l'entrée des intervenants à domicile (ex: refuse d'ouvrir la porte, déclare hostilement qu'il ne veut pas d'aide). Être confus ou victime passive d'une agression physique ou d'une maltraitance sans refus d'aide caractérisé n'est PAS de l'opposition aux soins. Laissez rigoureusement ABSENT sinon.
3. "agressivite" : DANGER D'HALLUCINATION ! Inclure uniquement si l'usager lui-même se montre agressif, hostile, crie ou menace autrui. Si c'est un conjoint, un fils, ou un agresseur tiers qui est agressif envers l'usager (maltraitance subie), laissez rigoureusement ABSENT.
4. "isolement_social" : DANGER D'HALLUCINATION ! Inclure uniquement si l'usager vit seul ET n'a aucun enfant, aucun proche, ni famille présente pour l'aider dans sa région. S'il a de la famille ou un proche mentionné (même s'il est malveillant ou éloigné géographiquement mais passe le voir de temps en temps), laissez rigoureusement ABSENT.
5. "perte_autonomie_recente" : DANGER D'HALLUCINATION ! Inclure uniquement s'il y a des preuves physiques de perte de capacités physiques ou motrices récentes (ex: chutes récentes, AVC récent avec incapacité physique pour la toilette/repas). Si l'usager est décrit comme autonome (ex: "elle est tout à fait autonome à la maison"), laissez rigoureusement ABSENT.
6. "epuisement_aidant" : Inclure uniquement si le conjoint ou l'enfant aidant régulier est décrit comme fatigué, à bout, épuisé ou ayant des problèmes physiques liés à l'aide (ex: dos fatigué). S'il n'y a pas d'aidant ou s'il est juste inquiet, laissez ABSENT.
7. "precarite_financiere" : Inclure uniquement si l'usager a des dettes, un découvert bancaire, n'a plus rien pour manger, ou une très petite retraite (900€).

Format JSON attendu (Ne contiendrait que les critères présents, vide si aucun) :
{{
  "code_du_critere_present_1": {{
    "presence": true,
    "justification": "Citation ou preuve stricte tirée du texte"
  }},
  "code_du_critere_present_2": {{
    "presence": true,
    "justification": "Citation ou preuve stricte tirée du texte"
  }}
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
            "usager.cadre_de_vie.etat_logement": raw_data.get("etat_logement", "non_renseigne")
        }

        # Mapping flexible (cherche dans "comid" ou à la racine). On formate le résultat de l'IA : true ou false dans le dictionnaire final
        comid_data = raw_data.get("comid", raw_data)
        for item in self._comid_items:
            code = item["code"]
            val = comid_data.get(code)
            
            # Support du format structuré avec justification
            if isinstance(val, dict):
                val = val.get("presence")
                
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
