from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# -----------------------------
# INPUT MODEL
# -----------------------------
class AnalyzeRequest(BaseModel):
    text: str


# -----------------------------
# ROOT ENDPOINT
# -----------------------------
@app.get("/")
def root():
    return {"message": "ORIA API is running"}


# -----------------------------
# ORIA CORE LOGIC
# -----------------------------

def extract_signals(text: str):
    """
    Extraction simple (version v1 sans IA)
    """
    text = text.lower()

    return {
        "isolation": "isolé" in text or "seul" in text,
        "fall_risk": "chute" in text,
        "age_risk": "âgé" in text or "personne âgée" in text
    }


def compute_score(signals: dict):
    """
    Scoring simple basé sur règles métier internes
    """
    score = 0

    if signals["isolation"]:
        score += 2
    if signals["fall_risk"]:
        score += 3
    if signals["age_risk"]:
        score += 2

    return score


def determine_risk_level(score: int):
    """
    Classification du risque
    """
    if score >= 5:
        return "high"
    elif score >= 3:
        return "medium"
    else:
        return "low"


# -----------------------------
# ANALYZE ENDPOINT
# -----------------------------
@app.post("/analyze")
def analyze(request: AnalyzeRequest):

    # 1. extraction des signaux
    signals = extract_signals(request.text)

    # 2. score
    score = compute_score(signals)

    # 3. niveau de risque
    risk_level = determine_risk_level(score)

    # 4. réponse ORIA
    return {
        "input": request.text,
        "signals": signals,
        "score": score,
        "risk_level": risk_level
    }