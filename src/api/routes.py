from fastapi import APIRouter, Query, HTTPException
from playwright.sync_api import sync_playwright

router = APIRouter()

@router.get("/hello")
async def hello():
    return {"message": "Hello from FastAPI!"}

@router.get("/extract")
async def extract(url: str = Query(..., description="Medium article URL")):
    if "medium.com" not in url:
        raise HTTPException(status_code=400, detail="Only Medium URLs are supported.")
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            page.goto(url, timeout=60000)
            page.wait_for_selector("article", timeout=15000)
            title = page.title()
            article = page.query_selector("article")
            content = article.inner_text() if article else "No article content found"
            browser.close()
        return {"title": title, "content": content[:2000]}  # Limit to 2000 chars
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error extracting article: {str(e)}")