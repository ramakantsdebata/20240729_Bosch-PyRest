from fastapi.testclient import TestClient

# Adjust the path to include the parent directory of car_sharing.py
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from car_sharing import app


client = TestClient(app)

def test_get_cars():
    response = client.get("/api/cars")
    assert response.status_code == 200
    cars = response.json()
    assert all(['doors' in c for c in cars])
    assert all(['size' in c for c in cars])
    

def test_get_cars_filter():
    response = client.get("/api/cars?size=m&doors=3")
    assert response.status_code == 200
    cars = response.json()
    assert all([c["size"] == "m" for c in cars])
    assert all([c["doors"] >= 3 for c in cars])
