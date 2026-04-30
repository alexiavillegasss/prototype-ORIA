import json
from typing import Dict, Any, List
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[3]
COMID_PATH = BASE_DIR / "config" / "rules" / "COMID.json"

# =========================================================
# 2. LOAD REFERENTIAL
# =========================================================
def load_comid() -> Dict[str, Any]:
    """
    Charge le référentiel COMID de façon robuste
    """

    if not COMID_PATH.exists():
        raise FileNotFoundError(f"COMID.json introuvable: {COMID_PATH.resolve()}")

    with open(COMID_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


# =========================================================
# 3. MAIN ENGINE
# =========================================================
def compute_comid(signals: Dict[str, bool]) -> Dict[str, Any]:

    comid = load_comid()

    items = comid["items"]
    mapping = comid.get("mapping_signaux", {})

    score_total = 0
    score_by_domain = {}
    activated_items = []
    clinical_explanations = []

    # =====================================================
    # SCORING ENGINE
    # =====================================================
    for signal_name, signal_value in signals.items():

        if not signal_value:
            continue

        if signal_name not in mapping:
            continue

        for item_id in mapping[signal_name]:

            item = _get_item_by_id(items, item_id)

            if not item:
                continue

            domain = item.get("domaine", "unknown")
            weight = item.get("weight", 1)

            score_total += weight
            score_by_domain[domain] = score_by_domain.get(domain, 0) + weight

            activated_items.append({
                "item_id": item_id,
                "code": item.get("code"),
                "label": item.get("label"),
                "domain": domain,
                "weight": weight
            })

            clinical_explanations.append(
                f"[{domain}] {item.get('label')} → +{weight}"
            )

    # =====================================================
    # INTERPRETATION
    # =====================================================
    interpretation = _interpret_score(score_total)

    return {
        "referentiel": comid["referentiel"]["id"],

        "score": {
            "total": score_total,
            "by_domain": score_by_domain
        },

        "classification": interpretation,

        "clinical_summary": {
            "explanations": clinical_explanations,
            "nb_items_triggered": len(activated_items)
        },

        "activated_items": activated_items,

        "audit": {
            "traceability": True,
            "version": comid["referentiel"]["id"]
        }
    }


# =========================================================
# 4. HELPERS
# =========================================================
def _get_item_by_id(items: List[dict], item_id: str):
    return next((item for item in items if item["id"] == item_id), None)


def _interpret_score(score: int) -> Dict[str, str]:

    if score <= 5:
        return {
            "level": "non_complexe",
            "label": "Situation non complexe"
        }

    elif score <= 9:
        return {
            "level": "a_risque",
            "label": "Situation à risque de complexité"
        }

    else:
        return {
            "level": "complexe",
            "label": "Situation complexe"
        }