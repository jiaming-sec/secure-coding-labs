from flask import Flask, request, jsonify

app = Flask(__name__)

users = {
  "1": {"name": "Alice", "role": "user"},
  "2": {"name": "Bob", "role": "admin"}

}

@app.route("/profile/<user_id>")

def profile(user_id):
  # ❌ No authorization check — any user can view any profile
  user = users.get(user_id)
    if not user:
        return "User not found", 404
    return jsonify(user)
