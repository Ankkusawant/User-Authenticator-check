import hashlib
import json
import os
import string

# Hash password using SHA-256
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Load user data from JSON file
def load_users():
    if not os.path.exists("users.json"):
        return {}
    with open("users.json", "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return {}

# Save user data to JSON file
def save_users(users):
    with open("users.json", "w") as f:
        json.dump(users, f)

# Register a new user
def register(email, password):
    users = load_users()

    if not email or "@" not in email or "." not in email:
        return "Invalid email format"
    if email in users:
        return "Email already registered"

    if (len(password) < 5 or
        not any(char.islower() for char in password) or
        not any(char.isupper() for char in password) or
        not any(char.isdigit() for char in password) or
        not any(char in string.punctuation for char in password)):
        return "Password must be at least 5 characters long and contain a lowercase, uppercase, digit, and special character."

    users[email] = hash_password(password)
    save_users(users)
    return "Registration successful"

# Login a user
def login(email, password):
    users = load_users()
    if "@" not in email or "." not in email:
        return "Invalid email format"
    if email not in users:
        return "Email not found"
    if users[email] == hash_password(password):
        return "Login successful"
    else:
        return "Incorrect password"
