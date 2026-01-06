from flask import Blueprint, request, jsonify, render_template
from flask_jwt_extended import create_access_token
import sqlite3
from config import DB_PATH

auth_bp = Blueprint("auth", __name__)

# ------------------------
# API: Register
# ------------------------
@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.json
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    try:
        c.execute(
            "INSERT INTO users VALUES (NULL, ?, ?)",
            (data["username"], data["password"])
        )
        conn.commit()
        return jsonify(msg="User registered")
    except:
        return jsonify(error="User already exists"), 400
    finally:
        conn.close()


# ------------------------
# API: Login (JWT)
# ------------------------
@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    c.execute(
        "SELECT * FROM users WHERE username=? AND password=?",
        (data["username"], data["password"])
    )
    user = c.fetchone()
    conn.close()

    if not user:
        return jsonify(error="Invalid credentials"), 401

    token = create_access_token(identity=data["username"])
    return jsonify(access_token=token)


# ------------------------
# UI: Login Page
# ------------------------
@auth_bp.route("/login-ui", methods=["GET"])
def login_ui():
    """
    Renders the login HTML page.
    No authentication logic here.
    """
    return render_template("login.html")
