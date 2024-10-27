# routes/post_routes.py
from flask import request, jsonify
from services.post_service import create_post

from . import post_routes

@post_routes.route('/posts', methods=['POST'])
def add_post():
    data = request.get_json()
    user_id = data.get('user_id')
    title = data.get('title')
    main_sentence = data.get('main_sentence')
    media_url = data.get('media_url')
    location = data.get('location')

    create_post(user_id, title, main_sentence, media_url, location)
    return jsonify({"message": "Post created successfully"}), 201
