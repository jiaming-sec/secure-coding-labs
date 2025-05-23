from flask import Flask
import os

app = Flask(__name__)

# ✅ Read sensitive data from environment variables
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")

@app.route("/")
def home():
  if DATABASE_PASSWORD:
