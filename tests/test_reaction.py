# tests/test_reaction.py
import unittest
from app import app

class ReactionTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_add_reaction(self):
        response = self.app.post('/posts/test-post-id/reactions', json={
            "reaction": "yey"
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Reaction added', response.data)

if __name__ == '__main__':
    unittest.main()
