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
        print("Firebase initialized successfully!")
    except Exception as e:
        print(f"Error initializing Firebase: {e}")

# Call initialize_firebase to set up Firebase
initialize_firebase()

# Firestore database reference
db = firestore.client()