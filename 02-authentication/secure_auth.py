from flask import Flask, request, redirect, session, render_template_string
from werkzeug.security import check_password_hash, generate_password_hash
