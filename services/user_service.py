import sys
import os

# Add the root directory to the path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from firebase_setup import db, auth
from models.user_model import user_data_structure

def create_user(email, password, username, dob, contact_number):
    try:
        user = auth.create_user(email=email, password=password)
        user_data = user_data_structure(user.uid, email, username, dob, contact_number)
        db.collection('users').document(user.uid).set(user_data)
        return f"User created with UID: {user.uid}"
    except Exception as e:
        return f"Error creating user: {str(e)}"

def create_sample_users():
    sample_users = [
        {
            "email": "sample1@example.com",
            "password": "password123",
            "username": "SampleUser1",
            "dob": "1990-01-01",
            "contact_number": "1234567890"
        },
        {
            "email": "sample2@example.com",
            "password": "password123",
            "username": "SampleUser2",
            "dob": "1992-02-02",
            "contact_number": "0987654321"
        },
        {
            "email": "sample3@example.com",
            "password": "password123",
            "username": "SampleUser3",
            "dob": "1994-03-03",
            "contact_number": "1122334455"
        }
    ]

    for user in sample_users:
        result = create_user(
            email=user['email'],
            password=user['password'],
            username=user['username'],
            dob=user['dob'],
            contact_number=user['contact_number']
        )
        print(result)

    print("Finished creating sample users.")

if __name__ == "__main__":
    create_sample_users()
    sys.exit()  # Explicitly exit the script
