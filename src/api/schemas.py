from pydantic import BaseModel
from typing import List, Optional

class ArticleSchema(BaseModel):
    title: str
    content: str
    images: Optional[List[str]] = None
    author: str
    published_date: str

class UserSchema(BaseModel):
    username: str
    email: str
    password: str

class ResponseSchema(BaseModel):
    success: bool
    message: str
    data: Optional[dict] = None

class ErrorSchema(BaseModel):
    success: bool
    error: str
    code: Optional[int] = None