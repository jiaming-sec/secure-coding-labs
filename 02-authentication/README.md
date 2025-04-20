# 🔐 Lab 02 – Broken Authentication & Session Management
## 🎯 Objective
Demonstrate insecure authentication practices (e.g., hardcoded passwords, insecure cookies) and apply secure password hashing and session management techniques.

---

## 🔥 Vulnerable Example

In `vulnerable_auth.py`:
- Passwords are **stored in plaintext**
- **Cookies are used without security flags**
- No session expiration or validation

### Example Exploits:
- Cookie theft leads to account hijacking
- Attacker guesses weak password "1234"

---

## ✅ Secure Example

In `secure_auth.py`:
- Passwords are hashed using `werkzeug.security`
- Flask session management is used (server-side sessions)
- Sensitive values are protected with a secret key
