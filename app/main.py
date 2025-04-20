from fastapi import FastAPI
from app.api import quote

app = FastAPI()

app.include_router(quote.router)
