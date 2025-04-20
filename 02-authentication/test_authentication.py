from secure_auth import app

def test_login_success():
    client = app.test_client()
    response = client.post("/", data={"username": "admin", "password": "SecureP@ssw0rd!"})
    assert response.status_code == 302  # should redirect on success

def test_login_fail():
