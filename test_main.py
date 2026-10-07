from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_add_and_list_expense():
    r = client.post("/expenses", json={"name": "Coffee", "amount": 4.5, "category": "food"})
    assert r.status_code == 200
    assert any(e["name"] == "Coffee" for e in client.get("/expenses").json())

def test_summary_has_category():
    client.post("/expenses", json={"name": "Gas", "amount": 40, "category": "car"})
    assert "car" in client.get("/summary").json()
