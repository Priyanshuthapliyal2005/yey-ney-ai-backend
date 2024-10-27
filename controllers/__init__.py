# controllers/user_controller.py
from flask import jsonify
from services.user_service import create_user

def register_user(data):
    result = create_user(data['email'], data['password'], data['username'], data['dob'], data['contact_number'])
    return jsonify({"message": result}), 201
