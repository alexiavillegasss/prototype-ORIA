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
1. "age" : Âge estimé ou mentionné de la personne (chiffre entier, ou null si non mentionné).
2. "ville" : Commune de résidence principale (ex: "Hyères", "Toulon", "Sanary-sur-Mer", "La Seyne-sur-Mer", "La Garde", "Ollioules", ou null si non mentionné).
3. "apa" : Choisir "oui" si la personne bénéficie de l'APA. Choisir "non" si elle n'en bénéficie pas. Choisir "inconnu" si non mentionné.
4. "pch" : Choisir "oui" si bénéficie de la PCH, "non" si non, ou "inconnu" si non mentionné.
5. "gir" : Chiffre officiel de 1 à 6 si précisé (ex: "GIR 2", "GIR 3"), ou null si non précisé.
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
    - "refus_de_soins" uniquement en cas d'opposition active, hostile ou de refus explicite de se soigner ou de recevoir les professionnels. Oublier de prendre ses médicaments (ex: "oublis de médicaments") ou oublier un rendez-vous (ex: "avait oublié ma visite") n'est JAMAIS un refus de soins.
    - "refus_aide_domicile" uniquement si l'usager lui-même s'oppose activement à l'aide à domicile.
    - "sortie_hospitalisation" si retour à domicile post-hospitalisation récente.
    - "aide_alimentaire" si dénutrition sévère ou frigo vide sans ressources.
    - "secours_urgence" si danger vital imminent ou agression physique en cours.
    - "recherche_medecin" si recherche active de médecin traitant.
    - "maintien_a_domicile" si demande générale d'aide à domicile pour rester chez soi, adaptation ou panne d'équipement (ex: réfrigérateur en panne), ou besoin d'aide pour les courses.
    - "information_aides" si demande générale d'informations.
11. "professionnels_domicile" : Choisir "oui" si des professionnels (infirmiers, kinés, aides) passent régulièrement, ou "non" sinon.
12. "aidant_regulier" : Choisir "oui" si présence régulière et stable d'un aidant familial, ou "non" sinon.
13. "etat_logement" : Choisir "diogene" si syndrome de Diogène, "incurie" si logement très sale, "insalubre" si pas d'eau ou plafond menace de s'effondrer, "propre" si propre, ou "non_renseigne" sinon.

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
      "justification": "Citation mot à mot ou synonyme direct prouvant la présence"
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
      "justification": "oublie de manger"
    }},
    {{
      "code": "perte_autonomie_recente",
      "justification": "a fait une chute hier"
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
            "usager.cadre_de_vie.etat_logement": raw_data.get("etat_logement", "non_renseigne")
        }

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

        # B. Force logement inadapté si l'état du logement est insalubre/diogène/incurie
        if mapped.get("usager.cadre_de_vie.etat_logement") in ["insalubre", "diogene", "incurie"]:
            mapped["evaluation.comid.logement_inadapte"] = True

        # C. Force opposition aux soins si le motif principal est le refus de soins ou d'aide
        if mapped.get("demande.motif_principal") in ["refus_de_soins", "refus_aide_domicile"]:
            mapped["evaluation.comid.opposition_soins"] = True

        # D. Force transition de parcours si hospitalisation récente et motif de sortie d'hôpital
        if mapped.get("vulnerabilites.sante.hospitalisation.statut") == "recente" and mapped.get("demande.motif_principal") == "sortie_hospitalisation":
            mapped["evaluation.comid.transition_parcours"] = True

        # E. Force lourdeur réseau si suspicion de malveillance avérée
        if mapped.get("usager.situation_actuelle.suspicion_malveillance") != "aucune":
            mapped["evaluation.comid.lourdeur_reseau"] = True

        # F. Force isolement social si pas d'aidant régulier et isolement relationnel critique
        if mapped.get("usager.cadre_de_vie.aidant_regulier") == "non" and mapped.get("vulnerabilites.social.isolement_relationnel") == "critique":
            mapped["evaluation.comid.isolement_social"] = True

        # G. Force multimorbidité si "polypathologie" mentionnée ET qu'une autre pathologie est extraite
        # Pour éviter de forcer sur M. Pierre qui n'a qu'une seule maladie listée en plus du mot-clé
        if "polypathologie" in text_lower or "polypathologique" in text_lower:
            if len(positive_codes) > 1 or (len(positive_codes) == 1 and "multimorbidite" not in positive_codes):
                mapped["evaluation.comid.multimorbidite"] = True

        # H. Force addiction si alcoolisme ou alcool mentionné de manière négative
        if "addiction à l'alcool" in text_lower or "alcoolisme" in text_lower:
            mapped["evaluation.comid.addiction"] = True

        # I. Sécurité Épuisement de l'aidant : si suspicion de malveillance active par un proche (agression, vol),
        # l'agresseur ne doit pas être considéré comme un aidant épuisé
        if mapped.get("usager.situation_actuelle.suspicion_malveillance") in ["spoliation_financiere", "violences_physiques"]:
            mapped["evaluation.comid.epuisement_aidant"] = False

        # Cas particulier pour l'isolement (vulnerabilites.social.isolement_relationnel)
        if mapped.get("evaluation.comid.isolement_social") or raw_data.get("seule") == "oui":
            mapped["vulnerabilites.social.isolement_relationnel"] = "critique"
        else:
            mapped["vulnerabilites.social.isolement_relationnel"] = None

        return mapped
