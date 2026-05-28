import httpx
import json

class OllamaClient:
    def __init__(self, base_url="http://localhost:11434", model="llama3", temperature=0.0):
        self.base_url = base_url
        self.model = model
        self.temperature = temperature

    async def generate_json(self, prompt: str):
        url = f"{self.base_url}/api/generate"
        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False,
            "format": "json",
            "options": {
                "temperature": self.temperature
            }
        }
        
        async with httpx.AsyncClient(timeout=None) as client:
            response = await client.post(url, json=payload)
            response.raise_for_status()
            result = response.json()
            return json.loads(result["response"])
