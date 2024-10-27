# services/user_service.py
from firebase_setup import auth, db
from models.user_model import user_data_structure

def create_user(email, password, username, dob, contact_number):
    try:
        user = auth.create_user(email=email, password=password)
        user_data = user_data_structure(user.uid, email, username, dob, contact_number)
        db.collection('users').document(user.uid).set(user_data)
        return f"User created with UID: {user.uid}"
    except Exception as e:
        return f"Error creating user: {str(e)}"
