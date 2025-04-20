from pydantic import BaseModel, HttpUrl
from typing import List

class QuoteResult(BaseModel):
    currency: str
    marketCap: int
    shortName: str
    longName: str
    regularMarketChange: float
    regularMarketChangePercent: float
    regularMarketTime: str
    regularMarketPrice: float
    regularMarketDayHigh: float
    regularMarketDayRange: str
    regularMarketDayLow: float
    regularMarketVolume: int
    regularMarketPreviousClose: float
    regularMarketOpen: float
    fiftyTwoWeekRange: str
    fiftyTwoWeekLow: float
    fiftyTwoWeekHigh: float
    symbol: str
    priceEarnings: float
    earningsPerShare: float
    logourl: HttpUrl

class QuoteResponse(BaseModel):
    results: List[QuoteResult]
    requestedAt: str
    took: str
