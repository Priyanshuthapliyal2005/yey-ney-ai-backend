# middlewares/auth_middleware.py
from flask import request, jsonify
import firebase_admin
from firebase_admin import auth

def auth_middleware(f):
    def decorated_function(*args, **kwargs):
        token = request.headers.get('Authorization').split(" ")[1]
        try:
            decoded_token = auth.verify_id_token(token)
            request.user_id = decoded_token['uid']  # Set user_id from token
        except Exception as e:
            return jsonify({"error": "Unauthorized"}), 401
        return f(*args, **kwargs)
    return decorated_function
