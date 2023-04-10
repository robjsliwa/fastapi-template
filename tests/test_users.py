from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_read_users():
    response = client.get("/users/")
    assert response.status_code == 200
    assert response.json() == [{"username": "Rick"}, {"username": "Morty"}]


def test_read_user_me():
    response = client.get("/users/me")
    assert response.status_code == 200
    assert response.json() == {"username": "fakecurrentuser"}


def test_read_user():
    username = "johndoe"
    response = client.get(f"/users/{username}")
    assert response.status_code == 200
    assert response.json() == {"username": username}