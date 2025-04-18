from flask import Flask, request, redirect, make_response

app = Flask(__name__)

# Hardcoded credentials (bad practice)
users = {"admin": "1234"}

@app.route("/", methods=["GET", "POST"])
def login():
