import os
import sys
import json
import pandas as pd

# Add backend/src to path
sys.path.append(os.path.join(os.getcwd(), 'backend', 'src'))

from application.orientation_engine import OrientationEngine
from application.scoring_engine import ScoringEngine

BASE_DIR = os.getcwd()
RULES_DIR = os.path.join(BASE_DIR, 'config', 'rules')
ORIENTATION_RULES_PATH = os.path.join(RULES_DIR, 'orientation_rules.json')
COMID_PATH = os.path.join(RULES_DIR, 'COMID.json')

engine_legacy = OrientationEngine(rules_path=ORIENTATION_RULES_PATH)
engine_legacy.excel_path = os.path.join(RULES_DIR, 'tableau_oria.xlsx')
engine_legacy._load_excel_rules()

engine_cassi = OrientationEngine(rules_path=ORIENTATION_RULES_PATH)
engine_cassi.excel_path = os.path.join(RULES_DIR, 'tableauORIA - NOMENCLATURE-CASSI.xlsx')
engine_cassi._load_excel_rules()

print(f"Legacy rules loaded: {len(engine_legacy.needs_mapping)} needs")
print(f"CASSI rules loaded: {len(engine_cassi.needs_mapping)} needs")
