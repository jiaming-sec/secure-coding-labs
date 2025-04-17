from flask import Flask, request
import html

app = Flask(__name__)

@app.route("/")
def index():
    name = request.args.get("name", "")
    safe_name = html.escape(name)
    return f"<h1>Hello, {safe_name}!</h1>"

if __name__ == "__main__":
    app.run(debug=True)
