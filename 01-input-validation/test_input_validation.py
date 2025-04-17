from secure_app import app

def test_xss_input():
    test_client = app.test_client()
