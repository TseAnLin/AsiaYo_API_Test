from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_order_success():
    response = client.post("/api/orders", json={
        "id": "A0000001",
        "name": "Melody Holiday Inn",
        "address": {
            "city": "taipei-city",
            "district": "da-an-district",
            "street": "fuxing-south-road"
        },
        "price": 1999,
        "currency": "TWD"
    })
    assert response.status_code == 200
    assert response.json()["price"] == 1999

def test_create_order_invalid_name():
    response = client.post("/api/orders", json={
        "id": "A0000001",
        "name": "melody holiday inn",
        "address": {
            "city": "taipei-city",
            "district": "da-an-district",
            "street": "fuxing-south-road"
        },
        "price": 2000,
        "currency": "TWD"
    })
    assert response.status_code == 400
    assert response.json()["detail"] == "Name is not capitalized"

def test_create_order_invalid_price():
    response = client.post("/api/orders", json={
        "id": "A0000001",
        "name": "Melody Holiday Inn",
        "address": {
            "city": "taipei-city",
            "district": "da-an-district",
            "street": "fuxing-south-road"
        },
        "price": 2500,
        "currency": "TWD"
    })
    assert response.status_code == 400
    assert response.json()["detail"] == "Price is over 2000"

def test_create_order_invalid_currency():
    response = client.post("/api/orders", json={
        "id": "A0000001",
        "name": "Melody Holiday Inn",
        "address": {
            "city": "taipei-city",
            "district": "da-an-district",
            "street": "fuxing-south-road"
        },
        "price": 2000,
        "currency": "JPY"
    })
    assert response.status_code == 400
    assert response.json()["detail"] == "Currency format is wrong"
