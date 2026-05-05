import re
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
import os

from backend.src.services.comid_engine import compute_comid
from backend.src.services.schema_loader import load_schema
from backend.src.services.schema_builder import build_schema

app = FastAPI(title="ORIA API")

# CORS pour permettre l'appel depuis le frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# -----------------------------
# INPUT MODEL
# -----------------------------
class AnalyzeRequest(BaseModel):
    text: str


# (Static files mount moved to the end of file)


# -----------------------------
# ENTITY EXTRACTION
# -----------------------------
def extract_entities(text: str):
    entities = {}
    match = re.search(r'(\d+)\s*ans', text.lower())
    if match:
        entities["age"] = int(match.group(1))
    return entities


from backend.src.services.llm_service import extract_signals_llm

# -----------------------------
# ANALYZE ENDPOINT (ORIA CORE)
# -----------------------------
@app.post("/analyze")
def analyze(request: AnalyzeRequest):

    # 1. extraction signaux via LLM (ou fallback mots-clés)
    signals = extract_signals_llm(request.text)

    # 2. COMID (complexité)
    comid_result = compute_comid(signals)

    # 3. charger le schema pivot
    template = load_schema()

    # 3b. extraction entites (age)
    entities = extract_entities(request.text)

    # 4. construire dossier ORIA complet
    dossier = build_schema(
        template=template,
        text=request.text,
        signals=signals,
        score=comid_result["score"]["total"],
        risk_level=comid_result["classification"]["level"],
        entities=entities
    )

    # 5. retour final ORIA
    return dossier


# -----------------------------
# STATIC FILES (Frontend UI)
# -----------------------------
from pathlib import Path as _Path
FRONTEND_DIR = str(_Path(__file__).resolve().parent.parent.parent / "frontend" / "public")

# Servir les fichiers statiques à la fin pour ne pas intercepter les routes API
app.mount("/", StaticFiles(directory=FRONTEND_DIR, html=True), name="static")