from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_generate_password_valid_length():
    response = client.post("/generate_password", json={"length": 10})
    assert response.status_code == 200
    assert "password" in response.json()
    assert len(response.json()["password"]) == 10

def test_generate_password_invalid_length():
    response = client.post("/generate_password", json={"length": 0})
    assert response.status_code == 400
    assert response.json() == {"detail": "Password length must be greater than 0"}

def test_generate_password_negative_length():
    response = client.post("/generate_password", json={"length": -5})
    assert response.status_code == 400
    assert response.json() == {"detail": "Password length must be greater than 0"}

def test_test_password_valid():
    response = client.post("/test_password", json={"password": "validpassword123"})
    assert response.status_code == 200
    json_response = response.json()
    assert "entropy" in json_response
    assert "strength" in json_response

def test_test_password_empty():
    response = client.post("/test_password", json={"password": ""})
    assert response.status_code == 400
    assert response.json() == {"detail": "Password cannot be empty"}