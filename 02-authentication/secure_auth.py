from flask import Flask, request, redirect, session, render_template_string
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)
app.secret_key = "a_very_secure_secret_key"  # Should be stored securely
