from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_api_success():
    response = client.post(
        "/carbon/calculate",
        json={
            "vehicleType": "DIESEL",
            "distance": 100,
            "weight": 10,
            "efficiency": 2
        }
    )

    assert response.status_code == 200
    assert response.json()["co2"] == 50.0


def test_api_invalid_input():
    response = client.post(
        "/carbon/calculate",
        json={
            "vehicleType": "INVALID",
            "distance": 100,
            "weight": 10,
            "efficiency": 2
        }
    )

    assert response.status_code == 422  # FastAPI validation layer