import unittest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


class TestSampleCrudApi(unittest.TestCase):

    def test_read_string(self):
        response = client.get("/sample-crud/1")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"string_id": 1})

    def test_create_string(self):
        response = client.post("/sample-crud/", json={"string": "Test String"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"string": "Test String"})

    def test_update_string(self):
        response = client.put("/sample-crud/1", json={"string": "Updated String"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"string_id": 1, "string": "Updated String"})

    def test_delete_string(self):
        response = client.delete("/sample-crud/1")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"string_id": 1})