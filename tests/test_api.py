from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_get_articles():
    response = client.get("/api/articles")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_article_by_id():
    response = client.get("/api/articles/1")
    assert response.status_code == 200
    assert "title" in response.json()
    assert "content" in response.json()

def test_create_article():
    response = client.post("/api/articles", json={"title": "Test Article", "content": "This is a test."})
    assert response.status_code == 201
    assert response.json()["title"] == "Test Article"

def test_invalid_article_creation():
    response = client.post("/api/articles", json={"title": "", "content": "This is a test."})
    assert response.status_code == 422

def test_user_authentication():
    response = client.post("/api/auth/login", json={"username": "testuser", "password": "testpass"})
    assert response.status_code == 200
    assert "access_token" in response.json()