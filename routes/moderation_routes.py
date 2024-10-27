# routes/moderation_routes.py
from flask import request, jsonify
from services.moderation_service import check_content_moderation

from . import moderation_routes

@moderation_routes.route('/moderate', methods=['POST'])
def moderate_content():
    data = request.get_json()
    media_url = data.get('media_url')

    moderation_result = check_content_moderation(media_url)
    return jsonify(moderation_result), 200
