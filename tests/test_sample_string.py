from fastapi.testclient import TestClient
from app.main import app
from app.repositories.repository import MySqlRepository

client = TestClient(app)


def test_read_string():
    # Setup
    instance = MySqlRepository()
    string_id = 1
    data = {"string_text": "hello", "description": "test"}
    instance.create(data=data)

    # Test
    response = client.get(f"/sample-crud/{string_id}")
    assert response.status_code == 200

    # Teardown
    instance.delete(id=string_id)


def test_create_string():
    # Setup
    data = {"string_text": "hello", "description": "test"}

    # Test
    response = client.post("/sample-crud/", json=data)
    assert response.status_code == 201

    # Teardown
    instance = MySqlRepository()
    instance.delete(id=response.json()["string"])


def test_update_string_returns_202():
    # create a sample string to update
    data = {"string_text": "hello world", "description": "a greeting"}
    response = client.post("/sample-crud/", json=data)
    string_id = response.json()["string"]

    # update the string
    data = {"string_text": "hello there", "description": "a greeting"}
    response = client.put(f"/sample-crud/{string_id}", json=data)
    assert response.status_code == 202
    assert response.json() == {"status": "updated", "status_code": 202}


def test_delete_string_returns_204():
    # create a sample string to delete
    data = {"string_text": "hello world", "description": "a greeting"}
    response = client.post("/sample-crud/", json=data)
    string_id = response.json()["string"]

    # delete the string
    response = client.delete(f"/sample-crud/{string_id}")
    assert response.status_code == 204