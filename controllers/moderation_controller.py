# controllers/moderation_controller.py
from flask import jsonify
from services.moderation_service import check_content_moderation

def moderate_content(media_url):
    result = check_content_moderation(media_url)
    return jsonify(result), 200
