# models/user_model.py
def user_data_structure(user_id, email, username, dob, contact_number, preferences=None):
    return {
        "userid": user_id,
        "email": email,
        "username": username,
        "birth": {
            "dob": dob,
            "age": 30  # Example, replace with actual age calculation
        },
        "contact": {
            "tel": contact_number,
            "verified": False
        },
        "preferences": preferences or {
            "alerts": True,
            "notifications": True,
            "language": "en-US",
        },
        "activity": {
            "yey": 0,
            "ney": 0,
            "status": "new_user"
        }
    }
