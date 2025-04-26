from flask import Flask

app = Flask(__name__)

# ❌ Hardcoded sensitive data
DATABASE_PASSWORD = "SuperSecretPassword123!"

@app.route("/")
def home():
  return f"Database password is {DATABASE_PASSWORD}"  # Should never expose sensitive info!
