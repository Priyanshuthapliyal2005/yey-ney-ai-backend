# tests/test_user.py
import unittest
from app import app

class UserTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_register_user(self):
        response = self.app.post('/users', json={
            "email": "test@example.com",
            "password": "test1234",
            "username": "testuser",
            "dob": "2000-01-01",
            "contact_number": "1234567890"
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn(b'User created', response.data)

if __name__ == '__main__':
    unittest.main()
