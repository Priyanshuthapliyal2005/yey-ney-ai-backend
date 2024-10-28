# controllers/feed_controller.py
from flask import Blueprint, request, jsonify
from services.feed_service import get_discovery_feed, get_user_feed

feed_routes = Blueprint('feed_routes', __name__)

@feed_routes.route('/api/v1/feed/discover', methods=['GET'])
def discover_feed():
    user_id = request.args.get('user_id')
    language = request.args.get('language')
    location = request.args.get('location')
    interests = request.args.get('interests')

    feed_data = get_discovery_feed(user_id, language, location, interests)
    return jsonify(feed_data)

@feed_routes.route('/api/v1/feed/yours', methods=['GET'])
def user_feed():
    user_id = request.args.get('user_id')
    post_id = request.args.get('post_id')

    user_feed_data = get_user_feed(user_id, post_id)
    return jsonify(user_feed_data)
