import sqlite3
import json
from datetime import datetime
import os
from typing import Optional

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT_DB_PATH = os.path.join(BASE_DIR, "oria_database.db")

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
                    structures_orientations TEXT
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
            conn.commit()
            
            # Seeding automatique si la table dossiers_patients est vide
            cursor.execute('SELECT COUNT(*) FROM dossiers_patients')
            if cursor.fetchone()[0] == 0:
                self._seed_initial_patients(cursor)
                conn.commit()

    def _seed_initial_patients(self, cursor):
        """Remplit des données de démonstration réalistes pour le diagramme de Sankey."""
        demo_patients = [
            ("2026-08-17 10:15:00", "Mme Marie Durant, 82 ans, habite Toulon. Chutes répétées.", json.dumps({"usager.localisation.commune_residence": "Toulon", "usager.identite.age_estime": 82, "usager.situation_actuelle.beneficiaire_apa": "non", "usager.autonomie.gir_estime": 3, "ville": "Toulon", "age": 82}), 14, "Très complexe", json.dumps(["DAC", "CRT"])),
            ("2026-08-17 11:30:00", "M. Jean Dupont, 78 ans, Sanary-sur-Mer. Épuisement aidant.", json.dumps({"usager.localisation.commune_residence": "Sanary-sur-Mer", "usager.identite.age_estime": 78, "usager.situation_actuelle.beneficiaire_apa": "oui", "usager.autonomie.gir_estime": 2, "ville": "Sanary-sur-Mer", "age": 78}), 18, "Très complexe", json.dumps(["DAC", "CLIC"])),
            ("2026-08-17 14:20:00", "Mme Huguette Martin, 86 ans, La Seyne-sur-Mer. Aide ménagère.", json.dumps({"usager.localisation.commune_residence": "La Seyne-sur-Mer", "usager.identite.age_estime": 86, "usager.situation_actuelle.beneficiaire_apa": "non", "usager.autonomie.gir_estime": 5, "ville": "La Seyne-sur-Mer", "age": 86}), 4, "Non complexe", json.dumps(["CCAS", "PSCG_SS_APA"])),
            ("2026-08-17 16:05:00", "Mme Jeanne Fontaine, 74 ans, Hyères. Isolement social.", json.dumps({"usager.localisation.commune_residence": "Hyères", "usager.identite.age_estime": 74, "usager.situation_actuelle.beneficiaire_apa": "non", "usager.autonomie.gir_estime": 4, "ville": "Hyères", "age": 74}), 9, "Complexe", json.dumps(["CLIC", "CCAS"])),
            ("2026-08-18 09:10:00", "M. Robert Chen, 81 ans, La Valette. Troubles cognitifs.", json.dumps({"usager.localisation.commune_residence": "La Valette", "usager.identite.age_estime": 81, "usager.situation_actuelle.beneficiaire_apa": "oui", "usager.autonomie.gir_estime": 3, "ville": "La Valette", "age": 81}), 12, "Complexe", json.dumps(["CONSULTATION MÉMOIRE", "DAC"])),
            ("2026-08-18 10:45:00", "Mme Claire Vial, 69 ans, Ollioules. Sortie d'hospitalisation.", json.dumps({"usager.localisation.commune_residence": "Ollioules", "usager.identite.age_estime": 69, "usager.situation_actuelle.beneficiaire_apa": "non", "usager.autonomie.gir_estime": 4, "ville": "Ollioules", "age": 69}), 7, "Complexe", json.dumps(["PRADO", "CLIC"]))
        ]
        cursor.executemany('''
            INSERT INTO dossiers_patients 
            (date_creation, texte_original, donnees_extraites, score_comid, niveau_comid, structures_orientations)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', demo_patients)

    def save_dossier(self, texte_original: str, donnees_extraites: dict, score_comid: int, niveau_comid: str, structures_orientations: list, details_complet: dict = None) -> Optional[int]:
        """Sauvegarde une nouvelle analyse dans la base et retourne son numéro de dossier (ID).
        Le paramètre ``details_complet`` contient toutes les informations additionnelles d'orientation
        sous forme de dictionnaire qui sera sérialisé en JSON.
        """
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            date_creation = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            # SQLite ne stocke que du texte ou des nombres. 
            # On convertit donc nos dictionnaires Python en chaînes de texte JSON.
            cursor.execute('''
                INSERT INTO dossiers_patients (
                    date_creation,
                    texte_original,
                    donnees_extraites,
                    score_comid,
                    niveau_comid,
                    structures_orientations,
                    details_complet
                ) VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (
                date_creation,
                texte_original,
                json.dumps(donnees_extraites, ensure_ascii=False),
                score_comid,
                niveau_comid,
                json.dumps(structures_orientations, ensure_ascii=False),
                json.dumps(details_complet or {}, ensure_ascii=False)
            ))
            conn.commit()
            return cursor.lastrowid  # Retourne l'ID qui vient d'être créé

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

    def update_dossier_validation(self, dossier_id: int, status: str, structure_choisie: str) -> bool:
        """Met à jour le statut du dossier et la structure finale choisie par l'utilisateur."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            
            # On vérifie si le dossier existe
            cursor.execute('SELECT details_complet FROM dossiers_patients WHERE id = ?', (dossier_id,))
            row = cursor.fetchone()
            if not row:
                return False
                
            try:
                details = json.loads(row[0]) if row[0] else {}
            except Exception:
                details = {}
                
            details["validation_utilisateur"] = {
                "status": status,
                "structure_choisie": structure_choisie,
                "date_validation": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            
            # On met à jour details_complet et le statut (niveau_comid)
            cursor.execute('''
                UPDATE dossiers_patients 
                SET details_complet = ?, niveau_comid = ?
                WHERE id = ?
            ''', (json.dumps(details, ensure_ascii=False), status, dossier_id))
            conn.commit()
            return True

    def save_comid_eval(self, dossier_id: str, senior_nom: str, type_eval: str, score: int, niveau: str, criteres: list) -> int:
        """Sauvegarde une évaluation COMID (Entrée ou Sortie) dans la base."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            date_creation = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            cursor.execute('''
                INSERT INTO comid_evaluations (
                    dossier_id, senior_nom, type_eval, score, niveau, criteres_json, date_creation
                ) VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (
                dossier_id,
                senior_nom or "",
                type_eval,
                score,
                niveau,
                json.dumps(criteres or [], ensure_ascii=False),
                date_creation
            ))
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
        """Récupère la liste unique des dossiers ayant une évaluation d'entrée."""
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute('''
                SELECT DISTINCT dossier_id, senior_nom, score, date_creation
                FROM comid_evaluations
                WHERE type_eval = 'entree'
                ORDER BY date_creation DESC
            ''')
            return [dict(row) for row in cursor.fetchall()]

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
                d_id = item['dossier_id']
                if d_id not in dossiers_map:
                    dossiers_map[d_id] = {
                        "dossier_id": d_id,
                        "senior_nom": item.get('senior_nom') or d_id,
                        "entree": None,
                        "sortie": None
                    }
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

                comparisons.append({
                    "dossier_id": d_id,
                    "senior_nom": data['senior_nom'],
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
