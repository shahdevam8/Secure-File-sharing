from authlib.integrations.flask_client import OAuth
from flask import Blueprint, current_app

oauth = OAuth()
oauth_bp = Blueprint("oauth", __name__)

def init_oauth(app):
    if "GOOGLE_CLIENT_ID" not in app.config:
        return  # OAuth disabled safely

    oauth.init_app(app)
    oauth.register(
        name="google",
        client_id=app.config["GOOGLE_CLIENT_ID"],
        client_secret=app.config["GOOGLE_CLIENT_SECRET"],
        server_metadata_url="https://accounts.google.com/.well-known/openid-configuration",
        client_kwargs={"scope": "openid email profile"}
    )
