import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

def load_json(relative_path):
    full_path = os.path.join(BASE_DIR, relative_path)

    if not os.path.exists(full_path):
        raise FileNotFoundError(f"Fichier introuvable: {full_path}")

    with open(full_path, "r", encoding="utf-8") as f:
        return json.load(f)


def load_comid():
    return load_json("config/rules/COMID.json")


def load_orientation():
    return load_json("config/rules/orientation_rules.json")