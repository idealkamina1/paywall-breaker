from fastapi import FastAPI
from src.api.routes import router as api_router

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to your FastAPI Paywall Breaker!"}

app.include_router(api_router)