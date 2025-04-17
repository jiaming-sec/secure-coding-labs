from secure_app import app

def test_xss_input():
    test_client = app.test_client()
    malicious_input = "<script>alert('XSS')</script>"
    response = test_client.get(f" /?name={malicious_input}")
    assert malicious_input not in response.get_data(as_text=True)
    assert "&lt;script&gt;" in response.get_data(as_text=True)
