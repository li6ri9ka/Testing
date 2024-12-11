import requests
import pytest
import allure

BASE_URL = "https://petstore.swagger.io/v2"
HEADERS = {"Content-Type": "application/json"}

@pytest.fixture
def store_data():
    return {
        "id": 1,
        "petId": 1,
        "quantity": 1,
        "shipDate": "2024-12-08T14:32:32.799Z",
        "status": "placed",
        "complete": "true"
    }

@allure.feature('get store data')
@allure.story('Тест получения данных магазина')
def test_get_store_data(store_data):
    response = requests.get(f"{BASE_URL}/store/inventory")
    assert response.status_code == 200, f"Код: {response.status_code}"

@allure.feature('post store data')
@allure.story('Тест создания данных магазина')
def test_post_store_data(store_data):
    response = requests.post(f"{BASE_URL}/store/order", headers=HEADERS, json=store_data)
    assert response.status_code == 200 ,f"code: {response.status_code}"
    response_data = response.json() if response.content else {}
    assert response_data.get("id") == store_data["id"]

@allure.feature('get store data v2')
@allure.story('Второй тест получения данных магазина')
def test_get_v2_store_data(store_data):
    orderId = store_data["id"]
    response = requests.get(f"{BASE_URL}/store/order/{orderId}", headers=HEADERS)
    assert response.status_code == 200 ,f"code: {response.status_code}"
    response_data = response.json() if response.content else {}
    assert response_data.get("id") == orderId

@allure.feature('delete store data')
@allure.story('Тест удаления данных магазина')
def test_delete_store_data(store_data):
    orderId = store_data["id"]
    response = requests.delete(f"{BASE_URL}/store/order/{orderId}", headers=HEADERS)
    assert response.status_code == 200 ,f"code: {response.status_code}"
    response = requests.get(f"{BASE_URL}/store/order/{orderId}", headers=HEADERS)
    assert response.status_code == 404 ,f"code: {response.status_code}"
