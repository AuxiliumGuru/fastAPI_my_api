import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_random_fact():
    response = client.get("/facts/random")
    assert response.status_code == 200
    assert "result" in response.json()
    assert "fact" in response.json()["result"]

def test_get_today_random_fact():
    response = client.get("/facts/today")
    assert response.status_code == 200
    assert "result" in response.json()
    assert "fact" in response.json()["result"]