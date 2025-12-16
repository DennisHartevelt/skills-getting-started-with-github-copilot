from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)


def test_get_activities():
    res = client.get("/activities")
    assert res.status_code == 200
    data = res.json()
    assert isinstance(data, dict)
    # Check a known activity exists
    assert "Chess Club" in data


def test_signup_and_unregister_flow():
    activity = "Basketball Team"
    email = "testuser@example.com"

    # Ensure email not present initially
    res = client.get("/activities")
    assert res.status_code == 200
    assert email not in res.json()[activity]["participants"]

    # Sign up
    res = client.post(f"/activities/{activity}/signup", params={"email": email})
    assert res.status_code == 200
    assert "Signed up" in res.json()["message"]

    # Confirm participant added
    res = client.get("/activities")
    assert res.status_code == 200
    assert email in res.json()[activity]["participants"]

    # Unregister
    res = client.post(f"/activities/{activity}/unregister", params={"email": email})
    assert res.status_code == 200
    assert "Unregistered" in res.json()["message"]

    # Confirm participant removed
    res = client.get("/activities")
    assert res.status_code == 200
    assert email not in res.json()[activity]["participants"]