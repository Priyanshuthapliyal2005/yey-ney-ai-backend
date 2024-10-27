# tests/test_user.py
from services.user_service import create_user

def test_create_user():
    result = create_user("test@example.com", "password123", "testuser", "1990-01-01", "+1234567890")
    print(result)
