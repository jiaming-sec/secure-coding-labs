from secure_access import app

def test_user_can_access_own_profile():
  client = app.test_client()
  response = client.get("/profile/1")
