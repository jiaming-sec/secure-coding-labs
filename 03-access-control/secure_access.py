from flask import Flask, request, jsonify, abort

app = Flask(__name__)

users = {
    "1": {"name": "Alice", "role": "user"},
    "2": {"name": "Bob", "role": "admin"}
}
