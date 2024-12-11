

import requests
import pytest
import allure

BASE_URL = "https://petstore.swagger.io/v2"
HEADERS = {"Content-Type": "application/json"}

@pytest.fixture
def user_data():
   return {
    "id": 1000,
    "username": "FlyffiUpdate",
    "firstName": "string",
    "lastName": "string",
    "email": "string",
    "password": "string",
    "phone": "string",
    "userStatus": 0
  }

@allure.feature('create user post')
@allure.story('Тест создания нового юзера')
def test_user_createUser_post(user_data):
    response = requests.post(f"{BASE_URL}/user", json=user_data, headers=HEADERS)
    assert response.status_code == 200, f"code: {response.status_code}"
    response_data = response.json() if response.content else {}
    assert response_data.get("code") == 200

@allure.feature('get user')
@allure.story('Получение юзера по имени')
def test_user_get(user_data):
    username = user_data["username"]
    response = requests.get(f"{BASE_URL}/user/{username}")
    assert response.status_code == 200, f"code: {response.status_code}"
    response_data = response.json() if response.content else {}
    assert user_data.get("username") == user_data["username"]

@allure.feature('Post user')
@allure.story('Тест обновления данных юзера')
def test_user_put(user_data):
    user_data = user_data.copy()
    username = user_data["username"]
    user_data["username"] = "FlyffiUpdate"
    response = requests.put(f"{BASE_URL}/user/{username}", json=user_data, headers=HEADERS)
    assert response.status_code == 200, f"code: {response.status_code}"
    response_data = response.json() if response.content else {}
    assert response_data.get("message") == str(user_data["id"])

@allure.feature('delete user')
@allure.story('Тест для удаления юзера')
def test_user_delete(user_data):
    username = user_data["username"]
    response = requests.delete(f"{BASE_URL}/user/{username}", headers=HEADERS)
    assert response.status_code == 200, f"code: {response.status_code}"
    response = requests.get(f"{BASE_URL}/user/{username}")
    assert response.status_code == 404, f"code: {response.status_code}"

@allure.feature('get user login')
@allure.story('Тест получения юзера по логину')
def test_user_get_login(user_data):
    response = requests.get(f"{BASE_URL}/user/login", headers=HEADERS)
    assert response.status_code == 200, f"code: {response.status_code}"
    response_data = response.json() if response.content else {}
    assert response_data.get("code") == 200


@allure.feature('get user logout')
@allure.story('Тест выхода из системы')
def test_user_get_logout(user_data):
    response = requests.get(f"{BASE_URL}/user/logout", headers=HEADERS)
    assert response.status_code == 200, f"code: {response.status_code}"
    response_data = response.json() if response.content else {}
    assert response_data.get("code") == 200







