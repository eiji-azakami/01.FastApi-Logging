from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_read_logs():
    response = client.get("/logs")
    assert response.status_code in (200, 404)
