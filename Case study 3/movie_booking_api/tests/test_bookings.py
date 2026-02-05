import requests

def test_book_tickets(base_url):
    payload = {
        "movie_id": 101,
        "seats": 2
    }

    response = requests.post(f"{base_url}/api/bookings", json=payload)
    assert response.status_code == 201

    data = response.json()
    assert data["total_price"] == 500
