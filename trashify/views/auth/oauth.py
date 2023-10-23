"""Handle user authentication during login and signup.
Also handle user logout.

All authentication is done through Auth0.
"""

import json
from flask import redirect, render_template, session, url_for
from os import environ as env
from urllib.parse import quote_plus, urlencode

# Local
from trashify import oauth
from trashify.views import auth_view


# Controllers API
@auth_view.route("/")
def home():
    return render_template(
        "home.html",
        session=session.get("user"),
        pretty=json.dumps(session.get("user"), indent=4),
    )


@auth_view.route("/callback", methods=["GET", "POST"])
def callback():
    """Get user token"""

    token = oauth.trashify.authorize_access_token()
    session["user"] = token
    return redirect(url_for("auth.home"))


@auth_view.route("/login")
def login():
    """Login user"""

    return oauth.trashify.authorize_redirect(
        redirect_uri=url_for("auth.callback", _external=True),
        audience=env.get("AUTH0_AUDIENCE"),
    )


@auth_view.route("/logout")
def logout():
    """Logout user."""

    session.clear()
    return redirect(
        "https://"
        + env.get("AUTH0_DOMAIN")
        + "/v2/logout?"
        + urlencode(
            {
                "returnTo": url_for("auth.home", _external=True),
                "client_id": env.get("AUTH0_CLIENT_ID"),
            },
            quote_via=quote_plus,
        )
    )
