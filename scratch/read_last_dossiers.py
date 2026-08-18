import sqlite3
import json

def read_db():
    conn = sqlite3.connect('oria_database.db')
    cursor = conn.cursor()
    # Check what tables exist
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    print("Tables:", tables)
    
    # Select last 5 rows from the main table (presumably 'dossiers' or similar)
    # Let's find columns in the table
    table_name = 'dossiers_patients'
    cursor.execute(f"PRAGMA table_info({table_name})")
    columns = cursor.fetchall()
    print(f"Columns in {table_name}:", [col[1] for col in columns])
    
    cursor.execute(f"SELECT id, texte_original, donnees_extraites, structures_orientations FROM {table_name} ORDER BY id DESC LIMIT 2")
    rows = cursor.fetchall()
    for r in rows:
        print("--- DOSSIER ---")
        print("ID:", r[0])
        print("Input Text:", r[1])
        print("Extracted Data:", r[2])
        print("Orientations:", r[3])
    conn.close()

if __name__ == "__main__":
    read_db()
