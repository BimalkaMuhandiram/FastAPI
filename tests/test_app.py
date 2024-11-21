# tests/test_app.py
from fastapi.testclient import TestClient
from app.main import app  # Adjust according to your app's structure

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}  # Adjust based on your app
