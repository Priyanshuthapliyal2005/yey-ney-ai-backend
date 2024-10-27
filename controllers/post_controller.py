# controllers/post_controller.py
from flask import jsonify
from services.post_service import create_post

def add_post(data):
    create_post(data['user_id'], data['title'], data['main_sentence'], data['media_url'], data['location'])
    return jsonify({"message": "Post created successfully"}), 201
