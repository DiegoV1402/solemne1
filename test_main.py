from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_time():
    response = client.get("/time")
    
    # Validamos que el servidor responda correctamente
    assert response.status_code == 200
    
    # Validamos el esquema del JSON
    data = response.json()
    assert "datetime" in data
    assert len(data["datetime"]) == 19