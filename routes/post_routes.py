from flask import Blueprint, request, jsonify
from services.post_service import PostService
from utils.firebase_auth import get_current_user, verify_token

post_routes = Blueprint('post_routes', __name__)

def get_authenticated_user():
    """Utility function to get the authenticated user from Firebase token."""
    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        return None
    
    id_token = auth_header.split("Bearer ")[1]
    token_verification = verify_token(id_token)  # Verify the ID token
    if not token_verification.get("success"):
        return None  # Token verification failed

    uid = token_verification.get("uid")
    user_info = get_current_user(uid)  # Retrieve user info by UID
    if not user_info.get("success"):
        return None  # User retrieval failed

    return user_info  # Return the user information

@post_routes.route('/posts', methods=['GET'])
def get_posts():
    try:
        limit = int(request.args.get('limit', 10))
        offset = int(request.args.get('offset', 0))
        sort = request.args.get('sort', 'newest')
        posts = PostService.get_all_posts(limit=limit, offset=offset, sort=sort)
        return jsonify(posts), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@post_routes.route('/posts', methods=['POST'])
def create_post():
    post_data = request.get_json()
    if not post_data:
        return jsonify({"error": "Invalid or missing JSON data"}), 415

    current_user = get_authenticated_user()
    if not current_user:
        return jsonify({"error": "User authentication required"}), 401

    try:
        new_post = PostService.create_post(post_data, current_user)
        return jsonify(new_post), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@post_routes.route('/posts/<post_id>', methods=['GET'])
def get_post(post_id):
    post = PostService.get_post_by_id(post_id)
    if not post:
        return jsonify({"error": "Post not found"}), 404
    return jsonify(post), 200

@post_routes.route('/posts/<post_id>', methods=['PUT'])
def update_post(post_id):
    post_data = request.get_json()
    if not post_data:
        return jsonify({"error": "Invalid or missing JSON data"}), 415

    current_user = get_authenticated_user()
    if not current_user:
        return jsonify({"error": "User authentication required"}), 401

    try:
        updated_post = PostService.update_post(post_id, post_data, current_user)
        return jsonify(updated_post), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@post_routes.route('/posts/<post_id>', methods=['DELETE'])
def delete_post(post_id):
    current_user = get_authenticated_user()
    if not current_user:
        return jsonify({"error": "User authentication required"}), 401

    try:
        result = PostService.delete_post(post_id, current_user)
        if result.get("success"):
            return jsonify(result), 200
        else:
            return jsonify({"error": "Failed to delete post"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 400
