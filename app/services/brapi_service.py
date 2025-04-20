import os
import httpx
from dotenv import load_dotenv

load_dotenv()  # Carrega as variáveis do .env, se estiver usando python-dotenv

BRAPI_TOKEN = os.getenv("BRAPI_TOKEN")
BRAPI_URL = "https://brapi.dev/api/quote"

async def fetch_quote(ticker: str):
    if not BRAPI_TOKEN:
        raise RuntimeError("BRAPI_TOKEN não está definido")
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{BRAPI_URL}/{ticker}",
            params={"token": BRAPI_TOKEN},
            timeout=10.0
        )
        response.raise_for_status()
        return response.json()

