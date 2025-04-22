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
- Redirects and invalid credential handling are applied

---

## 🧪 Testing Tips

- Use tools like **Burp Suite** to intercept session cookies
- Try **cookie tampering**: change `user=admin` to impersonate
- Test password brute-force using a script or automation

---

## 🛡 Best Practices

| Category               | Bad Practice                          | Secure Alternative                          |
|------------------------|----------------------------------------|---------------------------------------------|
| Password Storage        | Plaintext in dictionary                | Hashed using `bcrypt` or `PBKDF2`           |
| Authentication Check    | Direct comparison of strings           | Use constant-time hash checking             |
| Session Handling        | Raw cookies                            | Use `Flask session` (server-side)           |
| Cookie Security         | No flags                               | Use `HttpOnly`, `Secure`, and `SameSite`    |

---

## 📈 Simulated CVSS

- **Score**: 7.5 – High
- **Vector**: `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:N`
- Broken authentication can lead to full account compromise.

---

## 📘 Disclaimer

This project is independently written to reflect secure coding techniques. Inspired by secure coding concepts from Pluralsight.

