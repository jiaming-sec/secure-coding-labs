# 🛡️ Lab 03 – Broken Access Control

## 🎯 Objective

Demonstrate how missing authorization checks can lead to **insecure direct object references (IDOR)** and data exposure, and apply proper access control checks.

---

## 🔥 Vulnerable Example

In `vulnerable_access.py`:
- Users can access `/profile/<user_id>` without any validation
