# 🔒 Lab 01 – Input Validation and XSS Prevention

## 🎯 Objective
Demonstrate how improper input validation can result in Cross-Site Scripting (XSS), and show how secure coding practices like input sanitization prevent such vulnerabilities.

---

## 🧪 The Vulnerability: Reflected XSS

In `vulnerable_app.py`, the Flask app takes untrusted input from the query string and directly embeds it into the page without any sanitization.

### 💥 Exploit Example:
```text
http://localhost:5000/?name=<script>alert('XSS')</script>
