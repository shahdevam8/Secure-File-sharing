import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

SECRET_KEY = "super-secret-key"
JWT_SECRET_KEY = "jwt-secret"

DB_PATH = os.path.join(BASE_DIR, "database", "app.db")
UPLOAD_FOLDER = os.path.join(BASE_DIR, "storage", "encrypted")

GOOGLE_CLIENT_ID = "YOUR_GOOGLE_CLIENT_ID"
GOOGLE_CLIENT_SECRET = "YOUR_GOOGLE_CLIENT_SECRET"
