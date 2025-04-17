from flask import Flask, request
import html

app = Flask(__name__)

@app.route("/")
def index():
    name = request.args.get("name", "")
    safe_name = html.escape(name)
