# tests/test_app.py
from fastapi.testclient import TestClient
from main import app  # Import the app from the correct location

def test_main():  # Ensure the function name starts with 'test_'
    client = TestClient(app)
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}
