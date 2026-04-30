import os
import json
from dotenv import load_dotenv

load_dotenv()

# Vérifier si on a une clé API
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

try:
    if OPENAI_API_KEY and OPENAI_API_KEY.startswith("sk-"):
        from openai import OpenAI
        client = OpenAI(api_key=OPENAI_API_KEY)
        HAS_OPENAI = True
    else:
        HAS_OPENAI = False
except ImportError:
    HAS_OPENAI = False


def extract_signals_mock(text: str):
    """
    Fonction de fallback qui utilise la recherche par mots-clés 
    si l'API OpenAI n'est pas disponible.
    """
    text_lower = text.lower().replace("’", "'").replace("\n", " ")

    return {
        "isolement": any(w in text_lower for w in ["isolé", "isole", "seul", "isolement", "sans famille", "sans entourage"]),
        "chute": any(w in text_lower for w in ["chute", "tombé", "tombe", "par terre"]),
        "age_risk": any(w in text_lower for w in ["âgé", "age", "personne âgée", "vieillissement", "senior"]),
        "retour_hospit": any(w in text_lower for w in ["hospitalisation", "hôpital", "hopital", "retour", "clinique", "urgences", "sortie d'"]),
        "urgence_medicale": any(w in text_lower for w in ["urgence vitale", "danger de mort", "inconscient", "saigne"]),
        "violence_danger": any(w in text_lower for w in ["violence", "coup", "spoliation", "maltraitance", "arme", "menace"]),
        "logement_insalubre": any(w in text_lower for w in ["insalubre", "diogène", "diogene", "incurie", "cafard", "punaises", "sans abri"]),
        "troubles_cognitifs": any(w in text_lower for w in ["désorienté", "desoriente", "alzheimer", "démence", "demence", "oublie", "perd la tête"]),
        "presence_mandataire": any(w in text_lower for w in ["tutelle", "curatelle", "mandataire", "sauvegarde de justice"]),
        "refus_aide": any(w in text_lower for w in ["refus", "refuse", "ne veut pas", "opposition"]),
        "epuisement_aidant": any(w in text_lower for w in ["épuisé", "epuise", "n'en peut plus", "à bout", "a bout"])
    }


def extract_signals_llm(text: str):
    """
    Tente d'extraire les signaux via OpenAI. 
    En cas d'échec ou d'absence de clé, bascule sur le mock.
    """
    if not HAS_OPENAI:
        print("[LLM_SERVICE] Clé OpenAI non trouvée ou librairie manquante. Utilisation du fallback (Mots-clés).")
        return extract_signals_mock(text)

    prompt = f"""
    Tu es une assistante sociale experte. 
    Analyse le texte suivant et détermine si les signaux suivants sont présents (true ou false).
    Sois subtile, comprends la négation (ex: "n'est pas tombée" -> chute: false).
    
    Texte à analyser : "{text}"
    
    Réponds UNIQUEMENT avec un objet JSON contenant exactement ces clés (booléens) :
    - isolement
    - chute
    - age_risk
    - retour_hospit
    - urgence_medicale
    - violence_danger
    - logement_insalubre
    - troubles_cognitifs
    - presence_mandataire
    - refus_aide
    - epuisement_aidant
    """

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo", # ou gpt-4o-mini
            response_format={ "type": "json_object" },
            messages=[
                {"role": "system", "content": "Tu es un assistant qui renvoie uniquement du JSON."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.0
        )
        
        result_json = response.choices[0].message.content
        signals = json.loads(result_json)
        
        # Vérification basique des clés attendues
        expected_keys = [
            "isolement", "chute", "age_risk", "retour_hospit", 
            "urgence_medicale", "violence_danger", "logement_insalubre", 
            "troubles_cognitifs", "presence_mandataire", "refus_aide", "epuisement_aidant"
        ]
        
        # S'assurer que le dictionnaire a bien toutes les clés
        for key in expected_keys:
            if key not in signals:
                signals[key] = False
                
        print("[LLM_SERVICE] Extraction réussie via OpenAI !")
        return signals

    except Exception as e:
        print(f"[LLM_SERVICE] Erreur API OpenAI ({e}). Utilisation du fallback (Mots-clés).")
        return extract_signals_mock(text)
