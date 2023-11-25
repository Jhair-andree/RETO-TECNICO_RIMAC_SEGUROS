import unittest
import json
import requests
from app import app, db, User

class FlaskAppTests(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_add_user(self):
        user_data = {'username': 'test_user', 'email': 'test@example.com'}
        response = self.app.post('/add_user', json=user_data)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(User.query.count(), 1)

    def test_get_users(self):
        user_data = {'username': 'test_user', 'email': 'test@example.com'}
        self.app.post('/add_user', json=user_data)

        response = self.app.get('/get_users')
        data = json.loads(response.get_data(as_text=True))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data['users']), 1)
        self.assertEqual(data['users'][0]['username'], 'test_user')
        self.assertEqual(data['users'][0]['email'], 'test@example.com')

if __name__ == '__main__':
    unittest.main()
