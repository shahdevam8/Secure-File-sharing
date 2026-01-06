from flask import Blueprint, request, send_file, jsonify, render_template
import sqlite3, time, io, os
from app.utils.encryption import decrypt
from config import DB_PATH, UPLOAD_FOLDER

download_bp = Blueprint("download", __name__)

# ------------------------
# API: Download File
# ------------------------
@download_bp.route("/download/<file_id>", methods=["GET"])
def download_file(file_id):
    key = request.args.get("key")
    password = request.args.get("password")

    if not key:
        return jsonify(error="Encryption key required"), 400

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute(
        "SELECT filename, expiry, password FROM files WHERE id=?",
        (file_id,)
    )
    record = c.fetchone()
    conn.close()

    if not record:
        return jsonify(error="File not found"), 404

    filename, expiry, stored_password = record

    if time.time() > expiry:
        return jsonify(error="Download link expired"), 403

    if stored_password and password != stored_password:
        return jsonify(error="Invalid password"), 403

    with open(os.path.join(UPLOAD_FOLDER, file_id), "rb") as f:
        encrypted_data = f.read()

    decrypted_data = decrypt(encrypted_data, key.encode())

    return send_file(
        io.BytesIO(decrypted_data),
        download_name=filename,
        as_attachment=True
    )


# ------------------------
# UI: Download Page
# ------------------------
@download_bp.route("/download-ui", methods=["GET"])
def download_ui():
    """
    Renders the download HTML page.
    """
    return render_template("download.html")
