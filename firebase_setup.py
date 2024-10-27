import firebase_admin
from firebase_admin import credentials, auth, firestore
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Firebase
def initialize_firebase():
    try:
        firebase_cred_path = os.getenv('FIREBASE_CREDENTIALS')
        cred = credentials.Certificate(firebase_cred_path)
        firebase_admin.initialize_app(cred)
        print("Firebase initialized")
    except Exception as e:
        print(f"Error initializing Firebase: {e}")

# Firestore database reference
db = firestore.client()

# Function to create a new user in Firebase Authentication and Firestore
def create_user(email, password, user_data=None):
    try:
        # Create user in Firebase Authentication
        user = auth.create_user(email=email, password=password)
        
        # Add user data to Firestore
        if user_data:
            user_data['userid'] = user.uid
            db.collection('users').document(user.uid).set(user_data)
        
        return f"User created with UID: {user.uid}"
    except Exception as e:
        return f"Error creating user: {str(e)}"

# Define the user data structure
def user_data_structure(email, username, dob, contact_number):
    return {
        "email": email,
        "username": username,
        "birth": {
            "dob": dob,
            "age": 30  # Replace with actual age calculation if needed
        },
        "contact": {
            "tel": contact_number,
            "verified": False
        },
        "preferences": {
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

# Call initialize_firebase to set up Firebase when the script is run
initialize_firebase()
