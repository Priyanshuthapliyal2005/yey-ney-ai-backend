# routes/__init__.py
from flask import Blueprint

user_routes = Blueprint('user_routes', __name__)
post_routes = Blueprint('post_routes', __name__)
reaction_routes = Blueprint('reaction_routes', __name__)
moderation_routes = Blueprint('moderation_routes', __name__)
