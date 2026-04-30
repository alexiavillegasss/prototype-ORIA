from fastapi import FastAPI
from pydantic import BaseModel

from backend.src.services.comid_engine import compute_comid
from backend.src.services.schema_loader import load_schema
from backend.src.services.schema_builder import build_schema

app = FastAPI(title="ORIA API")


# -----------------------------
# INPUT MODEL
# -----------------------------
class AnalyzeRequest(BaseModel):
    text: str


# -----------------------------
# ROOT
# -----------------------------
@app.get("/")
def root():
    return {
        "message": "ORIA API running",
        "status": "ok"
    }


# -----------------------------
# SIGNAL EXTRACTION (V1 simple)
# -----------------------------
def extract_signals(text: str):
    text = text.lower()

    return {
        "isolement": "isolé" in text or "seul" in text,
        "chute": "chute" in text,
        "age_risk": "âgé" in text or "personne âgée" in text,
        "retour_hospit": "hospitalisation" in text or "retour" in text
    }


# -----------------------------
# ANALYZE ENDPOINT (ORIA CORE)
# -----------------------------
@app.post("/analyze")
def analyze(request: AnalyzeRequest):

    # 1. extraction signaux
    signals = extract_signals(request.text)

    # 2. COMID (complexité)
    comid_result = compute_comid(signals)

    # 3. charger le schema pivot
    template = load_schema()

    # 4. construire dossier ORIA complet
    dossier = build_schema(
        template=template,
        text=request.text,
        signals=signals,
        score=comid_result["score"]["total"],
        risk_level=comid_result["classification"]["level"]
    )

    # 5. retour final ORIA
    return dossier