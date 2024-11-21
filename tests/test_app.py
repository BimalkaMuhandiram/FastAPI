from fastapi.testclient import TestClient
from main import app  # Make sure this import is correct

def test_read_main():
    client = TestClient(app)
    response = client.get("/")
    assert response.status_code == 200
