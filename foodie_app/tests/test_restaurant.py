import requests

BASE_URL = "http://127.0.0.1:5000"


def test_create_restaurant():
    response = requests.post(
        f"{BASE_URL}/api/v1/restaurants",
        json={"name": "Test Restaurant"}
    )
    assert response.status_code == 201


def test_get_restaurant():
    # First create
    create_response = requests.post(
        f"{BASE_URL}/api/v1/restaurants",
        json={"name": "Get Test Restaurant"}
    )
    restaurant_id = create_response.json()["id"]

    # Then fetch
    response = requests.get(
        f"{BASE_URL}/api/v1/restaurants/{restaurant_id}"
    )

    assert response.status_code == 200
