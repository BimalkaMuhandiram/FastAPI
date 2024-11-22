from fastapi.testclient import TestClient
from app import app
from unittest.mock import patch
import pytest

client = TestClient(app)

def test_predict_car_type():
    mock_prediction = ["Supercar"]
    with patch("app.model.predict", return_value=mock_prediction):
        response = client.post("/car/predict", json={"age": 21, "gender": 1})
        assert response.status_code == 200
        assert response.json() == {"prediction": "Supercar"}
