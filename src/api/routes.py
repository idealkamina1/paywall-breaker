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
        # Try to extract main content
        article = soup.find("article")
        if article:
            text = article.get_text(separator="\n", strip=True)
        else:
            # Fallback: get all paragraphs
            paragraphs = soup.find_all("p")
            text = "\n".join([p.get_text(strip=True) for p in paragraphs])
        return {"title": title, "content": text[:2000]}  # Limit to 2000 chars
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))