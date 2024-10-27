# routes/user_routes.py
from flask import request, jsonify
from services.user_service import create_user

from . import user_routes

@user_routes.route('/users', methods=['POST'])
def register_user():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    username = data.get('username')
    dob = data.get('dob')
    contact_number = data.get('contact_number')

    result = create_user(email, password, username, dob, contact_number)
    return jsonify({"message": result}), 201
