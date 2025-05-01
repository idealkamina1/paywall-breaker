from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from src.api.routes import router as api_router
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")

app = FastAPI()

@app.middleware("http")
async def api_key_middleware(request: Request, call_next):
    if request.url.path.startswith("/docs") or request.url.path.startswith("/openapi.json"):
        return await call_next(request)
    api_key = request.headers.get("x-api-key")
    if api_key != API_KEY:
        return JSONResponse(status_code=401, content={"detail": "Invalid or missing API Key"})
    return await call_next(request)

@app.get("/")
async def root():
    return {"message": "Welcome to your FastAPI Paywall Breaker!"}

app.include_router(api_router)

app.mount("/", StaticFiles(directory="src/static", html=True), name="static")