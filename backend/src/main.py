from fastapi import FastAPI
from pydantic import BaseModel

import os
import yaml
from ai.extraction.extractor import SignalExtractor
from application.scoring_engine import ScoringEngine
from application.orientation_engine import OrientationEngine
from application.territory_manager import TerritoryManager
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
    base_url=ai_config.get('base_url', 'http://localhost:11434')
)
scoring_engine = ScoringEngine(comid_rules_path=COMID_PATH)
orientation_engine = OrientationEngine(rules_path=ORIENTATION_RULES_PATH)
territory_manager = TerritoryManager(territory_rules_path=TERRITORY_PATH)

db_manager = DatabaseManager(db_path=os.path.join(BASE_DIR, 'oria_database.db'))

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
    return {"message": "ORIA API is running with AI Extraction"}


# -----------------------------
# ANALYZE ENDPOINT
# -----------------------------
@app.post("/analyze")
async def analyze(request: AnalyzeRequest):

    # 1. extraction des signaux par l'IA (Llama 3)
    # Note: Cela peut prendre quelques secondes en local. extracted_data est le nouveau nom que l'ont donne à "mapped" car ce sont les nouvelles données extraites du travail de l'IA dans extractor.py
    try:
        extracted_data = await extractor.extract(request.text)
    except Exception as e:
        return {"error": f"Erreur lors de l'extraction IA : {str(e)}"}

    # 2. Analyse de complexité (COMID). Ici on reçoit les données générées par l'IA dans le fichier extractor.py, que l'on vient de renommer "extracted_data".
    comid_results = scoring_engine.calculate_comid_score(extracted_data)

    # 3. Moteur d'orientation
    orientation_results = orientation_engine.evaluate_orientation(extracted_data, comid_results)

    # 4. Territorialisation (Contacts locaux)
    patient_city = extracted_data.get("usager.localisation.commune_residence")
    orientation_with_contacts = territory_manager.get_contacts_for_structures(orientation_results, patient_city)

    # 5. Sauvegarde en Base de Données (Pseudonymisée)
    dossier_id = None
    try:
        # On pseudonymise le texte d'entrée en clair (ex: Mme Antoinette Durand -> Mme A. D.)
        safe_text = extractor.anonymizer.pseudonymize(request.text)
        dossier_id = db_manager.save_dossier(
            texte_original=safe_text,
            donnees_extraites=extracted_data,
            score_comid=comid_results["score_total"],
            niveau_comid=comid_results["label"],
            structures_orientations=orientation_with_contacts
        )
    except Exception as e:
        print(f"Erreur de sauvegarde en base de données : {e}")

    # 6. réponse ORIA complète
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
        "status": "analyse_terminee_en_attente_de_relecture"
    }
