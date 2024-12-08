import requests
import pytest

BASE_URL = "https://petstore.swagger.io/v2"
HEADERS = {"Content-Type": "application/json"}

@pytest.fixture
def user_data():
   return [{
    "id": 0,
    "username": "string",
    "firstName": "string",
    "lastName": "string",
    "email": "string",
    "password": "string",
    "phone": "string",
    "userStatus": 0
  },
    {"id": 1,
    "username": "string",
    "firstName": "string",
    "lastName": "string",
    "email": "string",
    "password": "string",
    "phone": "string",
    "userStatus": 0}
   ]


def test_user_post(user_data):
    response = requests.post(f"{BASE_URL}/user/createWithList", json=user_data, headers=HEADERS)
    assert response.status_code == 200, f"code: {response.status_code}"
    response_data = response.json() if response.content else {}
    assert response_data.get("code") == 200


def test_user_post_createWithArray(user_data):
    response = requests.post(f"{BASE_URL}/user/createWithArray", json=user_data, headers=HEADERS)
    assert response.status_code == 200, f"code: {response.status_code}"
    response_data = response.json() if response.content else {}
    assert response_data.get("code") == 200
