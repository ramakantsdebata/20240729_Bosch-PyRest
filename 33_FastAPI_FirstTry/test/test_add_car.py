from unittest.mock import Mock
from fastapi.testclient import TestClient

# Adjust the path to include the parent directory of car_sharing.py
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from car_sharing import app
from routers.cars import add_car
from schema import CarInput, User_DBModel, Car_DBModel


client = TestClient(app)


def test_add_car():
    response = client.post("/api/cars",
                           json={
                               "doors": 7,
                               "size": "xxl",
                           }, headers={'Authorization': 'Bearer ramakant'}
                           )
    assert response.status_code == 200
    car = response.json()
    assert car['doors'] == 7
    assert car['size'] == 'xxl'


def test_add_car_with_mock_session():
    mock_session = Mock()
    input = CarInput(doors=2, size="xl")
    user = User_DBModel(username="ramakant")
    result = add_car(car=input, session=mock_session, user=user)

    mock_session.add.assert_called_once()
    mock_session.commit.assert_called_once()
    mock_session.refresh.assert_called_once()

    assert isinstance(result, Car_DBModel)
    assert result.doors == 2
    assert result.size == "xl"
