# Secure File Sharing Platform

## Overview
Secure File Sharing is a lightweight, security-focused web application designed to safely upload, store, and share files between users.  
It emphasizes **authentication, access control, encryption awareness, and audit logging**, making it ideal for learning secure system design.

This project is suitable for **cybersecurity learners, developers, and students** who want hands-on exposure to secure file-handling concepts.

---

## Key Features
- User registration & login
- Secure file upload & download
- Access-controlled file sharing
- Hash-based file integrity checks
- Activity logging (uploads/downloads)
- Simple, clean UI
- Educational focus on security concepts

---

## Tech Stack
- **Backend:** Python (Flask)
- **Frontend:** HTML, CSS
- **Database:** SQLite
- **Authentication:** Flask-Login
- **Hashing:** SHA-256
- **OS:** Cross-platform (Linux / Windows / macOS)

---

## Folder Structure
secure-file-sharing/
│
├── app.py # Main Flask application
├── database.db # SQLite database
├── requirements.txt # Python dependencies
├── uploads/ # Stored uploaded files
│
├── templates/
│ ├── login.html
│ ├── register.html
│ ├── dashboard.html
│ └── upload.html
│
├── static/
│ └── style.css
│
└── README.md # Documentation

yaml
Always show details

Copy code

---

## Installation & Setup

### 1. Clone or Extract Project
```bash
git clone <repo-url>
cd secure-file-sharing
2. Create Virtual Environment (Recommended)
bash
Always show details

Copy code
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\\Scripts\\activate    # Windows
3. Install Dependencies
bash
Always show details

Copy code
pip install -r requirements.txt
4. Run the Application
bash
Always show details

Copy code
python app.py
5. Open in Browser
cpp
Always show details

Copy code
http://127.0.0.1:5000
How to Use
User Flow
Register a new account

Login securely

Upload files (stored securely)

Download only authorized files

View activity logs (if enabled)

Security Concepts Demonstrated
Authentication
Password hashing

Session handling

File Security
File type validation

Secure file storage paths

Hash verification (SHA-256)

Access Control
User-based file ownership

Restricted downloads

Logging
Upload/download tracking

Audit trail awareness

What to Look For (Learning Perspective)
How improper file validation leads to vulnerabilities

Why direct file access is dangerous

Importance of hashing & integrity checks

Secure vs insecure file-sharing practices
