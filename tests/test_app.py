"""a"""
import unittest
from app import app

class TestApp(unittest.TestCase):
    """a"""
    def setUp(self):
        """a"""
        self.app = app.test_client()
        self.app.testing = True

    def test_home(self):
        """a"""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Welcome to the Flask App", response.data)

    def test_about(self):
        """a"""
        response = self.app.get('/about')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"This is the About Page", response.data)

if __name__ == "__main__":
    unittest.main()
