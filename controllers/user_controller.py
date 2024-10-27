# controllers/user_controller.py
from flask import Blueprint, request, jsonify
from firebase_admin import auth, firestore

user_controller = Blueprint('user_controller', __name__)
db = firestore.client()

@user_controller.route('/register', methods=['POST'])
def register_user():
    try:
        data = request.json
        # Create user in Firebase Auth
        user = auth.create_user(
            email=data['email'],
            password=data['password']
        )
        # Save additional user data in Firestore
        db.collection('users').document(user.uid).set({
            'name': data['name'],
            'email': data['email'],
            'created_at': firestore.SERVER_TIMESTAMP,
        })
        return jsonify({"message": "User registered successfully!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400
