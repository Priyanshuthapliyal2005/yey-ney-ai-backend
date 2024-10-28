# routes/feed_routes.py

from flask import Blueprint, request, jsonify
from services.feed_service import get_discover_feed, get_user_feed

feed_bp = Blueprint('feed', __name__)

@feed_bp.route('/api/v1/feed/discover', methods=['GET'])
def discover_feed():
    user_id = request.args.get('user_id')
    language = request.args.get('language')
    location = request.args.get('location')
    interests = request.args.get('interests')
    feed = get_discover_feed(user_id, language, location, interests)
    return jsonify(feed), 200

@feed_bp.route('/api/v1/feed/yours', methods=['GET'])
def user_feed():
    post_id = request.args.get('post_id')
    user_id = request.args.get('user_id')
    feed = get_user_feed(user_id, post_id)
    return jsonify(feed), 200
