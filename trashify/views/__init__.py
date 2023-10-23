"""Views"""

from flask import Blueprint

auth_view = Blueprint("auth", __name__)

from .auth.oauth import *
