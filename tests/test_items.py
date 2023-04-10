from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_items():
    response = client.get("/items/")
    assert response.status_code == 200
    assert response.json() == {"plumbus": {"name": "Plumbus"}, "gun": {"name": "Portal Gun"}}

def test_read_item():
    item_id = "plumbus"
    response = client.get(f"/items/{item_id}")
    assert response.status_code == 200
    assert response.json() == {"name": "Plumbus", "item_id": "plumbus"}

def test_read_item_not_found():
    item_id = "nonexistentitem"
    response = client.get(f"/items/{item_id}")
    assert response.status_code == 404
    assert response.json() == {"detail": "Item not found"}

def test_update_item():
    item_id = "plumbus"
    response = client.put(f"/items/{item_id}")
    assert response.status_code == 200
    assert response.json() == {"item_id": "plumbus", "name": "The great Plumbus"}

def test_update_item_forbidden():
    item_id = "gun"
    response = client.put(f"/items/{item_id}")
    assert response.status_code == 403
    assert response.json() == {"detail": "You can only update the item: plumbus"}