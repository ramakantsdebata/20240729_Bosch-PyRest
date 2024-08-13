from fastapi.testclient import TestClient

# Adjust the path to include the parent directory of car_sharing.py
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from car_sharing import app


client = TestClient(app)


def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert "Welcome" in response.text