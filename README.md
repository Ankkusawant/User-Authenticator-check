# 🛡️ User Authentication System (Python)

A simple command-line user authentication system built using Python.  
It supports **user registration**, **login**, **password hashing**, and **basic validations**.
## Features
- Register with email and password
- Secure password hashing (SHA-256)
- Password strength validation
- Email format validation
- Login with validation
- JSON file storage
- Easy-to-extend structure
## 📁 Project Structure
Auth_Project/
│
├── auth.py # Handles registration, login, hashing, JSON I/O
├── main.py # CLI menu for interacting with users
├── users.json # (auto-generated) Stores registered users
└── README.md # Project documentation
---------- Registration Rules ----------
- Valid email format (`@` and `.` required)
- Password must have:
  - At least 5 characters
  - One uppercase letter
  - One lowercase letter
  - One digit
  - One special character
---------- User Authentication System ----------
1. Register
2. Login
3. Exit
Choose an option (1-3): 1
Enter your email: user@example.com
Enter your password: MyPass@123
Registration successful
-----------  .gitignore  ----------
To avoid uploading sensitive data.
-----------  Requirements  ----------
No external libraries required.
Works on Python 3.x.
