# routes/reaction_routes.py
from flask import request, jsonify
from services.reaction_service import add_reaction_to_post

from . import reaction_routes

@reaction_routes.route('/posts/<post_id>/reactions', methods=['POST'])
def react_to_post(post_id):
    data = request.get_json()
    reaction = data.get('reaction')

    add_reaction_to_post(post_id, reaction)
    return jsonify({"message": "Reaction added"}), 200
