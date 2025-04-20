import os
import httpx

BRAPI_TOKEN = os.getenv("BRAPI_TOKEN", "7mEUe4S1CcENwJyqN1c1hK")
BRAPI_URL = "https://brapi.dev/api/quote"

async def fetch_quote(ticker: str) -> dict:
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{BRAPI_URL}/{ticker}",
            params={"token": BRAPI_TOKEN}
        )
        return response.json()

