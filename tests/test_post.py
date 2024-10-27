# tests/test_post.py
import unittest
from app import app

class PostTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_create_post(self):
        response = self.app.post('/posts', json={
            "user_id": "test-user-id",
            "title": "Test Post",
            "main_sentence": "This is a test post.",
            "media_url": "http://example.com/media.jpg",
            "location": "Test Location"
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn(b'Post created successfully', response.data)

if __name__ == '__main__':
    unittest.main()
