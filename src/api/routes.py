from fastapi import APIRouter, Query, HTTPException
import requests
from bs4 import BeautifulSoup

router = APIRouter()

@router.get("/hello")
async def hello():
    return {"message": "Hello from FastAPI!"}

@router.get("/extract")
async def extract(url: str = Query(..., description="URL of the article")):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        title = soup.title.string if soup.title else "No title found"
        return {"title": title}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))