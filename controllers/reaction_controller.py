# controllers/reaction_controller.py
from flask import jsonify
from services.reaction_service import add_reaction_to_post

def react_to_post(post_id, reaction):
    add_reaction_to_post(post_id, reaction)
    return jsonify({"message": "Reaction added"}), 200
