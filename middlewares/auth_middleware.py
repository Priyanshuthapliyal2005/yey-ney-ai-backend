# middlewares/auth_middleware.py
from flask import request, jsonify
from firebase_setup import auth

def auth_middleware(f):
    def decorated_function(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({"message": "Token is missing!"}), 403
        try:
            auth.verify_id_token(token)
        except Exception as e:
            return jsonify({"message": str(e)}), 403
        return f(*args, **kwargs)
    return decorated_function
