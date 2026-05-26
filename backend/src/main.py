from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

import os
import yaml
from ai.extraction.extractor import SignalExtractor
from application.scoring_engine import ScoringEngine
from application.orientation_engine import OrientationEngine
from application.territory_manager import TerritoryManager
from application.clarification_engine import ClarificationEngine
from infrastructure.database import DatabaseManager

app = FastAPI()

# Initialisation des moteurs
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SCHEMA_PATH = os.path.join(BASE_DIR, 'config', 'schemas', 'schema_definition.json')
COMID_PATH = os.path.join(BASE_DIR, 'config', 'rules', 'COMID.json')
ORIENTATION_RULES_PATH = os.path.join(BASE_DIR, 'config', 'rules', 'orientation_rules.json')
TERRITORY_PATH = os.path.join(BASE_DIR, 'config', 'referentials', 'referentiel_territoire.json')
CONFIG_PATH = os.path.join(BASE_DIR, 'config', 'app_config.yaml')

# 1. Chargement de la configuration technique (app_config.yaml)
with open(CONFIG_PATH, 'r', encoding='utf-8') as f:
    app_config = yaml.safe_load(f)

ai_config = app_config.get('ai', {})

# 2. On "branche" l'extracteur en lui donnant les paramètres du fichier YAML
extractor = SignalExtractor(
    schema_path=SCHEMA_PATH, 
    comid_path=COMID_PATH,
    model=ai_config.get('model_name', 'llama3'),
    base_url=ai_config.get('base_url', 'http://localhost:11434'),
    temperature=float(ai_config.get('temperature', 0.1))
)
scoring_engine = ScoringEngine(comid_rules_path=COMID_PATH)
orientation_engine = OrientationEngine(rules_path=ORIENTATION_RULES_PATH)
territory_manager = TerritoryManager(territory_rules_path=TERRITORY_PATH)
clarification_engine = ClarificationEngine()

db_manager = DatabaseManager(db_path=os.path.join(BASE_DIR, 'oria_database.db'))

# -----------------------------
# INPUT MODEL
# -----------------------------
class AnalyzeRequest(BaseModel):
    text: str
    # Overrides optionnels de validation humaine
    age: Optional[int] = None
    gir: Optional[int] = None
    apa: Optional[str] = None
    pch: Optional[str] = None
    aidant_regulier: Optional[str] = None
    medecin_traitant: Optional[str] = None


# -----------------------------
# ROOT ENDPOINT
# -----------------------------
@app.get("/")
def root():
    return {"message": "ORIA API is running with AI Extraction"}


# -----------------------------
# ANALYZE ENDPOINT
# -----------------------------
@app.post("/analyze")
async def analyze(request: AnalyzeRequest):

    # 1. extraction des signaux par l'IA (Llama 3)
    try:
        extracted_data = await extractor.extract(request.text)
    except Exception as e:
        return {"error": f"Erreur lors de l'extraction IA : {str(e)}"}

    # Application des validations / overrides humains facultatifs
    has_overrides = False
    if request.age is not None:
        extracted_data["usager.identite.age_estime"] = request.age
        has_overrides = True
    if request.gir is not None:
        extracted_data["usager.situation_actuelle.GIR"] = request.gir
        has_overrides = True
    if request.apa is not None:
        extracted_data["usager.situation_actuelle.APA"] = request.apa.lower()
        has_overrides = True
    if request.pch is not None:
        extracted_data["usager.situation_actuelle.PCH"] = request.pch.lower()
        has_overrides = True
    if request.aidant_regulier is not None:
        extracted_data["usager.cadre_de_vie.aidant_regulier"] = request.aidant_regulier.lower()
        has_overrides = True
    if request.medecin_traitant is not None:
        extracted_data["vulnerabilites.sante.suivi_medical.medecin_traitant"] = request.medecin_traitant.lower()
        has_overrides = True

    # 2. Analyse de complexité (COMID)
    comid_results = scoring_engine.calculate_comid_score(extracted_data)

    # 3. Moteur d'orientation
    orientation_results = orientation_engine.evaluate_orientation(extracted_data, comid_results)

    # 4. Territorialisation (Contacts locaux)
    patient_city = extracted_data.get("usager.localisation.commune_residence")
    orientation_with_contacts = territory_manager.get_contacts_for_structures(orientation_results, patient_city)

    # 5. Détection des informations critiques manquantes pour la relecture
    clarification_questions = clarification_engine.get_clarification_questions(extracted_data, orientation_with_contacts, request.text)

    # Définition du statut selon les données disponibles et le contrôle humain
    if clarification_questions:
        status = "en_attente_clarification"
    elif has_overrides:
        status = "analyse_affinee_par_humain"
    else:
        status = "analyse_terminee_en_attente_de_relecture"

    # 6. Sauvegarde en Base de Données (avec les données validées/corrigées par l'humain)
    dossier_id = None
    try:
        dossier_id = db_manager.save_dossier(
            texte_original=request.text,
            donnees_extraites=extracted_data,
            score_comid=comid_results["score_total"],
            niveau_comid=comid_results["label"],
            structures_orientations=orientation_with_contacts
        )
    except Exception as e:
        print(f"Erreur de sauvegarde en base de données : {e}")

    # 7. réponse ORIA complète
    return {
        "id_dossier": dossier_id,
        "input": request.text,
        "schema_pivot": extracted_data,
        "evaluation_complexe": {
            "score_total": comid_results["score_total"],
            "niveau": comid_results["niveau"],
            "label": comid_results["label"],
            "facteurs_detectes": comid_results["items_detectes"]
        },
        "orientation_suggeree": orientation_with_contacts,
        "questions_clarification": clarification_questions,
        "status": status
    }
