import sqlite3
import json
from datetime import datetime
import os
from typing import Optional, Union

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT_DB_PATH = os.path.join(BASE_DIR, "oria_database.db")

def clean_id_str(d_id) -> str:
    if not d_id:
        return ""
    import re
    d_str = str(d_id).strip()
    digits = re.findall(r'\d+', d_str)
    if digits:
        return digits[0]
    return d_str

class DatabaseManager:
    def __init__(self, db_path=None):
        """Initialise la connexion à la base de données SQLite en garantissant un chemin absolu unique."""
        if db_path is None:
            db_path = DEFAULT_DB_PATH
        self.db_path = os.path.abspath(db_path)
        self._initialize_db()

    def _initialize_db(self):
        """Crée les tables 'dossiers_patients' et 'comid_evaluations' si elles n'existent pas."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            # Table dossiers patients
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS dossiers_patients (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    date_creation TEXT NOT NULL,
                    texte_original TEXT NOT NULL,
                    donnees_extraites TEXT NOT NULL,
                    score_comid INTEGER,
                    niveau_comid TEXT,
                    structures_orientations TEXT,
                    details_complet TEXT
                )
            ''')
            # Table comid_evaluations (Entrée / Sortie)
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS comid_evaluations (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    dossier_id TEXT NOT NULL,
                    senior_nom TEXT,
                    type_eval TEXT NOT NULL,
                    score INTEGER NOT NULL,
                    niveau TEXT NOT NULL,
                    criteres_json TEXT,
                    date_creation TEXT NOT NULL
                )
            ''')
            # Table zarit_evaluations (Grille Zarit - Fardeau de l'aidant)
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS zarit_evaluations (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    dossier_id TEXT,
                    senior_nom TEXT,
                    aidant_nom TEXT,
                    score INTEGER NOT NULL,
                    niveau TEXT NOT NULL,
                    reponses_json TEXT,
                    date_creation TEXT NOT NULL
                )
            ''')
            # Migration si la colonne details_complet manque dans dossiers_patients
            try:
                cursor.execute('ALTER TABLE dossiers_patients ADD COLUMN details_complet TEXT')
            except Exception:
                pass
            # Migration si la colonne dossier_id manque
            try:
                cursor.execute('ALTER TABLE zarit_evaluations ADD COLUMN dossier_id TEXT')
            except Exception:
                pass
            # Migration pour ajouter createur à comid_evaluations et zarit_evaluations
            try:
                cursor.execute('ALTER TABLE comid_evaluations ADD COLUMN createur TEXT')
            except Exception:
                pass
            try:
                cursor.execute('ALTER TABLE zarit_evaluations ADD COLUMN createur TEXT')
            except Exception:
                pass
            try:
                cursor.execute('ALTER TABLE dossiers_patients ADD COLUMN is_archived INTEGER DEFAULT 0')
            except Exception:
                pass
            try:
                cursor.execute('ALTER TABLE dossiers_patients ADD COLUMN date_modification TEXT')
            except Exception:
                pass
            try:
                cursor.execute('ALTER TABLE zarit_evaluations ADD COLUMN aidant_lien TEXT')
            except Exception:
                pass
            conn.commit()

    def save_dossier(self, texte_original: str, donnees_extraites: dict, score_comid: int, niveau_comid: str, structures_orientations: list, details_complet: dict = None, dossier_id: Optional[int] = None) -> Optional[int]:
        """Sauvegarde une nouvelle analyse dans la base et retourne son numéro de dossier (ID).
        Le paramètre ``details_complet`` contient toutes les informations additionnelles d'orientation
        sous forme de dictionnaire qui sera sérialisé en JSON.
        """
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            date_creation = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            date_modification = date_creation
            
            # SQLite ne stocke que du texte ou des nombres. 
            # On convertit donc nos dictionnaires Python en chaînes de texte JSON.
            if dossier_id is not None:
                cursor.execute('''
                    INSERT INTO dossiers_patients (
                        id,
                        date_creation,
                        date_modification,
                        texte_original,
                        donnees_extraites,
                        score_comid,
                        niveau_comid,
                        structures_orientations,
                        details_complet
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                ''', (
                    dossier_id,
                    date_creation,
                    date_modification,
                    texte_original,
                    json.dumps(donnees_extraites, ensure_ascii=False),
                    score_comid,
                    niveau_comid,
                    json.dumps(structures_orientations, ensure_ascii=False),
                    json.dumps(details_complet or {}, ensure_ascii=False)
                ))
            else:
                cursor.execute('''
                    INSERT INTO dossiers_patients (
                        date_creation,
                        date_modification,
                        texte_original,
                        donnees_extraites,
                        score_comid,
                        niveau_comid,
                        structures_orientations,
                        details_complet
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                ''', (
                    date_creation,
                    date_modification,
                    texte_original,
                    json.dumps(donnees_extraites, ensure_ascii=False),
                    score_comid,
                    niveau_comid,
                    json.dumps(structures_orientations, ensure_ascii=False),
                    json.dumps(details_complet or {}, ensure_ascii=False)
                ))
            conn.commit()
            return dossier_id if dossier_id is not None else cursor.lastrowid  # Retourne l'ID qui vient d'être créé

    def update_dossier(self, dossier_id: int, texte_original: str, donnees_extraites: dict, score_comid: int, niveau_comid: str, structures_orientations: list, details_complet: dict = None) -> bool:
        """Met à jour un dossier existant avec les nouvelles données d'orientation."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            date_modification = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            cursor.execute('''
                UPDATE dossiers_patients
                SET texte_original = ?, donnees_extraites = ?, score_comid = ?, niveau_comid = ?, structures_orientations = ?, details_complet = ?, date_modification = ?
                WHERE id = ?
            ''', (
                texte_original,
                json.dumps(donnees_extraites, ensure_ascii=False),
                score_comid,
                niveau_comid,
                json.dumps(structures_orientations, ensure_ascii=False),
                json.dumps(details_complet or {}, ensure_ascii=False),
                date_modification,
                dossier_id
            ))
            conn.commit()
            return cursor.rowcount > 0

    def get_all_dossiers(self):
        """Récupère tout l'historique des dossiers patients."""
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row # Permet d'avoir le nom des colonnes dans le résultat
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM dossiers_patients ORDER BY date_creation DESC')
            rows = cursor.fetchall()
            
            result = []
            for row in rows:
                dossier = dict(row)
                # On fait l'opération inverse : on transforme le texte stocké en dictionnaires Python
                try:
                    dossier['donnees_extraites'] = json.loads(dossier['donnees_extraites'])
                    dossier['structures_orientations'] = json.loads(dossier['structures_orientations'])
                    if dossier.get('details_complet'):
                        dossier['details_complet'] = json.loads(dossier['details_complet'])
                except Exception:
                    pass
                result.append(dossier)
                
            return result

    def update_dossier_validation(self, dossier_id: Union[int, str], status: str, structure_choisie: str) -> bool:
        """Met à jour le statut du dossier et la structure finale choisie par l'utilisateur."""
        clean_id = clean_id_str(str(dossier_id))
        try:
            d_id_int = int(clean_id)
        except (ValueError, TypeError):
            d_id_int = None

        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT details_complet FROM dossiers_patients WHERE id = ? OR id = ?', (d_id_int, clean_id))
            row = cursor.fetchone()
            if not row:
                return False
                
            try:
                details = json.loads(row[0]) if row[0] else {}
            except Exception:
                details = {}
                
            val_data = {
                "status": status,
                "structure_choisie": structure_choisie,
                "date_validation": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            details["validation_utilisateur"] = val_data
            if "historique_orientations" in details and isinstance(details["historique_orientations"], list) and len(details["historique_orientations"]) > 0:
                details["historique_orientations"][-1]["validation_utilisateur"] = val_data
            
            cursor.execute('''
                UPDATE dossiers_patients 
                SET details_complet = ?, niveau_comid = ?
                WHERE id = ? OR id = ?
            ''', (json.dumps(details, ensure_ascii=False), status, d_id_int, clean_id))
            conn.commit()
            return True

    def update_history_item_validation(self, dossier_id: Union[int, str], history_index: int, status: str, structure_choisie: str) -> bool:
        """Met à jour le statut de validation d'un élément spécifique de l'historique d'orientations."""
        clean_id = clean_id_str(str(dossier_id))
        try:
            d_id_int = int(clean_id)
        except (ValueError, TypeError):
            d_id_int = None

        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT details_complet FROM dossiers_patients WHERE id = ? OR id = ?', (d_id_int, clean_id))
            row = cursor.fetchone()
            if not row:
                return False

            try:
                details = json.loads(row[0]) if row[0] else {}
            except Exception:
                details = {}

            val_data = {
                "status": status,
                "structure_choisie": structure_choisie,
                "date_validation": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }

            historique = details.get("historique_orientations", [])
            if isinstance(historique, list) and 0 <= history_index < len(historique):
                historique[history_index]["validation_utilisateur"] = val_data
                if history_index == len(historique) - 1:
                    details["validation_utilisateur"] = val_data
                    status_col = status
                else:
                    status_col = details.get("validation_utilisateur", {}).get("status", status)

                cursor.execute('''
                    UPDATE dossiers_patients 
                    SET details_complet = ?, niveau_comid = ?
                    WHERE id = ? OR id = ?
                ''', (json.dumps(details, ensure_ascii=False), status_col, d_id_int, clean_id))
                conn.commit()
                return True
            return False

    def save_comid_eval(self, dossier_id: str, senior_nom: str, type_eval: str, score: int, niveau: str, criteres: list, createur: str = "Anonyme") -> int:
        """Sauvegarde ou met à jour une évaluation COMID (Entrée ou Sortie) pour un dossier_id."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            date_creation = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            criteres_str = json.dumps(criteres or [], ensure_ascii=False)

            cursor.execute('''
                SELECT id FROM comid_evaluations
                WHERE dossier_id = ? AND type_eval = ?
            ''', (dossier_id, type_eval))
            existing = cursor.fetchone()

            if existing:
                eval_id = existing[0]
                cursor.execute('''
                    UPDATE comid_evaluations
                    SET senior_nom = ?, score = ?, niveau = ?, criteres_json = ?, date_creation = ?, createur = ?
                    WHERE id = ?
                ''', (senior_nom or "", score, niveau, criteres_str, date_creation, createur, eval_id))
                conn.commit()
                return eval_id
            else:
                cursor.execute('''
                    INSERT INTO comid_evaluations (
                        dossier_id, senior_nom, type_eval, score, niveau, criteres_json, date_creation, createur
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                ''', (dossier_id, senior_nom or "", type_eval, score, niveau, criteres_str, date_creation, createur))
                conn.commit()
                return cursor.lastrowid

    def get_comid_evaluations(self):
        """Récupère toutes les évaluations COMID."""
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM comid_evaluations ORDER BY date_creation DESC')
            rows = cursor.fetchall()
            result = []
            for row in rows:
                item = dict(row)
                try:
                    item['criteres'] = json.loads(item['criteres_json'])
                except Exception:
                    item['criteres'] = []
                result.append(item)
            return result

    def get_entree_dossiers(self):
        """Récupère les dossiers avec évaluation d'entrée pour la liaison en sortie."""
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute('''
                SELECT e.dossier_id, e.senior_nom, e.score, e.criteres_json, e.date_creation
                FROM comid_evaluations e
                WHERE e.type_eval = 'entree'
                AND e.dossier_id NOT IN (
                    SELECT s.dossier_id FROM comid_evaluations s WHERE s.type_eval = 'sortie'
                )
                ORDER BY e.date_creation DESC
            ''')
            rows = cursor.fetchall()
            res = []
            for row in rows:
                item = dict(row)
                try:
                    item['criteres'] = json.loads(item['criteres_json'])
                except Exception:
                    item['criteres'] = []
                res.append(item)
            return res

    def get_comid_comparisons(self):
        """Calcule la comparaison Entrée vs Sortie pour chaque dossier."""
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM comid_evaluations ORDER BY date_creation ASC')
            rows = cursor.fetchall()

            dossiers_map = {}
            for row in rows:
                item = dict(row)
                d_id = clean_id_str(item['dossier_id'])
                s_nom = item.get('senior_nom')
                if not s_nom or s_nom == d_id or s_nom in ('Senior non renseigné', 'Usager'):
                    s_nom = 'Anonyme'
                if d_id not in dossiers_map:
                    dossiers_map[d_id] = {
                        "dossier_id": d_id,
                        "senior_nom": s_nom,
                        "entree": None,
                        "sortie": None
                    }
                elif s_nom != 'Anonyme':
                    dossiers_map[d_id]["senior_nom"] = s_nom

                if item['type_eval'] == 'entree':
                    dossiers_map[d_id]['entree'] = item
                elif item['type_eval'] == 'sortie':
                    dossiers_map[d_id]['sortie'] = item

            comparisons = []
            for d_id, data in dossiers_map.items():
                entree = data['entree']
                sortie = data['sortie']
                
                score_entree = entree['score'] if entree else None
                score_sortie = sortie['score'] if sortie else None
                
                delta = None
                evolution_pct = None
                if score_entree is not None and score_sortie is not None:
                    delta = score_entree - score_sortie  # positif = réduction de la complexité
                    if score_entree > 0:
                        evolution_pct = round((delta / score_entree) * 100, 1)

                createur_val = (entree and entree.get('createur')) or (sortie and sortie.get('createur')) or "Anonyme"
                comparisons.append({
                    "dossier_id": d_id,
                    "senior_nom": data['senior_nom'],
                    "createur": createur_val,
                    "score_entree": score_entree,
                    "niveau_entree": entree['niveau'] if entree else None,
                    "date_entree": entree['date_creation'] if entree else None,
                    "score_sortie": score_sortie,
                    "niveau_sortie": sortie['niveau'] if sortie else None,
                    "date_sortie": sortie['date_creation'] if sortie else None,
                    "delta_score": delta,
                    "evolution_pct": evolution_pct,
                    "statut_resolution": "Complète" if (entree and sortie) else "Seulement Entrée" if entree else "Seulement Sortie"
                })
            return comparisons

    def delete_comid_evaluations_by_dossier(self, dossier_id: str) -> bool:
        """Supprime toutes les évaluations COMID rattachées à un dossier_id."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM comid_evaluations WHERE dossier_id = ?', (dossier_id,))
            conn.commit()
            return cursor.rowcount > 0

    def save_zarit_eval(self, senior_nom: str, aidant_nom: str, score: int, niveau: str, reponses: list, dossier_id: str = None, createur: str = "Anonyme", aidant_lien: str = "") -> int:
        """Enregistre une évaluation de la grille de Zarit (Fardeau de l'aidant)."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            date_creation = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            cursor.execute('''
                INSERT INTO zarit_evaluations (dossier_id, senior_nom, aidant_nom, aidant_lien, score, niveau, reponses_json, date_creation, createur)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (dossier_id, senior_nom, aidant_nom, aidant_lien or "", score, niveau, json.dumps(reponses), date_creation, createur))
            if dossier_id:
                clean_id = clean_id_str(str(dossier_id))
                try:
                    d_id_int = int(clean_id)
                    cursor.execute('UPDATE dossiers_patients SET date_modification = ? WHERE id = ?', (date_creation, d_id_int))
                except (ValueError, TypeError):
                    pass
            conn.commit()
            return cursor.lastrowid

    def toggle_archive_dossier(self, dossier_id: Union[int, str], archive: bool = True) -> bool:
        """Archive ou désarchive un dossier patient."""
        clean_id = clean_id_str(str(dossier_id))
        try:
            d_id_int = int(clean_id)
        except (ValueError, TypeError):
            return False

        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            val = 1 if archive else 0
            date_modif = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            cursor.execute('UPDATE dossiers_patients SET is_archived = ?, date_modification = ? WHERE id = ?', (val, date_modif, d_id_int))
            conn.commit()
            return cursor.rowcount > 0

    def get_zarit_evaluations(self) -> list:
        """Récupère l'historique de toutes les évaluations de Zarit."""
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM zarit_evaluations ORDER BY date_creation DESC')
            rows = cursor.fetchall()
            return [dict(row) for row in rows]

    def delete_zarit_eval(self, eval_id: int) -> bool:
        """Supprime une évaluation de Zarit par son ID."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM zarit_evaluations WHERE id = ?', (eval_id,))
            conn.commit()
            return cursor.rowcount > 0

    def get_dossiers_for_dropdown(self) -> list:
        """Retourne la liste complète de tous les dossiers patients (dossiers, COMID, Zarit)."""
        res = []
        dossiers_map = {}

        # 1. Dossiers patients principaux
        for d in self.get_all_dossiers():
            d_id = str(d["id"])
            details_complet = d.get("details_complet") or {}
            if isinstance(details_complet, str):
                try: details_complet = json.loads(details_complet)
                except: details_complet = {}
            
            s_nom = "Anonyme"
            if isinstance(details_complet, dict):
                prenom = details_complet.get("senior_prenom", "")
                nom = details_complet.get("senior_nom", "")
                if prenom or nom:
                    s_nom = f"{prenom} {nom}".strip()
            
            if s_nom == "Anonyme":
                dEx = d.get("donnees_extraites") or {}
                if isinstance(dEx, str):
                    try: dEx = json.loads(dEx)
                    except: dEx = {}
                nom_u = dEx.get("usager.identite.nom") or dEx.get("usager_nom_usage") or ""
                prenom_u = dEx.get("usager.identite.prenom") or dEx.get("usager_prenoms") or ""
                if nom_u or prenom_u:
                    s_nom = f"{prenom_u} {nom_u}".strip()

            dossiers_map[d_id] = {
                "dossier_id": d_id,
                "senior_nom": s_nom
            }

        # 2. Dossiers COMID
        for item in self.get_comid_evaluations():
            c_d_id = str(item.get('dossier_id'))
            cleaned_c_d_id = clean_id_str(c_d_id)
            d_id = str(cleaned_c_d_id) if cleaned_c_d_id is not None else c_d_id
            s_nom = item.get('senior_nom')
            if not s_nom or s_nom == d_id or s_nom in ('Senior non renseigné', 'Usager'):
                s_nom = "Anonyme"
                
            if d_id not in dossiers_map:
                dossiers_map[d_id] = {
                    "dossier_id": d_id,
                    "senior_nom": s_nom
                }
            elif s_nom != "Anonyme" and dossiers_map[d_id]["senior_nom"] == "Anonyme":
                dossiers_map[d_id]["senior_nom"] = s_nom

        # 3. Dossiers ZARIT
        for item in self.get_zarit_evaluations():
            z_d_id = str(item.get('dossier_id'))
            cleaned_z_d_id = clean_id_str(z_d_id)
            d_id = str(cleaned_z_d_id) if cleaned_z_d_id is not None else z_d_id
            s_nom = item.get('senior_nom')
            if not s_nom or s_nom == d_id or s_nom in ('Senior non renseigné', 'Usager'):
                s_nom = "Anonyme"
                
            if d_id not in dossiers_map:
                dossiers_map[d_id] = {
                    "dossier_id": d_id,
                    "senior_nom": s_nom
                }
            elif s_nom != "Anonyme" and dossiers_map[d_id]["senior_nom"] == "Anonyme":
                dossiers_map[d_id]["senior_nom"] = s_nom

        def sort_key(k):
            try:
                return (0, int(clean_id_str(k)))
            except:
                return (1, str(k))

        for d_id in sorted(dossiers_map.keys(), key=sort_key):
            info = dossiers_map[d_id]
            nom = info["senior_nom"]
            res.append({
                "dossier_id": d_id,
                "senior_nom": nom,
                "display_label": f"Dossier #{d_id} – {nom}" if nom != "Anonyme" else f"Dossier #{d_id}"
            })

        return res

    def get_dossier_360_details(self, dossier_id: str) -> dict:
        """Récupère l'ensemble synthétique à 360° d'un dossier (Orientation, COMID, Zarit)."""
        clean_id = clean_id_str(str(dossier_id))
        try:
            d_id_int = int(clean_id)
        except (ValueError, TypeError):
            d_id_int = None
        d_id_str = str(clean_id)

        # 1. Orientation dossier info (dossiers_patients)
        orientation_info = None
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM dossiers_patients WHERE id = ? OR id = ?', (d_id_int, d_id_str))
            row = cursor.fetchone()
            if row:
                d = dict(row)
                try: d['donnees_extraites'] = json.loads(d['donnees_extraites'])
                except Exception: pass
                try: d['structures_orientations'] = json.loads(d['structures_orientations'])
                except Exception: pass
                try: d['details_complet'] = json.loads(d['details_complet'])
                except Exception: d['details_complet'] = {}
                
                details_complet = d['details_complet']
                if not isinstance(details_complet, dict):
                    details_complet = {}
                
                if "historique_orientations" not in details_complet:
                    if d.get("texte_original") or d.get("structures_orientations"):
                        details_complet["historique_orientations"] = [
                            {
                                "date": d.get("date_creation") or datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                                "texte_original": d.get("texte_original"),
                                "donnees_extraites": d.get("donnees_extraites"),
                                "structures_orientations": d.get("structures_orientations"),
                                "validation_utilisateur": details_complet.get("validation_utilisateur")
                            }
                        ]
                    else:
                        details_complet["historique_orientations"] = []
                
                d['details_complet'] = details_complet
                orientation_info = d

        # 2. COMID evaluations (entree & sortie)
        comid_evals = []
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute('''
                SELECT * FROM comid_evaluations 
                WHERE dossier_id = ? OR dossier_id = ? OR dossier_id = ? 
                ORDER BY date_creation ASC
            ''', (d_id_str, f"DOS-{d_id_str}", f"DOS-ZARIT-{d_id_str}"))
            rows = cursor.fetchall()
            for r in rows:
                item = dict(r)
                try: item['criteres'] = json.loads(item['criteres_json'])
                except Exception: item['criteres'] = []
                comid_evals.append(item)

        # 3. Zarit evaluations
        zarit_evals = []
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute('''
                SELECT * FROM zarit_evaluations 
                WHERE dossier_id = ? OR dossier_id = ? OR dossier_id = ? 
                ORDER BY date_creation DESC
            ''', (d_id_str, f"DOS-{d_id_str}", f"DOS-ZARIT-{d_id_str}"))
            rows = cursor.fetchall()
            for r in rows:
                item = dict(r)
                try: item['reponses'] = json.loads(item['reponses_json'])
                except Exception: item['reponses'] = []
                zarit_evals.append(item)

        return {
            "dossier_id": d_id_str,
            "orientation": orientation_info,
            "comid": comid_evals,
            "zarit": zarit_evals
        }

    def update_dossier_patient_info(self, dossier_id: int, senior_nom: str = None, senior_prenom: str = None, age: str = None, description: str = None) -> bool:
        """Met à jour les informations du profil usager (Nom, Prénom, Âge, Description)."""
        d_id_str = str(dossier_id)
        full_name = f"{senior_prenom or ''} {senior_nom or ''}".strip()
        if not full_name:
            full_name = senior_nom or ""

        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT details_complet FROM dossiers_patients WHERE id = ?', (dossier_id,))
            row = cursor.fetchone()
            if row:
                try:
                    details = json.loads(row[0]) if row[0] else {}
                except Exception:
                    details = {}
                
                details["senior_nom"] = senior_nom or details.get("senior_nom")
                details["senior_prenom"] = senior_prenom or details.get("senior_prenom")
                details["age"] = age or details.get("age")
                details["description_usager"] = description or details.get("description_usager")
                
                cursor.execute('UPDATE dossiers_patients SET details_complet = ? WHERE id = ?', (
                    json.dumps(details, ensure_ascii=False),
                    dossier_id
                ))
            
            if full_name:
                cursor.execute('UPDATE comid_evaluations SET senior_nom = ? WHERE dossier_id = ? OR dossier_id = ? OR dossier_id = ?', (
                    full_name, d_id_str, f"DOS-{d_id_str}", f"DOS-ZARIT-{d_id_str}"
                ))
            conn.commit()
            return True
