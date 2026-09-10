from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, FileResponse, Response
from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from collections import Counter

import os
import json
import yaml
from ai.extraction.extractor import SignalExtractor
from ai.extraction.fiche_extractor import FicheExtractor
from application.scoring_engine import ScoringEngine
from application.orientation_engine import OrientationEngine
from application.territory_manager import TerritoryManager
from application.commune_normalizer import normalize_commune
from application.pdf_generator import PDFGenerator
from infrastructure.database import DatabaseManager

app = FastAPI()

@app.middleware("http")
async def add_no_cache_header(request: Request, call_next):
    response = await call_next(request)
    if request.url.path.startswith("/static"):
        response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate, max-age=0"
        response.headers["Pragma"] = "no-cache"
        response.headers["Expires"] = "0"
    return response

# Montage des fichiers statiques (CSS, JS) pour le tableau de bord
STATIC_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

STORAGE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "storage", "dossiers")

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
db_manager = DatabaseManager()
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
    createur: Optional[str] = "Anonyme"
    dossier_id: Optional[str] = None


class ValidateRequest(BaseModel):
    status: str
    structure_choisie: str


# -----------------------------
# ROOT ENDPOINT
# -----------------------------
from fastapi.responses import RedirectResponse

@app.get("/")
def root():
    return RedirectResponse(url="/profil")

def clean_dossier_id(d_id: Optional[str]) -> Optional[int]:
    if not d_id or str(d_id).lower() in ("new", "undefined", "null", ""):
        return None
    d_id_str = str(d_id).strip()
    try:
        return int(d_id_str)
    except ValueError:
        pass
    import re
    digits = re.findall(r'\d+', d_id_str)
    if digits:
        try:
            return int(digits[0])
        except ValueError:
            pass
    return None




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
        
        d_id_int = clean_dossier_id(request.dossier_id)
        
        # Gérer l'historique des orientations
        historique = []
        existing_details = {}
        if d_id_int is not None:
            dossier_360 = db_manager.get_dossier_360_details(str(d_id_int))
            if dossier_360 and dossier_360.get("orientation"):
                existing_details = dossier_360["orientation"].get("details_complet") or {}
                if isinstance(existing_details, dict):
                    historique = list(existing_details.get("historique_orientations", []))
                    if not historique:
                        first_entry = {
                            "date": dossier_360["orientation"].get("date_creation") or datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                            "texte_original": dossier_360["orientation"].get("texte_original"),
                            "donnees_extraites": dossier_360["orientation"].get("donnees_extraites"),
                            "structures_orientations": dossier_360["orientation"].get("structures_orientations"),
                            "validation_utilisateur": existing_details.get("validation_utilisateur")
                        }
                        if first_entry["texte_original"]:
                            historique.append(first_entry)
                            
        # Ajouter la nouvelle orientation
        new_entry = {
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "texte_original": safe_text,
            "donnees_extraites": extracted_data,
            "structures_orientations": orientation_with_contacts,
            "validation_utilisateur": None
        }
        historique.append(new_entry)
        
        details = existing_details.copy() if isinstance(existing_details, dict) else {}
        details["createur"] = request.createur or details.get("createur", "Anonyme")
        details["historique_orientations"] = historique
        details["raw_text"] = request.text
        
        # Si un ID de dossier existant est passé, on met à jour
        if d_id_int is not None:
            success = db_manager.update_dossier(
                dossier_id=d_id_int,
                texte_original=safe_text,
                donnees_extraites=extracted_data,
                score_comid=comid_results["score_total"],
                niveau_comid=comid_results["label"],
                structures_orientations=orientation_with_contacts,
                details_complet=details
            )
            if success:
                dossier_id = d_id_int
            else:
                # Si non trouvé pour x raison (ex: dossier créé via COMID/ZARIT mais pas encore d'orientation), 
                # on crée la ligne dans dossiers_patients en forçant l'ID pour conserver la liaison.
                dossier_id = db_manager.save_dossier(
                    texte_original=safe_text,
                    donnees_extraites=extracted_data,
                    score_comid=comid_results["score_total"],
                    niveau_comid=comid_results["label"],
                    structures_orientations=orientation_with_contacts,
                    details_complet=details,
                    dossier_id=d_id_int
                )
        else:
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

@app.get("/profil", response_class=HTMLResponse)
def profil():
    """Sert la page du profil utilisateur"""
    html_path = os.path.join(STATIC_DIR, "profil.html")
    with open(html_path, "r", encoding="utf-8") as f:
        return f.read()

@app.get("/dossier/{dossier_id}", response_class=HTMLResponse)
def dossier_details_page(dossier_id: str):
    """Sert la page HTML des détails du dossier patient."""
    html_path = os.path.join(STATIC_DIR, "dossier_details.html")
    with open(html_path, "r", encoding="utf-8") as f:
        return f.read()

class ComidEvalRequest(BaseModel):
    dossier_id: str
    senior_nom: Optional[str] = ""
    type_eval: str  # 'entree' ou 'sortie'
    score: int
    niveau: str
    criteres: Optional[list] = []
    createur: Optional[str] = "Anonyme"

@app.post("/api/dossiers/{dossier_id}/validate")
def validate_dossier(dossier_id: str, request: ValidateRequest):
    """Valide l'orientation d'un dossier par le professionnel."""
    cleaned_id = clean_dossier_id(dossier_id)
    if cleaned_id is None:
        return {"error": "Dossier introuvable."}

    success = db_manager.update_dossier_validation(
        dossier_id=cleaned_id,
        status=request.status,
        structure_choisie=request.structure_choisie
    )
    if not success:
        return {"error": "Dossier introuvable."}
    return {"message": "Orientation enregistrée avec succès en base de données !"}

class ValidateHistoryItemRequest(BaseModel):
    history_index: int
    status: str
    structure_choisie: str

@app.post("/api/dossiers/{dossier_id}/validate-history-item")
def validate_history_item_endpoint(dossier_id: str, req: ValidateHistoryItemRequest):
    """Valide une orientation spécifique de l'historique d'un dossier."""
    cleaned_id = clean_dossier_id(dossier_id)
    if cleaned_id is None:
        return {"error": "Dossier introuvable."}

    success = db_manager.update_history_item_validation(
        dossier_id=cleaned_id,
        history_index=req.history_index,
        status=req.status,
        structure_choisie=req.structure_choisie
    )
    if not success:
        return {"error": "Mise à jour de la validation échouée."}
    return {"success": True, "message": "Statut de l'orientation mis à jour avec succès !"}

# -----------------------------
# API COMID EVALUATIONS (ENTREE / SORTIE)
# -----------------------------
@app.post("/api/comid/evaluations")
def save_comid_evaluation(request: ComidEvalRequest):
    """Sauvegarde une évaluation COMID (Entrée ou Sortie)."""
    cleaned_id = clean_dossier_id(request.dossier_id)
    if cleaned_id is None:
        # Nouveau dossier
        d_id_int = db_manager.save_dossier(
            texte_original="",
            donnees_extraites={
                "usager.identite.nom": request.senior_nom.split()[-1] if request.senior_nom else "",
                "usager.identite.prenom": " ".join(request.senior_nom.split()[:-1]) if request.senior_nom and len(request.senior_nom.split()) > 1 else (request.senior_nom or ""),
                "usager_nom_usage": request.senior_nom.split()[-1] if request.senior_nom else "",
                "usager_prenoms": " ".join(request.senior_nom.split()[:-1]) if request.senior_nom and len(request.senior_nom.split()) > 1 else (request.senior_nom or "")
            },
            score_comid=request.score if request.type_eval == "entree" else 0,
            niveau_comid=request.niveau if request.type_eval == "entree" else "",
            structures_orientations=[],
            details_complet={"createur": request.createur or "Anonyme", "historique_orientations": []}
        )
        d_id = str(d_id_int)
    else:
        d_id = str(cleaned_id)
        # S'assurer que le dossier existe aussi dans dossiers_patients pour éviter les désynchronisations
        dossier_360 = db_manager.get_dossier_360_details(d_id)
        if not dossier_360 or not dossier_360.get("orientation"):
            db_manager.save_dossier(
                texte_original="",
                donnees_extraites={
                    "usager.identite.nom": request.senior_nom.split()[-1] if request.senior_nom else "",
                    "usager.identite.prenom": " ".join(request.senior_nom.split()[:-1]) if request.senior_nom and len(request.senior_nom.split()) > 1 else (request.senior_nom or ""),
                    "usager_nom_usage": request.senior_nom.split()[-1] if request.senior_nom else "",
                    "usager_prenoms": " ".join(request.senior_nom.split()[:-1]) if request.senior_nom and len(request.senior_nom.split()) > 1 else (request.senior_nom or "")
                },
                score_comid=request.score if request.type_eval == "entree" else 0,
                niveau_comid=request.niveau if request.type_eval == "entree" else "",
                structures_orientations=[],
                details_complet={"createur": request.createur or "Anonyme", "historique_orientations": []},
                dossier_id=cleaned_id
            )

    eval_id = db_manager.save_comid_eval(
        dossier_id=d_id,
        senior_nom=request.senior_nom,
        type_eval=request.type_eval,
        score=request.score,
        niveau=request.niveau,
        criteres=request.criteres,
        createur=request.createur
    )
    return {"message": "Évaluation COMID enregistrée avec succès !", "id": eval_id, "dossier_id": d_id}

@app.get("/api/comid/evaluations")
def get_comid_evaluations():
    """Récupère la liste de toutes les évaluations COMID (Entrée et Sortie)."""
    return db_manager.get_comid_evaluations()

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
        val = data.get("usager.localisation.commune_residence", "") or data.get("ville", "")
        return normalize_commune(val)

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
        score = dossier.get("score_comid")
        if score is not None:
            try:
                score_int = int(score)
                if score_int <= 5:
                    return "Non complexe"
                elif score_int <= 10:
                    return "Complexe"
                else:
                    return "Très complexe"
            except (ValueError, TypeError):
                pass
        val = str(dossier.get("niveau_comid", ""))
        if "Validé - " in val:
            val = val.replace("Validé - ", "").strip()
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
    """Extrait l'unique structure retenue (celle validée par le professionnel ou la 1ère recommandation)."""
    details = dossier.get("details_complet") or {}
    if isinstance(details, dict) and details.get("validation_utilisateur"):
        val_info = details["validation_utilisateur"]
        status = str(val_info.get("status", ""))
        if "Validé - " in status:
            selected_type = status.replace("Validé - ", "").strip()
            if selected_type:
                return [selected_type]

    niveau = str(dossier.get("niveau_comid") or "")
    if "Validé - " in niveau:
        selected_type = niveau.replace("Validé - ", "").strip()
        if selected_type:
            return [selected_type]

    structs = dossier.get("structures_orientations", [])
    if isinstance(structs, list) and len(structs) > 0:
        s0 = structs[0]
        if isinstance(s0, dict):
            st = s0.get("structure_type") or s0.get("label") or "Inconnu"
            return [st]
        elif isinstance(s0, str) and s0.strip():
            return [s0.strip()]

    return ["Inconnu"]


def matches_user_status(creator_name: Optional[str], status_role: Optional[str]) -> bool:
    if not status_role or str(status_role).lower() in ("all", "tous", "toutes", ""):
        return True
    c_lower = (creator_name or "").lower()
    s_lower = str(status_role).lower()
    if s_lower == "dac":
        return "durand" in c_lower or "dac" in c_lower
    elif s_lower == "pro":
        return "dupont" in c_lower or "dr" in c_lower or "sante" in c_lower or "santé" in c_lower or "pro" in c_lower
    elif s_lower in ("usager", "aidant"):
        return "martin" in c_lower or "bernard" in c_lower or "usager" in c_lower or "aidant" in c_lower or "patient" in c_lower or c_lower == "" or c_lower == "anonyme"
    return True

@app.get("/api/dashboard/sankey")
def get_sankey_data(dim1: str = "commune", dim2: str = "complexite", dim3: str = "structure", createur: Optional[str] = None, status_role: Optional[str] = None):
    """Construit les données du diagramme de Sankey à partir de la BDD.
    Les 3 dimensions sont configurables via les paramètres dim1, dim2, dim3.
    """
    all_dossiers = db_manager.get_all_dossiers()

    # Filtrer par créateur ou statut si spécifié
    dossiers = []
    for d in all_dossiers:
        details = d.get("details_complet") or {}
        if isinstance(details, str):
            try: details = json.loads(details)
            except: details = {}
        c_name = details.get("createur") if isinstance(details, dict) else None
        
        if createur and str(createur).lower() not in ("all", "anonyme", "tous", "toutes", ""):
            if not (c_name and c_name.lower() == createur.lower()):
                continue
        if status_role and not matches_user_status(c_name, status_role):
            continue
            
        dossiers.append(d)

    # Exclure impérativement les dossiers sans commune renseignée pour le Sankey (pas d'inconnus)
    valid_sankey_dossiers = []
    for d in dossiers:
        data = d.get("donnees_extraites", {})
        if isinstance(data, dict):
            raw_c = data.get("usager.localisation.commune_residence", "") or data.get("ville", "")
            norm_c = normalize_commune(raw_c)
            if norm_c and norm_c.lower() not in ("inconnue", "commune inconnue", "inconnu"):
                valid_sankey_dossiers.append(d)

    # --- KPIs (calculés sur les dossiers valides) ---
    total = len(valid_sankey_dossiers)
    scores = [d["score_comid"] for d in valid_sankey_dossiers if d.get("score_comid") is not None]
    score_moyen = sum(scores) / len(scores) if scores else None

    communes = []
    all_structure_types = []
    niveaux = []

    for d in valid_sankey_dossiers:
        data = d.get("donnees_extraites", {})
        if isinstance(data, dict):
            raw_c = data.get("usager.localisation.commune_residence", "") or data.get("ville", "")
            communes.append(normalize_commune(raw_c))

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

    for d in valid_sankey_dossiers:
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
                    # Ne pas inclure de nœuds Inconnus
                    if "inconnu" not in src.lower() and "inconnu" not in tgt.lower():
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

class ExtractFieldsRequest(BaseModel):
    text: str
    structure: Optional[str] = "DAC Var Ouest"

@app.post("/api/orientation/extract_fields")
async def extract_orientation_fields(request: ExtractFieldsRequest):
    """Extrait les champs structurés pour le pré-remplissage interactif d'une fiche d'orientation."""
    try:
        struct_lower = (request.structure or "").lower()
        if "dac" in struct_lower:
            extracted = await fiche_extractor.extract_for_dac(request.text)
        else:
            extracted = await fiche_extractor.extract_for_clic(request.text)
        return {"success": True, "data": extracted}
    except Exception as e:
        print(f"Erreur extract_orientation_fields: {e}")
        return {"success": False, "error": str(e), "data": {}}

def save_pdf_to_dossier(dossier_id: str, filename: str, pdf_bytes: bytes):
    """Enregistre le fichier PDF physique dans le répertoire du dossier patient et évite les doublons."""
    dossier_dir = os.path.join(STORAGE_DIR, str(dossier_id))
    os.makedirs(dossier_dir, exist_ok=True)
    
    # Supprimer d'éventuels doublons précédents pour la même fiche
    prefix = filename.rsplit("_dossier_", 1)[0] if "_dossier_" in filename else filename.rsplit(".", 1)[0]
    for existing in os.listdir(dossier_dir):
        if existing.startswith(prefix) and existing.endswith(".pdf"):
            try:
                os.remove(os.path.join(dossier_dir, existing))
            except Exception as e:
                print(f"Erreur suppression ancien PDF {existing}: {e}")

    file_path = os.path.join(dossier_dir, filename)
    with open(file_path, "wb") as f:
        f.write(pdf_bytes)

async def get_or_create_dossier_for_fiche(dossier_id: Optional[str], text: str, createur: str, structure_type: str) -> str:
    """Assure qu'un dossier patient existe en BDD et retourne son ID.
    Si le dossier est créé directement depuis une fiche d'orientation, on laisse l'historique d'orientation vide."""
    cleaned_id = clean_dossier_id(dossier_id)
    if cleaned_id is None:
        # Extraction des données via l'IA
        if "dac" in structure_type.lower():
            extracted_data = await fiche_extractor.extract_for_dac(text)
        else:
            extracted_data = await fiche_extractor.extract_for_clic(text)
        
        val_data = {
            "status": f"Fiche téléchargée ({structure_type})",
            "structure_choisie": structure_type,
            "date_validation": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        details = {
            "createur": createur,
            "orientation_results": [],
            "orientation_with_contacts": [],
            "validation_utilisateur": val_data,
            "historique_orientations": [] # Laissé vide pour ne pas créer de faux panneau d'orientation
        }
        
        new_id = db_manager.save_dossier(
            texte_original="", # Laissé vide
            donnees_extraites=extracted_data,
            score_comid=0,
            niveau_comid=f"Validé - {structure_type}",
            structures_orientations=[], # Laissé vide
            details_complet=details
        )
        return str(new_id)
    else:
        db_manager.update_dossier_validation(cleaned_id, f"Acceptée ({structure_type})", structure_type)
        return str(cleaned_id)

async def process_and_save_fiche_pdf(request: AnalyzeRequest, structure_type: str, pdf_generator_func, filename_prefix: str):
    """
    Helper pour extraire les données, générer le PDF, l'enregistrer dans le dossier
    patient (créé automatiquement si c'est un nouveau dossier) et renvoyer le PDF.
    """
    # 1. Obtenir ou créer le dossier patient
    dossier_id = await get_or_create_dossier_for_fiche(request.dossier_id, request.text, request.createur, structure_type)
    
    # 2. Extraire les données selon le type
    if "dac" in structure_type.lower():
        extracted_data = await fiche_extractor.extract_for_dac(request.text)
    else:
        extracted_data = await fiche_extractor.extract_for_clic(request.text)
        
    # 3. Générer les bytes du PDF
    pdf_bytes = pdf_generator_func(extracted_data)
    
    # 4. Enregistrer physiquement le PDF dans le dossier
    filename = f"fiche_orientation_{filename_prefix}_dossier_{dossier_id}.pdf"
    save_pdf_to_dossier(dossier_id, filename, pdf_bytes)

    # 5. Synchroniser le dossier patient en Base de Données avec les modifications/extractions de la fiche
    try:
        d_id_int = clean_dossier_id(dossier_id)
        if d_id_int is not None:
            dossier_360 = db_manager.get_dossier_360_details(str(d_id_int))
            if dossier_360 and dossier_360.get("orientation"):
                existing_details = dossier_360["orientation"].get("details_complet") or {}
                if isinstance(existing_details, str):
                    try: existing_details = json.loads(existing_details)
                    except: existing_details = {}
                existing_details["raw_text"] = request.text
                existing_details["fiche_extracted_data"] = extracted_data
                
                old_data = dossier_360["orientation"].get("donnees_extraites") or {}
                if isinstance(old_data, str):
                    try: old_data = json.loads(old_data)
                    except: old_data = {}
                merged_data = {**old_data, **extracted_data}

                db_manager.update_dossier(
                    dossier_id=d_id_int,
                    texte_original=dossier_360["orientation"].get("texte_original") or extractor.anonymizer.pseudonymize(request.text),
                    donnees_extraites=merged_data,
                    score_comid=dossier_360["orientation"].get("score_comid") or 0,
                    niveau_comid=dossier_360["orientation"].get("niveau_comid") or f"Validé - {structure_type}",
                    structures_orientations=dossier_360["orientation"].get("structures_orientations") or [],
                    details_complet=existing_details
                )
    except Exception as e:
        print(f"Erreur mise à jour BDD dossier patient lors du PDF: {e}")
    
    # 6. Renvoyer la réponse avec l'ID du dossier dans les headers
    return Response(
        content=pdf_bytes,
        media_type="application/pdf",
        headers={
            "Content-Disposition": f'inline; filename="{filename}"',
            "X-Dossier-ID": str(dossier_id),
            "Access-Control-Expose-Headers": "X-Dossier-ID"
        }
    )

@app.post("/api/orientation/dac/generate_pdf")
async def generate_dac_pdf(request: AnalyzeRequest):
    try:
        return await process_and_save_fiche_pdf(request, "DAC Var Ouest", pdf_generator.generate_dac_pdf, "dac")
    except Exception as e:
        return {"error": f"Erreur lors de la génération du PDF : {str(e)}"}

@app.post("/api/orientation/clic/generate_pdf")
async def generate_clic_pdf(request: AnalyzeRequest):
    try:
        return await process_and_save_fiche_pdf(request, "CLIC La Seyne", pdf_generator.generate_clic_pdf, "clic_laseyne")
    except Exception as e:
        return {"error": f"Erreur lors de la génération du PDF : {str(e)}"}

@app.post("/api/orientation/clic_toulon/generate_pdf")
async def generate_clic_toulon_pdf(request: AnalyzeRequest):
    try:
        return await process_and_save_fiche_pdf(request, "CLIC Toulon", pdf_generator.generate_clic_toulon_pdf, "clic_toulon")
    except Exception as e:
        return {"error": f"Erreur lors de la génération du PDF : {str(e)}"}


@app.post("/api/orientation/clic_provence_verte/generate_pdf")
async def generate_clic_provence_verte_pdf(request: AnalyzeRequest):
    try:
        return await process_and_save_fiche_pdf(request, "CLIC Provence Verte", pdf_generator._fill_clic_provence_verte, "clic_provence_verte")
    except Exception as e:
        return {"error": f"Erreur lors de la génération du PDF : {str(e)}"}

@app.post("/api/orientation/clic_hadage/generate_pdf")
async def generate_clic_hadage_pdf(request: AnalyzeRequest):
    try:
        return await process_and_save_fiche_pdf(request, "CLIC Hadage", pdf_generator._fill_clic_hadage, "clic_hadage")
    except Exception as e:
        return {"error": f"Erreur lors de la génération du PDF : {str(e)}"}

@app.get("/api/dossiers/{dossier_id}/pdf/{structure_type}")
async def generate_dossier_orientation_pdf(dossier_id: int, structure_type: str):
    """
    Génère ou sert la fiche d'orientation PDF pour un dossier existant.
    """
    try:
        struct_lower = structure_type.lower()
        if "dac" in struct_lower:
            prefix = "dac"
        elif "toulon" in struct_lower:
            prefix = "clic_toulon"
        elif "provence" in struct_lower:
            prefix = "clic_provence_verte"
        elif "hadage" in struct_lower:
            prefix = "clic_hadage"
        elif "seyne" in struct_lower or "clic" in struct_lower:
            prefix = "clic_laseyne"
        else:
            prefix = struct_lower

        filename = f"fiche_orientation_{prefix}_dossier_{dossier_id}.pdf"
        saved_file_path = os.path.join(STORAGE_DIR, str(dossier_id), filename)

        # Si le fichier existe déjà physiquement sur le disque, on le sert directement inline
        if os.path.exists(saved_file_path):
            with open(saved_file_path, "rb") as f:
                pdf_bytes = f.read()
            return Response(
                content=pdf_bytes,
                media_type="application/pdf",
                headers={"Content-Disposition": f'inline; filename="{filename}"'}
            )

        # 1. Récupération des données du dossier
        dossier_details = db_manager.get_dossier_360_details(str(dossier_id))
        if not dossier_details or not dossier_details.get("orientation"):
            return {"error": "Dossier introuvable"}
        
        details_complet = dossier_details["orientation"].get("details_complet") or {}
        texte_original = details_complet.get("raw_text") or dossier_details["orientation"].get("texte_original") or ""
        if not texte_original:
            return {"error": "Aucun texte d'orientation disponible pour ce dossier"}

        # 2. Extraction des champs et génération selon la structure demandée
        if "dac" in struct_lower:
            extracted = await fiche_extractor.extract_for_dac(texte_original)
            pdf_bytes = pdf_generator.generate_dac_pdf(extracted)
        elif "toulon" in struct_lower:
            extracted = await fiche_extractor.extract_for_clic(texte_original)
            pdf_bytes = pdf_generator.generate_clic_toulon_pdf(extracted)
        elif "provence" in struct_lower:
            extracted = await fiche_extractor.extract_for_clic(texte_original)
            pdf_bytes = pdf_generator._fill_clic_provence_verte(extracted)
        elif "hadage" in struct_lower:
            extracted = await fiche_extractor.extract_for_clic(texte_original)
            pdf_bytes = pdf_generator._fill_clic_hadage(extracted)
        else:
            extracted = await fiche_extractor.extract_for_clic(texte_original)
            pdf_bytes = pdf_generator.generate_clic_pdf(extracted)

        save_pdf_to_dossier(str(dossier_id), filename, pdf_bytes)

        return Response(
            content=pdf_bytes,
            media_type="application/pdf",
            headers={"Content-Disposition": f'inline; filename="{filename}"'}
        )
    except Exception as e:
        return {"error": f"Erreur lors de la génération du PDF : {str(e)}"}

@app.get("/api/dossiers")
def get_all_dossiers_summary(createur: Optional[str] = None):
    """
    Récupère la liste résumée de tous les dossiers patients avec indicateurs de grilles 
    et fiches d'orientation, en fusionnant les tables dossiers, comid et zarit, 
    et en filtrant selon le créateur.
    """
    try:
        dossiers = db_manager.get_all_dossiers()
        comids = db_manager.get_comid_evaluations()
        zarits = db_manager.get_zarit_evaluations()
        
        dossier_map = {}
        
        # 1. Insérer d'abord les dossiers d'orientations patients
        for d in dossiers:
            details_complet = d.get("details_complet") or {}
            if isinstance(details_complet, str):
                try: details_complet = json.loads(details_complet)
                except: details_complet = {}
            d_createur = details_complet.get("createur") if isinstance(details_complet, dict) else None
            
            if createur and d_createur and str(d_createur).lower() != "anonyme" and d_createur != createur:
                continue
                
            d_id = str(d["id"])
            senior_nom = "Anonyme"
            senior_prenom = ""
            age = None
            sexe = None

            if isinstance(details_complet, dict):
                senior_prenom = details_complet.get("senior_prenom", "")
                nom = details_complet.get("senior_nom", "")
                if senior_prenom or nom:
                    senior_nom = f"{senior_prenom} {nom}".strip()
                age = details_complet.get("age")
                sexe = details_complet.get("sexe")

            dEx = d.get("donnees_extraites") or {}
            if isinstance(dEx, str):
                try: dEx = json.loads(dEx)
                except: dEx = {}

            if senior_nom == "Anonyme" and isinstance(dEx, dict):
                nom_u = dEx.get("usager.identite.nom") or dEx.get("usager_nom_usage") or ""
                prenom_u = dEx.get("usager.identite.prenom") or dEx.get("usager_prenoms") or ""
                if nom_u or prenom_u:
                    senior_nom = f"{prenom_u} {nom_u}".strip()
                    senior_prenom = prenom_u
                if not age:
                    age = dEx.get("usager.identite.age_estime")
                if not sexe:
                    sexe = dEx.get("usager.identite.sexe")
                
            validation_status = "En attente"
            val_user = details_complet.get("validation_utilisateur") if isinstance(details_complet, dict) else None
            if val_user:
                val_status = val_user.get("status", "")
                if "valid" in val_status.lower() or "accept" in val_status.lower():
                    validation_status = "Accepté"
                else:
                    validation_status = "Refusé"

            structs = d.get("structures_orientations", [])
            has_orientation = bool(structs and len(structs) > 0 or (d.get("texte_original") and d.get("texte_original").strip() != ""))

            dossier_map[d_id] = {
                "dossier_id": d_id,
                "senior_nom": senior_nom,
                "senior_prenom": senior_prenom,
                "age": age,
                "sexe": sexe,
                "has_orientation": has_orientation,
                "has_comid": False,
                "has_zarit": False,
                "score_comid": d.get("score_comid"),
                "niveau_comid": d.get("niveau_comid"),
                "structures": [s.get("type") or s.get("nom") for s in structs if isinstance(s, dict)],
                "validation_status": validation_status,
                "is_archived": bool(d.get("is_archived", 0)),
                "date_modification": d.get("date_modification") or d.get("date_creation") or "",
                "zarits_info": []
            }
            
        # 2. Insérer/Fusionner les dossiers créés depuis les évaluations COMID
        for c in comids:
            c_d_id = str(c["dossier_id"])
            cleaned_c_d_id = clean_dossier_id(c_d_id)
            d_id = str(cleaned_c_d_id) if cleaned_c_d_id is not None else c_d_id
            d_createur = c.get("createur")
            
            if createur and d_createur and str(d_createur).lower() != "anonyme" and d_createur != createur:
                continue
                
            if d_id not in dossier_map:
                dossier_map[d_id] = {
                    "dossier_id": d_id,
                    "senior_nom": c.get("senior_nom") or "Anonyme",
                    "senior_prenom": "",
                    "age": None,
                    "sexe": None,
                    "has_orientation": False,
                    "has_comid": True,
                    "has_zarit": False,
                    "score_comid": c.get("score"),
                    "niveau_comid": c.get("niveau"),
                    "structures": [],
                    "validation_status": "En attente",
                    "is_archived": False,
                    "date_modification": c.get("date_creation") or "",
                    "zarits_info": []
                }
            else:
                dossier_map[d_id]["has_comid"] = True
                if c.get("score") is not None:
                    dossier_map[d_id]["score_comid"] = c.get("score")
                    dossier_map[d_id]["niveau_comid"] = c.get("niveau")
                if c.get("senior_nom") and dossier_map[d_id]["senior_nom"] == "Anonyme":
                    dossier_map[d_id]["senior_nom"] = c.get("senior_nom")
                if c.get("date_creation") and c.get("date_creation") > dossier_map[d_id]["date_modification"]:
                    dossier_map[d_id]["date_modification"] = c.get("date_creation")
                    
        # 3. Insérer/Fusionner les dossiers créés depuis les évaluations ZARIT
        for z in zarits:
            z_d_id = str(z["dossier_id"]) if z.get("dossier_id") else ""
            if not z_d_id:
                continue
            cleaned_z_d_id = clean_dossier_id(z_d_id)
            d_id = str(cleaned_z_d_id) if cleaned_z_d_id is not None else z_d_id
            d_createur = z.get("createur")
            
            if createur and d_createur and str(d_createur).lower() != "anonyme" and d_createur != createur:
                continue

            z_info = {
                "aidant_nom": z.get("aidant_nom") or "Aidant",
                "aidant_lien": z.get("aidant_lien") or "",
                "score": z.get("score"),
                "niveau": z.get("niveau"),
                "date_creation": z.get("date_creation")
            }
                
            if d_id not in dossier_map:
                dossier_map[d_id] = {
                    "dossier_id": d_id,
                    "senior_nom": z.get("senior_nom") or "Anonyme",
                    "senior_prenom": "",
                    "age": None,
                    "sexe": None,
                    "has_orientation": False,
                    "has_comid": False,
                    "has_zarit": True,
                    "score_comid": None,
                    "niveau_comid": None,
                    "structures": [],
                    "validation_status": "En attente",
                    "is_archived": False,
                    "date_modification": z.get("date_creation") or "",
                    "zarits_info": [z_info]
                }
            else:
                dossier_map[d_id]["has_zarit"] = True
                dossier_map[d_id]["zarits_info"].append(z_info)
                if z.get("senior_nom") and dossier_map[d_id]["senior_nom"] == "Anonyme":
                    dossier_map[d_id]["senior_nom"] = z.get("senior_nom")
                if z.get("date_creation") and z.get("date_creation") > dossier_map[d_id]["date_modification"]:
                    dossier_map[d_id]["date_modification"] = z.get("date_creation")

        result = list(dossier_map.values())
        # Trier par date_modification descendant (plus récent en haut)
        result.sort(key=lambda item: item.get("date_modification") or "", reverse=True)
        return result
    except Exception as e:
        return {"error": f"Erreur de fusion : {str(e)}"}

@app.post("/api/dossiers/{dossier_id}/archive")
def archive_dossier_endpoint(dossier_id: str):
    """Archive un dossier patient."""
    cleaned_id = clean_dossier_id(dossier_id)
    if cleaned_id is None:
        return {"error": "Dossier introuvable."}
    success = db_manager.toggle_archive_dossier(cleaned_id, archive=True)
    if not success:
        return {"error": "Dossier introuvable."}
    return {"success": True, "message": "Dossier archivé avec succès !"}

@app.post("/api/dossiers/{dossier_id}/unarchive")
def unarchive_dossier_endpoint(dossier_id: str):
    """Désarchive un dossier patient."""
    cleaned_id = clean_dossier_id(dossier_id)
    if cleaned_id is None:
        return {"error": "Dossier introuvable."}
    success = db_manager.toggle_archive_dossier(cleaned_id, archive=False)
    if not success:
        return {"error": "Dossier introuvable."}
    return {"success": True, "message": "Dossier restauré avec succès !"}

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


# --- Page & Routes Grille ZARIT ---

class ZaritEvalRequest(BaseModel):
    dossier_id: Optional[str] = None
    senior_nom: Optional[str] = "Senior non renseigné"
    aidant_nom: Optional[str] = "Aidant"
    aidant_lien: Optional[str] = ""
    score: int
    niveau: str
    reponses: list
    createur: Optional[str] = "Anonyme"

class ZaritPDFRequest(BaseModel):
    dossier_id: Optional[str] = None
    senior_nom: Optional[str] = "Senior non renseigné"
    aidant_nom: Optional[str] = "Aidant"
    aidant_lien: Optional[str] = ""
    score: int = 0
    niveau: str = "Charge faible"
    date: str = ""
    reponses: list = []

@app.get("/zarit", response_class=HTMLResponse)
def get_zarit_page():
    zarit_path = os.path.join(STATIC_DIR, "zarit.html")
    with open(zarit_path, "r", encoding="utf-8") as f:
        return HTMLResponse(content=f.read())

@app.get("/api/dossiers/dropdown-list")
def get_dossiers_dropdown_list(createur: Optional[str] = None):
    """Retourne la liste des dossiers pour les menus déroulants, filtrés par créateur."""
    try:
        summary = get_all_dossiers_summary(createur=createur)
        if isinstance(summary, dict) and "error" in summary:
            return []
        res = []
        for d in summary:
            res.append({
                "dossier_id": d["dossier_id"],
                "senior_nom": d["senior_nom"],
                "display_label": f"{d['dossier_id']} – {d['senior_nom']}"
            })
        return res
    except Exception:
        return []

@app.post("/api/zarit/evaluations")
def save_zarit_evaluation(req: ZaritEvalRequest):
    cleaned_id = clean_dossier_id(req.dossier_id)
    if cleaned_id is None:
        d_id_int = db_manager.save_dossier(
            texte_original="",
            donnees_extraites={
                "usager.identite.nom": req.senior_nom.split()[-1] if req.senior_nom else "",
                "usager.identite.prenom": " ".join(req.senior_nom.split()[:-1]) if req.senior_nom and len(req.senior_nom.split()) > 1 else (req.senior_nom or ""),
                "usager_nom_usage": req.senior_nom.split()[-1] if req.senior_nom else "",
                "usager_prenoms": " ".join(req.senior_nom.split()[:-1]) if req.senior_nom and len(req.senior_nom.split()) > 1 else (req.senior_nom or "")
            },
            score_comid=0,
            niveau_comid="",
            structures_orientations=[],
            details_complet={"createur": req.createur or "Anonyme", "historique_orientations": []}
        )
        d_id = str(d_id_int)
    else:
        d_id = str(cleaned_id)
        dossier_360 = db_manager.get_dossier_360_details(d_id)
        if not dossier_360 or not dossier_360.get("orientation"):
            db_manager.save_dossier(
                texte_original="",
                donnees_extraites={
                    "usager.identite.nom": req.senior_nom.split()[-1] if req.senior_nom else "",
                    "usager.identite.prenom": " ".join(req.senior_nom.split()[:-1]) if req.senior_nom and len(req.senior_nom.split()) > 1 else (req.senior_nom or ""),
                    "usager_nom_usage": req.senior_nom.split()[-1] if req.senior_nom else "",
                    "usager_prenoms": " ".join(req.senior_nom.split()[:-1]) if req.senior_nom and len(req.senior_nom.split()) > 1 else (req.senior_nom or "")
                },
                score_comid=0,
                niveau_comid="",
                structures_orientations=[],
                details_complet={"createur": req.createur or "Anonyme", "historique_orientations": []},
                dossier_id=cleaned_id
            )

    eval_id = db_manager.save_zarit_eval(
        senior_nom=req.senior_nom,
        aidant_nom=req.aidant_nom,
        score=req.score,
        niveau=req.niveau,
        reponses=req.reponses,
        dossier_id=d_id,
        createur=req.createur,
        aidant_lien=req.aidant_lien or ""
    )
    return {"status": "ok", "id": eval_id, "dossier_id": d_id}

@app.get("/api/zarit/evaluations")
def get_zarit_evaluations():
    return db_manager.get_zarit_evaluations()

@app.delete("/api/zarit/evaluations/{eval_id}")
def delete_zarit_evaluation(eval_id: int):
    success = db_manager.delete_zarit_eval(eval_id)
    return {"status": "ok" if success else "error"}

@app.post("/api/zarit/generate_pdf")
async def generate_zarit_pdf_endpoint(request: ZaritPDFRequest):
    try:
        pdf_bytes = pdf_generator.generate_zarit_pdf(request.dict())
        filename = f"Grille_Zarit_Score_{request.score}.pdf"
        return Response(
            content=pdf_bytes, 
            media_type="application/pdf", 
            headers={"Content-Disposition": f"attachment; filename={filename}"}
        )
    except Exception as e:
        return {"error": f"Erreur lors de la génération du PDF Zarit : {str(e)}"}

@app.get("/api/dossier-360/{dossier_id}")
def get_dossier_360_endpoint(dossier_id: str):
    cleaned_id = clean_dossier_id(dossier_id)
    if cleaned_id is None:
        return {"error": "Dossier introuvable"}
    
    details = db_manager.get_dossier_360_details(str(cleaned_id))
    # Lister les PDFs enregistrés physiquement sur le disque
    saved_pdfs = []
    dossier_dir = os.path.join(STORAGE_DIR, str(cleaned_id))
    if os.path.exists(dossier_dir):
        for f in os.listdir(dossier_dir):
            if f.lower().endswith(".pdf"):
                saved_pdfs.append(f)
    details["saved_pdfs"] = saved_pdfs
    return details

@app.get("/api/dossiers/{dossier_id}/saved-pdf/{filename}")
def download_saved_pdf(dossier_id: str, filename: str):
    file_path = os.path.join(STORAGE_DIR, str(dossier_id), filename)
    if not os.path.exists(file_path):
        return Response(content="Fichier introuvable.", status_code=404)
    return FileResponse(file_path, media_type="application/pdf", content_disposition_type="inline", filename=filename)

class PatientInfoUpdateRequest(BaseModel):
    senior_nom: Optional[str] = None
    senior_prenom: Optional[str] = None
    age: Optional[str] = None
    description: Optional[str] = None

@app.post("/api/dossiers/{dossier_id}/update-info")
def update_patient_info_endpoint(dossier_id: str, req: PatientInfoUpdateRequest):
    cleaned_id = clean_dossier_id(dossier_id)
    if cleaned_id is None:
        return {"error": "Dossier introuvable"}
    
    db_manager.update_dossier_patient_info(
        dossier_id=cleaned_id,
        senior_nom=req.senior_nom,
        senior_prenom=req.senior_prenom,
        age=req.age,
        description=req.description
    )
    return {"success": True, "message": "Informations usager mises à jour avec succès"}
