import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[3]
SCHEMA_PATH = BASE_DIR / "config" / "schemas" / "schema_pivot.json"


def load_schema():

    if not SCHEMA_PATH.exists():
        raise FileNotFoundError(f"schema_pivot.json introuvable: {SCHEMA_PATH}")

    with open(SCHEMA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)