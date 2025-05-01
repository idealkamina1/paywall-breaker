from fastapi import APIRouter, Query, HTTPException
from playwright.sync_api import sync_playwright

router = APIRouter()

@router.get("/extract")
async def extract(url: str = Query(..., description="Medium article URL")):
    if "medium.com" not in url:
        raise HTTPException(status_code=400, detail="Only Medium URLs are supported.")
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
            page.goto(url, timeout=60000)
            page.wait_for_selector("article", timeout=15000)
            # Scroll to bottom to load all content
            page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
            page.wait_for_timeout(2000)
            title = page.title()
            article = page.query_selector("article")
            content = article.inner_text() if article else "No article content found"
            browser.close()
        return {"title": title, "content": content[:2000]}  # Limit to 2000 chars
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error extracting article: {str(e)}")