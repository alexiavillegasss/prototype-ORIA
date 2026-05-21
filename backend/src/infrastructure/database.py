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
        """Crée la table 'dossiers_patients' si elle n'existe pas déjà."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            # Création de la table avec toutes nos colonnes
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
            conn.commit()

    def save_dossier(self, texte_original: str, donnees_extraites: dict, score_comid: int, niveau_comid: str, structures_orientations: list) -> Optional[int]:
        """Sauvegarde une nouvelle analyse dans la base et retourne son numéro de dossier (ID)."""
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
                    structures_orientations
                ) VALUES (?, ?, ?, ?, ?, ?)
            ''', (
                date_creation,
                texte_original,
                json.dumps(donnees_extraites, ensure_ascii=False),
                score_comid,
                niveau_comid,
                json.dumps(structures_orientations, ensure_ascii=False)
            ))
            conn.commit()
            return cursor.lastrowid # Retourne l'ID qui vient d'être créé

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
                except Exception:
                    pass
                result.append(dossier)
                
            return result
