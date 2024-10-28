from firebase_admin import auth

def get_current_user(uid):
    """Retrieve the current user by UID."""
    try:
        user = auth.get_user(uid)
        return {
            "success": True,
            "user_id": user.uid,
            "email": user.email,
            "display_name": user.display_name,
            "photo_url": user.photo_url
        }
    except Exception as e:
        return {
            "success": False,
            "message": str(e)
        }

def verify_token(id_token):
    """Verify the Firebase ID token and return user information."""
    try:
        decoded_token = auth.verify_id_token(id_token)
        return {
            "success": True,
            "uid": decoded_token['uid']
        }
    except Exception as e:
        return {
            "success": False,
            "message": str(e)
        }
