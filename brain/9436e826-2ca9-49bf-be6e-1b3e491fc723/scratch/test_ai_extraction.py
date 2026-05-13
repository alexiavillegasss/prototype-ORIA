import httpx
import asyncio
import json

async def test_analyze():
    url = "http://localhost:8000/analyze"
    payload = {
        "text": "Ma mère de 85 ans vit seule à Toulon. Elle est tombée dans sa cuisine hier soir et elle est très confuse ce matin. Elle ne peut plus se déplacer seule."
    }
    
    print(f"Envoi de la requête à {url}...")
    async with httpx.AsyncClient(timeout=120.0) as client:
        response = await client.post(url, json=payload)
        if response.status_code == 200:
            print("Succès !")
            print(json.dumps(response.json(), indent=2, ensure_ascii=False))
        else:
            print(f"Erreur {response.status_code}: {response.text}")

if __name__ == "__main__":
    asyncio.run(test_analyze())
