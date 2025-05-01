from fastapi import FastAPI
from src.api.routes import router as api_router

app = FastAPI()

app.include_router(api_router)

# For local development only
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("src.app:app", host="0.0.0.0", port=8000, reload=True)