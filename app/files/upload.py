from flask import Blueprint, request, jsonify, render_template
from flask_jwt_extended import jwt_required, get_jwt_identity
import os, uuid, time, sqlite3
from app.utils.encryption import encrypt
from config import UPLOAD_FOLDER, DB_PATH

upload_bp = Blueprint("upload", __name__)

# ------------------------
# API: Upload File
# ------------------------
@upload_bp.route("/upload", methods=["POST"])
@jwt_required()
def upload_file():
    user = get_jwt_identity()
    file = request.files["file"]
    password = request.form.get("password")
    expiry = int(time.time()) + 600  # 10 minutes

    encrypted_data, key = encrypt(file.read())
    file_id = str(uuid.uuid4())

    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    with open(os.path.join(UPLOAD_FOLDER, file_id), "wb") as f:
        f.write(encrypted_data)

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute(
        "INSERT INTO files VALUES (?, ?, ?, ?, ?, ?)",
        (file_id, user, file.filename, expiry, password, None)
    )
    conn.commit()
    conn.close()

    return jsonify(
        file_id=file_id,
        encryption_key=key.decode(),
        expires_in="10 minutes"
    )


# ------------------------
# UI: Upload Page
# ------------------------
@upload_bp.route("/upload-ui", methods=["GET"])
def upload_ui():
    """
    Renders the upload HTML page.
    """
    return render_template("upload.html")
