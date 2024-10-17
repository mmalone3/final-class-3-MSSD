# test_app.py

import unittest
from app import app

class FlaskAppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_track_activity(self):
        response = self.app.post('/track', json={'activity': 'Work', 'color': 'blue'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('Tracking started', response.get_json()['message'])

    def test_get_history(self):
        # First, add an activity
        self.app.post('/track', json={'activity': 'Work', 'color': 'blue'})
        
        # Now, get the history
        response = self.app.get('/history')
        self.assertEqual(response.status_code, 200)
        self.assertGreater(len(response.get_json()), 0)

    def test_track_activity_without_activity(self):
        response = self.app.post('/track', json={'color': 'blue'})
        self.assertEqual(response.status_code, 400)
        self.assertIn('Activity not provided', response.get_json()['error'])

if __name__ == '__main__':
    unittest.main()