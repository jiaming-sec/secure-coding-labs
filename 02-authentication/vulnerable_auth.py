from flask import Flask, request, redirect, make_response

app = Flask(__name__)

# Hardcoded credentials (bad practice)
users = {"admin": "1234"}

def login():
    if request.method == "POST":
        username = request.form.get("username", "")
        password = request.form.get("password", "")
        if users.get(username) == password:
            # Insecure session: manually setting user cookie without security flags
            resp = make_response(redirect("/dashboard"))
            resp.set_cookie("user", username)
            return resp
        return "Invalid credentials"
    
    return '''
        <form method="POST">
            Username: <input name="username">
            Password: <input name="password" type="password">
            <input type="submit">
        </form>
    '''
    
@app.route("/dashboard")
def dashboard():
    user = request.cookies.get("user")
    return f"Welcome, {user}!"
