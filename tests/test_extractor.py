from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_extract_unauthorized():
    response = client.get("/extract?url=https://example.com")
    assert response.status_code == 401

def test_extract_authorized(monkeypatch):
    def mock_get(*args, **kwargs):
        class MockResponse:
            text = "<html><head><title>Test</title></head><body><article>Article text</article></body></html>"
            def raise_for_status(self): pass
        return MockResponse()
    import requests
    monkeypatch.setattr(requests, "get", mock_get)
    response = client.get(
        "/extract?url=https://example.com",
        headers={"x-api-key": "your_secret_api_key"}
    )
    assert response.status_code == 200
    assert response.json()["title"] == "Test"
    assert "Article text" in response.json()["content"]