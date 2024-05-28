from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_addition_success():
    response = client.post("/add", 
        json={
                "batch_id": "id0101",
                "payload": [[1,2], [3,4]]
        })
    assert response.status_code == 200
    response_json = response.json()
    assert response_json["batch_id"]=="id0101"
    assert response_json["payload"]==[3,7]
    assert response_json["status"]=="complete"
    assert "started_at" in response_json
    assert "completed_at" in response_json

def test_addition_invalid_payload():
    response = client.post("/add",
        json={
                "batch_id": "id0101",
                "payload": [[1,2], [a,b]]
        })
    assert response.status_code == 422

def test_addition_empty_payload():
    response = client.post("/add",
        json={
                "batch_id": "id0101",
                "payload": []
        })
    assert response.status_code == 422