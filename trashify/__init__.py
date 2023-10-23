"""Flask app initialization"""

from flask import Flask
from authlib.integrations.flask_client import OAuth
from dotenv import find_dotenv, load_dotenv
from os import environ as env


ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)


oauth = OAuth()
oauth.register(
    "trashify",
    client_id=env.get("AUTH0_CLIENT_ID"),
    client_secret=env.get("AUTH0_CLIENT_SECRET"),
    client_kwargs={
        "scope": "openid profile email",
    },
    api_base_url=f'https://{env.get("AUTH0_DOMAIN")}',
    access_token_url=f'https://{env.get("AUTH0_DOMAIN")}/oauth/token',
    authorize_url=f'https://{env.get("AUTH0_DOMAIN")}/authorize',
    server_metadata_url=f'https://{env.get("AUTH0_DOMAIN")}/'
    + ".well-known/openid-configuration",
)


def create_app():
    """Create a Flask app"""

    app = Flask(__name__)

    app.secret_key = env.get("APP_SECRET_KEY")
    oauth.init_app(app)

    from trashify.views import auth_view

    app.register_blueprint(auth_view)

    return app
