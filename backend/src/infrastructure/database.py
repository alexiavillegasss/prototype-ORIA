import sqlite3
import json
from datetime import datetime
import os
from typing import Optional

class DatabaseManager:
    def __init__(self, db_path="oria_database.db"):
        """Initialise la connexion à la base de données SQLite."""
        # On s'assure que la base est créée à la racine du projet (ou là où le script est lancé)
        self.db_path = db_path
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
