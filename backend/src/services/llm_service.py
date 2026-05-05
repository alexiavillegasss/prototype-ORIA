import os
import json
from dotenv import load_dotenv

load_dotenv()

# Configuration LLM Local ou OpenAI
USE_LOCAL_LLM = os.getenv("USE_LOCAL_LLM", "false").lower() == "true"
LOCAL_LLM_URL = os.getenv("LOCAL_LLM_URL", "http://localhost:11434/v1")
LOCAL_LLM_MODEL = os.getenv("LOCAL_LLM_MODEL", "llama3")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

try:
    from openai import OpenAI
    if USE_LOCAL_LLM:
        client = OpenAI(base_url=LOCAL_LLM_URL, api_key="ollama")
        HAS_LLM = True
        CURRENT_MODEL = LOCAL_LLM_MODEL
        print(f"[LLM_SERVICE] Initialisé avec un LLM local : {CURRENT_MODEL} sur {LOCAL_LLM_URL}")
    elif OPENAI_API_KEY and OPENAI_API_KEY.startswith("sk-"):
        client = OpenAI(api_key=OPENAI_API_KEY)
        HAS_LLM = True
        CURRENT_MODEL = "gpt-3.5-turbo"
        print("[LLM_SERVICE] Initialisé avec OpenAI")
    else:
        HAS_LLM = False
        CURRENT_MODEL = None
except ImportError:
    HAS_LLM = False
    CURRENT_MODEL = None


def extract_signals_mock(text: str):
    """
    Fonction de fallback qui utilise la recherche par mots-clés 
    si aucune API LLM n'est disponible ou en cas d'erreur.
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
    Tente d'extraire les signaux via le LLM configuré (Local ou OpenAI). 
    En cas d'échec, bascule sur le mock.
    """
    if not HAS_LLM:
        print("[LLM_SERVICE] Aucun LLM configuré (ni local ni OpenAI) ou librairie manquante. Utilisation du fallback (Mots-clés).")
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
            model=CURRENT_MODEL,
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
                
        print(f"[LLM_SERVICE] Extraction réussie via {CURRENT_MODEL} !")
        return signals

    except Exception as e:
        print(f"[LLM_SERVICE] Erreur API LLM ({e}). Utilisation du fallback (Mots-clés).")
        return extract_signals_mock(text)
