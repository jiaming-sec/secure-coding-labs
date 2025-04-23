from flask import Flask, request, jsonify

app = Flask(__name__)

users = {
  "1": {"name": "Alice", "role": "user"},
  "2": {"name": "Bob", "role": "admin"}

}

users = {
    "1": {"name": "Alice", "role": "user"},
    "2": {"name": "Bob", "role": "admin"}
}
