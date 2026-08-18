from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, FileResponse, Response
from fastapi import Request
from pydantic import BaseModel
from typing import Optional
from collections import Counter

import os
import json
import yaml
from ai.extraction.extractor import SignalExtractor
from ai.extraction.fiche_extractor import FicheExtractor
from application.scoring_engine import ScoringEngine
from application.orientation_engine import OrientationEngine
from application.territory_manager import TerritoryManager
from application.pdf_generator import PDFGenerator
from infrastructure.database import DatabaseManager

app = FastAPI()

# Montage des fichiers statiques (CSS, JS) pour le tableau de bord
STATIC_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

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

# 2. Initialisation des composants
extractor = SignalExtractor(
    schema_path=SCHEMA_PATH, 
    comid_path=COMID_PATH,
    model=ai_config.get('model_name', 'llama3'),
    base_url=ai_config.get('base_url', 'http://localhost:11434')
)
fiche_extractor = FicheExtractor()
scoring_engine = ScoringEngine(comid_rules_path=COMID_PATH)
orientation_engine = OrientationEngine(rules_path=ORIENTATION_RULES_PATH)
territory_manager = TerritoryManager(territory_rules_path=TERRITORY_PATH)
db_manager = DatabaseManager(db_path=os.path.join(BASE_DIR, 'oria_database.db'))
pdf_generator = PDFGenerator(
    dac_template_path=os.path.join(STATIC_DIR, "fiche_dac_vierge.pdf"),
    clic_template_path=os.path.join(STATIC_DIR, "fiche_clic_LaSeyne_vierge.pdf"),
    clic_toulon_template_path=os.path.join(STATIC_DIR, "fiche_clic_Toulon.pdf"),
    clic_provence_verte_template_path=os.path.join(STATIC_DIR, "fiche_clic_ProvenceVerte.pdf"),
    clic_hadage_template_path=os.path.join(STATIC_DIR, "fiche_clic_Hadage.pdf")
)

# -----------------------------
# INPUT MODEL
# -----------------------------
class AnalyzeRequest(BaseModel):
    text: str


class ValidateRequest(BaseModel):
    status: str
    structure_choisie: str


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
    orientation_results = orientation_engine.evaluate_orientation(extracted_data, comid_results, original_text=request.text)

    # 4. Territorialisation (Contacts locaux)
    patient_city = extracted_data.get("usager.localisation.commune_residence")
    orientation_with_contacts = territory_manager.get_contacts_for_structures(orientation_results, patient_city)

    # 5. Sauvegarde en Base de Données (Pseudonymisée)
    dossier_id = None
    try:
        # On pseudonymise le texte d'entrée en clair (ex: Mme Antoinette Durand -> Mme A. D.)
        safe_text = extractor.anonymizer.pseudonymize(request.text)
        # Assemble all orientation details to store in a single JSON column
        details = {
            "orientation_results": orientation_results,
            "orientation_with_contacts": orientation_with_contacts
        }
        dossier_id = db_manager.save_dossier(
            texte_original=safe_text,
            donnees_extraites=extracted_data,
            score_comid=comid_results["score_total"],
            niveau_comid=comid_results["label"],
            structures_orientations=orientation_with_contacts,
            details_complet=details
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


# -----------------------------
# DASHBOARD (Tableau de bord)
# -----------------------------
@app.get("/dashboard", response_class=HTMLResponse)
def dashboard():
    """Sert la page HTML du tableau de bord."""
    html_path = os.path.join(STATIC_DIR, "index.html")
    with open(html_path, "r", encoding="utf-8") as f:
        return f.read()

# -----------------------------
# INTERFACE DE TEST D'ORIENTATION
# -----------------------------
@app.get("/orienter", response_class=HTMLResponse)
def orienter():
    """Sert la page HTML du moteur d'orientation interactif."""
    html_path = os.path.join(STATIC_DIR, "orienter.html")
    with open(html_path, "r", encoding="utf-8") as f:
        return f.read()

@app.get("/remplir", response_class=HTMLResponse)
def remplir():
    """Sert la page HTML de sélection FO/Grille COMID."""
    html_path = os.path.join(STATIC_DIR, "remplir.html")
    with open(html_path, "r", encoding="utf-8") as f:
        return f.read()

@app.get("/fiches", response_class=HTMLResponse)
def fiches():
    """Sert la page HTML de sélection des Fiches d'Orientation."""
    html_path = os.path.join(STATIC_DIR, "fiches.html")
    with open(html_path, "r", encoding="utf-8") as f:
        return f.read()

@app.get("/comid", response_class=HTMLResponse)
def comid():
    """Sert la page HTML de la grille COMID interactive."""
    html_path = os.path.join(STATIC_DIR, "comid.html")
    with open(html_path, "r", encoding="utf-8") as f:
        return f.read()

class ComidEvalRequest(BaseModel):
    dossier_id: str
    senior_nom: Optional[str] = ""
    type_eval: str  # 'entree' ou 'sortie'
    score: int
    niveau: str
    criteres: Optional[list] = []

@app.post("/api/dossiers/{dossier_id}/validate")
def validate_dossier(dossier_id: int, request: ValidateRequest):
    """Valide l'orientation d'un dossier par le professionnel."""
    success = db_manager.update_dossier_validation(
        dossier_id=dossier_id,
        status=request.status,
        structure_choisie=request.structure_choisie
    )
    if not success:
        return {"error": "Dossier introuvable."}
    return {"message": "Orientation enregistrée avec succès en base de données !"}

# -----------------------------
# API COMID EVALUATIONS (ENTREE / SORTIE)
# -----------------------------
@app.post("/api/comid/evaluations")
def save_comid_evaluation(request: ComidEvalRequest):
    """Sauvegarde une évaluation COMID (Entrée ou Sortie)."""
    eval_id = db_manager.save_comid_eval(
        dossier_id=request.dossier_id,
        senior_nom=request.senior_nom,
        type_eval=request.type_eval,
        score=request.score,
        niveau=request.niveau,
        criteres=request.criteres
    )
    return {"message": "Évaluation COMID enregistrée avec succès !", "id": eval_id}

@app.get("/api/comid/dossiers-entree")
def get_entree_dossiers():
    """Récupère les dossiers avec évaluation d'entrée pour la liaison en sortie."""
    return db_manager.get_entree_dossiers()

@app.get("/api/comid/comparisons")
def get_comid_comparisons():
    """Récupère les données comparatives Entrée vs Sortie pour le tableau de bord."""
    return db_manager.get_comid_comparisons()

@app.delete("/api/comid/evaluations/{dossier_id}")
def delete_comid_dossier(dossier_id: str):
    """Supprime les évaluations d'un dossier COMID."""
    success = db_manager.delete_comid_evaluations_by_dossier(dossier_id)
    if not success:
        return {"error": "Dossier introuvable."}
    return {"message": f"Dossier {dossier_id} supprimé avec succès."}

# -----------------------------
# API SANKEY DATA
# -----------------------------

def _get_dimension_value(dossier: dict, dimension: str) -> str:
    """Extrait la valeur d'une dimension donnée pour un dossier.
    Retourne une chaîne lisible pour l'affichage dans le Sankey.
    """
    data = dossier.get("donnees_extraites", {})
    if not isinstance(data, dict):
        data = {}

    if dimension == "commune":
        val = data.get("usager.localisation.commune_residence", "")
        return val if val else "Inconnue"

    elif dimension == "tranche_age":
        age = data.get("usager.identite.age_estime")
        if age is None:
            return "Âge inconnu"
        try:
            age = int(age)
        except (ValueError, TypeError):
            return "Âge inconnu"
        if age < 65:
            return "60-64 ans"
        elif age < 70:
            return "65-69 ans"
        elif age < 75:
            return "70-74 ans"
        elif age < 80:
            return "75-79 ans"
        elif age < 85:
            return "80-84 ans"
        else:
            return "85 ans et plus"

    elif dimension == "complexite":
        val = dossier.get("niveau_comid", "")
        return val if val else "Inconnu"

    elif dimension == "apa":
        val = data.get("usager.situation_actuelle.beneficiaire_apa")
        if val is True or (isinstance(val, str) and val.lower() in ["oui", "true", "1"]):
            return "APA : Oui"
        elif val is False or (isinstance(val, str) and val.lower() in ["non", "false", "0"]):
            return "APA : Non"
        return "APA : Non renseigné"

    elif dimension == "gir":
        val = data.get("usager.situation_actuelle.GIR")
        if val is not None:
            return f"GIR {val}"
        return "GIR non renseigné"

    elif dimension == "medecin_traitant":
        val = data.get("usager.entourage.medecin_traitant_identifie")
        if val is True or (isinstance(val, str) and val.lower() in ["oui", "true", "1"]):
            return "Médecin traitant : Oui"
        elif val is False or (isinstance(val, str) and val.lower() in ["non", "false", "0"]):
            return "Médecin traitant : Non"
        return "Médecin traitant : Non renseigné"

    elif dimension == "urgence":
        val = data.get("demande.urgence_ressentie")
        if val is True or (isinstance(val, str) and val.lower() in ["oui", "true", "1"]):
            return "Urgence : Oui"
        elif val is False or (isinstance(val, str) and val.lower() in ["non", "false", "0"]):
            return "Urgence : Non"
        return "Urgence : Non renseigné"

    return "Inconnu"


def _get_structure_types(dossier: dict) -> list:
    """Extrait la liste des types de structures orientées pour un dossier."""
    structs = dossier.get("structures_orientations", [])
    if not isinstance(structs, list):
        return ["Inconnu"]
    types = []
    for s in structs:
        if isinstance(s, dict):
            st = s.get("structure_type", "Inconnu")
            if st and st not in types:
                types.append(st)
    return types if types else ["Inconnu"]


@app.get("/api/dashboard/sankey")
def get_sankey_data(dim1: str = "commune", dim2: str = "complexite", dim3: str = "structure"):
    """Construit les données du diagramme de Sankey à partir de la BDD.
    Les 3 dimensions sont configurables via les paramètres dim1, dim2, dim3.
    Dimensions disponibles : commune, tranche_age, complexite, structure, apa, gir, medecin_traitant, urgence.
    """
    dossiers = db_manager.get_all_dossiers()

    # --- KPIs ---
    total = len(dossiers)
    scores = [d["score_comid"] for d in dossiers if d.get("score_comid") is not None]
    score_moyen = sum(scores) / len(scores) if scores else None

    communes = []
    all_structure_types = []
    niveaux = []

    for d in dossiers:
        data = d.get("donnees_extraites", {})
        if isinstance(data, dict):
            communes.append(data.get("usager.localisation.commune_residence", "Inconnue") or "Inconnue")
        else:
            communes.append("Inconnue")

        niveaux.append(d.get("niveau_comid", "Inconnu") or "Inconnu")

        structs = d.get("structures_orientations", [])
        if isinstance(structs, list):
            for s in structs:
                if isinstance(s, dict):
                    all_structure_types.append(s.get("structure_type", "Inconnu"))

    commune_counter = Counter(communes)
    niveau_counter = Counter(niveaux)
    structure_counter = Counter(all_structure_types)

    kpis = {
        "total_dossiers": total,
        "score_moyen": score_moyen,
        "commune_top": commune_counter.most_common(1)[0][0] if commune_counter else None,
        "niveau_top": niveau_counter.most_common(1)[0][0] if niveau_counter else None,
        "structure_top": structure_counter.most_common(1)[0][0] if structure_counter else None
    }

    # Construction dynamique des liens en fonction des dimensions valides
    valid_dims = []
    for dim in [dim1, dim2, dim3]:
        if dim != "none":
            valid_dims.append(dim)

    links_counts = []
    for i in range(len(valid_dims) - 1):
        links_counts.append(Counter())

    for d in dossiers:
        # Extraire les valeurs pour chaque dimension valide
        dim_values = []
        for dim in valid_dims:
            if dim == "structure":
                dim_values.append(_get_structure_types(d))
            else:
                dim_values.append([_get_dimension_value(d, dim)])

        # Créer les liens entre les niveaux adjacents
        for i in range(len(valid_dims) - 1):
            vals_src = dim_values[i]
            vals_tgt = dim_values[i+1]
            for src in vals_src:
                for tgt in vals_tgt:
                    links_counts[i][(src, tgt)] += 1

    # Construction des nœuds (uniques)
    node_names = set()
    for counter in links_counts:
        for (src, tgt) in counter:
            node_names.add(src)
            node_names.add(tgt)

    nodes = [{"name": n} for n in sorted(node_names)]

    # Construction des liens
    links = []
    for counter in links_counts:
        for (src, tgt), value in counter.items():
            links.append({"source": src, "target": tgt, "value": value})

    return {
        "kpis": kpis,
        "sankey": {
            "nodes": nodes,
            "links": links
        }
    }

@app.post("/api/orientation/dac/generate_pdf")
async def generate_dac_pdf(request: AnalyzeRequest):
    try:
        extracted_data = await fiche_extractor.extract_for_dac(request.text)
        pdf_bytes = pdf_generator.generate_dac_pdf(extracted_data)
        return Response(
            content=pdf_bytes, 
            media_type="application/pdf", 
            headers={"Content-Disposition": "attachment; filename=fiche_orientation_dac.pdf"}
        )
    except Exception as e:
        return {"error": f"Erreur lors de la génération du PDF : {str(e)}"}

@app.post("/api/orientation/clic/generate_pdf")
async def generate_clic_pdf(request: AnalyzeRequest):
    try:
        extracted_data = await fiche_extractor.extract_for_clic(request.text)
        pdf_bytes = pdf_generator.generate_clic_pdf(extracted_data)
        return Response(
            content=pdf_bytes, 
            media_type="application/pdf", 
            headers={"Content-Disposition": "attachment; filename=fiche_orientation_clic_laseyne.pdf"}
        )
    except Exception as e:
        return {"error": f"Erreur lors de la génération du PDF : {str(e)}"}

@app.post("/api/orientation/clic_toulon/generate_pdf")
async def generate_clic_toulon_pdf(request: AnalyzeRequest):
    try:
        extracted_data = await fiche_extractor.extract_for_clic(request.text)
        pdf_bytes = pdf_generator.generate_clic_toulon_pdf(extracted_data)
        return Response(
            content=pdf_bytes, 
            media_type="application/pdf", 
            headers={"Content-Disposition": "attachment; filename=fiche_orientation_clic_toulon.pdf"}
        )
    except Exception as e:
        return {"error": f"Erreur lors de la génération du PDF : {str(e)}"}


@app.post("/api/orientation/clic_provence_verte/generate_pdf")
async def generate_clic_provence_verte_pdf(request: AnalyzeRequest):
    try:
        extracted_data = await fiche_extractor.extract_for_clic(request.text)
        pdf_bytes = pdf_generator._fill_clic_provence_verte(extracted_data)
        return Response(
            content=pdf_bytes, 
            media_type="application/pdf", 
            headers={"Content-Disposition": "attachment; filename=fiche_orientation_clic_provence_verte.pdf"}
        )
    except Exception as e:
        return {"error": f"Erreur lors de la génération du PDF : {str(e)}"}

@app.post("/api/orientation/clic_hadage/generate_pdf")
async def generate_clic_hadage_pdf(request: AnalyzeRequest):
    try:
        extracted_data = await fiche_extractor.extract_for_clic(request.text)
        pdf_bytes = pdf_generator._fill_clic_hadage(extracted_data)
        return Response(
            content=pdf_bytes, 
            media_type="application/pdf", 
            headers={"Content-Disposition": "attachment; filename=fiche_orientation_clic_hadage.pdf"}
        )
    except Exception as e:
        return {"error": f"Erreur lors de la génération du PDF : {str(e)}"}

class ComidPDFRequest(BaseModel):
    email: str = ""
    score: int = 0
    level: str = "Non complexe"
    date: str = ""
    domainScores: dict = {}
    checkedItems: list = []

@app.post("/api/comid/generate_pdf")
async def generate_comid_pdf_endpoint(request: ComidPDFRequest):
    try:
        pdf_bytes = pdf_generator.generate_comid_pdf(request.dict())
        filename = f"Synthese_COMID_Score_{request.score}.pdf"
        return Response(
            content=pdf_bytes, 
            media_type="application/pdf", 
            headers={"Content-Disposition": f"attachment; filename={filename}"}
        )
    except Exception as e:
        return {"error": f"Erreur lors de la génération du PDF COMID : {str(e)}"}
