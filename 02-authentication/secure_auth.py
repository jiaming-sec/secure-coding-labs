from flask import Flask, request, redirect, session, render_template_string
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)
app.secret_key = "a_very_secure_secret_key"  # Should be stored securely

# Properly hashed password storage
users = {"admin": generate_password_hash("SecureP@ssw0rd!")}

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username", "")
        password = request.form.get("password", "")
        stored_pw_hash = users.get(username)
        
        if stored_pw_hash and check_password_hash(stored_pw_hash, password):
            session["user"] = username
            return redirect("/dashboard")
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
    user = session.get("user")
