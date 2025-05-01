from fastapi import APIRouter, HTTPException
from src.services.article_service import ArticleService
from src.services.user_service import UserService
from src.api.schemas import ArticleSchema, UserSchema

router = APIRouter()

article_service = ArticleService()
user_service = UserService()

@router.get("/articles/{article_id}", response_model=ArticleSchema)
async def get_article(article_id: str):
    article = article_service.fetch_article(article_id)
    if not article:
        raise HTTPException(status_code=404, detail="Article not found")
    return article

@router.post("/articles/", response_model=ArticleSchema)
async def create_article(article: ArticleSchema):
    new_article = article_service.save_article(article)
    return new_article

@router.post("/users/login", response_model=UserSchema)
async def login_user(user: UserSchema):
    authenticated_user = user_service.authenticate(user.username, user.password)
    if not authenticated_user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return authenticated_user

@router.get("/users/{user_id}", response_model=UserSchema)
async def get_user(user_id: str):
    user = user_service.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user