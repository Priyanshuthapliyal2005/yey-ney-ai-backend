# controllers/post_controller.py
from flask import Blueprint, request, jsonify
from services.post_service import create_post

post_routes = Blueprint('post_routes', __name__)

@post_routes.route('/api/v1/post/create-post', methods=['POST'])
def create_new_post():
    data = request.form.to_dict()
    media = request.files.get('media')
    place = {
        'latitude': data['latitude'],
        'longitude': data['longitude'],
        'friendly_name': data['friendly_name'],
        'city': data['city'],
        'address': data['address']
    }
    friend_group = data.get('friend_group', [])
    sentence = data['sentence']
    music_id = data.get('music_id')
    is_private = data['isPrivate'].lower() == 'true'
    
    post_response = create_post(media, place, friend_group, sentence, music_id, is_private)
    return jsonify(post_response)
