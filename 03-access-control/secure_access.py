from flask import Flask, request, jsonify, abort

app = Flask(__name__)

users = {
    "1": {"name": "Alice", "role": "user"},
    "2": {"name": "Bob", "role": "admin"}
}

# Simulated session (user_id and role)
current_user = {"user_id": "1", "role": "user"}  # simulate Alice logged in

@app.route("/profile/<user_id>")
def profile(user_id):
    # ✅ Enforce user-level access
    if user_id != current_user["user_id"] and current_user["role"] != "admin":
        abort(403, description="Access denied")
