import os
import sys
import asyncio

sys.path.append(os.path.join(os.getcwd(), 'backend', 'src'))

from fastapi.testclient import TestClient
from main import app

def run_tests():
    print("=== Testing API Endpoints for CASSI / Legacy Matrix Management ===")
    client = TestClient(app)
    
    # 1. GET /api/rules/matrices
    print("\n1. Testing GET /api/rules/matrices...")
    resp = client.get("/api/rules/matrices")
    assert resp.status_code == 200, f"Expected 200, got {resp.status_code}: {resp.text}"
    data = resp.json()
    print("Response matrices:", data)
    assert "matrices" in data
    assert len(data["matrices"]) == 2
    assert any(m["id"] == "cassi" and m["rules_count"] == 95 for m in data["matrices"])
    assert any(m["id"] == "legacy" and m["rules_count"] == 58 for m in data["matrices"])
    print("-> GET /api/rules/matrices OK!")

    # 2. POST /api/rules/switch to legacy
    print("\n2. Testing POST /api/rules/switch to 'legacy'...")
    resp = client.post("/api/rules/switch", json={"matrix": "legacy"})
    assert resp.status_code == 200, f"Expected 200, got {resp.status_code}: {resp.text}"
    data = resp.json()
    assert data["active_matrix"] == "legacy"
    print("Switched to:", data["active_matrix"])
    print("-> Switch to legacy OK!")

    # 3. POST /api/rules/switch back to cassi
    print("\n3. Testing POST /api/rules/switch back to 'cassi'...")
    resp = client.post("/api/rules/switch", json={"matrix": "cassi"})
    assert resp.status_code == 200, f"Expected 200, got {resp.status_code}: {resp.text}"
    data = resp.json()
    assert data["active_matrix"] == "cassi"
    print("Switched to:", data["active_matrix"])
    print("-> Switch to cassi OK!")

    # 4. POST /api/orientation/compare
    print("\n4. Testing POST /api/orientation/compare...")
    sample_text = (
        "Mme Dupont a 83 ans et habite à Toulon. Elle vit seule et a fait deux chutes ce mois-ci. "
        "Elle a de grosses difficultés pour faire ses courses, préparer ses repas et assurer sa toilette. "
        "Elle a une petite retraite et a besoin d'aide pour financer des aides à domicile."
    )
    resp = client.post("/api/orientation/compare", json={"text": sample_text})
    assert resp.status_code == 200, f"Expected 200, got {resp.status_code}: {resp.text}"
    comp_data = resp.json()
    
    print("\n=== Compare Results ===")
    top_leg = comp_data["legacy"]["results"][0]["structure_type"] if comp_data["legacy"]["results"] else "AUCUNE"
    print("Top Legacy Orientation:", top_leg)
    print("Legacy Needs Identified:", [n["detaille"] for n in comp_data["legacy"]["besoins_identifies"]])
    
    top_cas = comp_data["cassi"]["results"][0]["structure_type"] if comp_data["cassi"]["results"] else "AUCUNE"
    print("\nTop CASSI Orientation:", top_cas)
    print("CASSI Needs Identified:", [n["detaille"] for n in comp_data["cassi"]["besoins_identifies"]])
    
    # Check if CASSI items have CASSI fields
    cassi_items_with_prestation = [
        n for n in comp_data["cassi"]["besoins_identifies"]
        if n.get("cassi_prestation") or n.get("cassi_problematique")
    ]
    print(f"\nCASSI items with enriched nomenclature: {len(cassi_items_with_prestation)}/{len(comp_data['cassi']['besoins_identifies'])}")
    for item in cassi_items_with_prestation[:3]:
        print(f" - {item['detaille']} -> [{item.get('cassi_problematique')} > {item.get('cassi_besoin')}] Prestation: {item.get('cassi_prestation')}")

    print("\nALL API AND MATRIX SWITCH TESTS PASSED SUCCESSFULLY!")

if __name__ == "__main__":
    run_tests()
