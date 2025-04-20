from fastapi import APIRouter
from app.services.brapi_service import fetch_quote
from app.models.quote import QuoteResponse

router = APIRouter()

@router.get("/quote/{ticker}", response_model=QuoteResponse)
async def get_quote(ticker: str):
    quote = await fetch_quote(ticker)
    return quote

