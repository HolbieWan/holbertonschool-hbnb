# app/api/tests/test_users.py
import unittest
import os
import json
from app import app
from persistence.data_manager import DataManager
from models.user import User

class TestUserAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        self.data_manager = DataManager('data/test_data_users.json')
        self.data_manager.storage = {}
        app.config['DATA_MANAGER_USERS'] = self.data_manager

    def tearDown(self):
        if os.path.exists('data/test_data_users.json'):
            os.remove('data/test_data_users.json')

    def test_create_user(self):
        response = self.app.post('/users', json={
            'email': 'test@gmail.com',
            'first_name': 'Test',
            'last_name': 'User'
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn('user_id', json.loads(response.data))

    def test_get_users(self):
        self.app.post('/users', json={
            'email': 'test@gmail.com',
            'first_name': 'Test',
            'last_name': 'User'
        })
        response = self.app.get('/users')
        self.assertEqual(response.status_code, 200)
        users = json.loads(response.data)
        self.assertEqual(len(users), 1)

    def test_get_user(self):
        response = self.app.post('/users', json={
            'email': 'test@gmail.com',
            'first_name': 'Test',
            'last_name': 'User'
        })
        user_id = json.loads(response.data)['user_id']
        response = self.app.get(f'/users/{user_id}')
        self.assertEqual(response.status_code, 200)
        user = json.loads(response.data)
        self.assertEqual(user['email'], 'test@gmail.com')

    def test_update_user(self):
        response = self.app.post('/users', json={
            'email': 'test@gmail.com',
            'first_name': 'Test',
            'last_name': 'User'
        })
        user_id = json.loads(response.data)['user_id']
        response = self.app.put(f'/users/{user_id}', json={
            'first_name': 'Updated'
        })
        self.assertEqual(response.status_code, 200)
        user = json.loads(response.data)
        self.assertEqual(user['first_name'], 'Updated')

    def test_delete_user(self):
        response = self.app.post('/users', json={
            'email': 'test@gmail.com',
            'first_name': 'Test',
            'last_name': 'User'
        })
        user_id = json.loads(response.data)['user_id']
        response = self.app.delete(f'/users/{user_id}')
        self.assertEqual(response.status_code, 204)
        response = self.app.get(f'/users/{user_id}')
        self.assertEqual(response.status_code, 404)

    def test_invalid_email_format(self):
        response = self.app.post('/users', json={
            'email': 'invalid-email',
            'first_name': 'Test',
            'last_name': 'User'
        })
        self.assertEqual(response.status_code, 400)

    def test_missing_email(self):
        response = self.app.post('/users', json={
            'first_name': 'Test',
            'last_name': 'User'
        })
        self.assertEqual(response.status_code, 400)

    def test_empty_fields(self):
        response = self.app.post('/users', json={
            'email': '',
            'first_name': '',
            'last_name': ''
        })
        self.assertEqual(response.status_code, 400)

    def test_duplicate_email(self):
        self.app.post('/users', json={
            'email': 'test@gmail.com',
            'first_name': 'Test',
            'last_name': 'User'
        })
        response = self.app.post('/users', json={
            'email': 'test@gmail.com',
            'first_name': 'Test2',
            'last_name': 'User2'
        })
        self.assertEqual(response.status_code, 409)

    def test_update_user_email_exists(self):
        response1 = self.app.post('/users', json={
            'email': 'test@gmail.com',
            'first_name': 'Test',
            'last_name': 'User'
        })
        response2 = self.app.post('/users', json={
            'email': 'test2@gmail.com',
            'first_name': 'Test2',
            'last_name': 'User2'
        })
        user_id = json.loads(response1.data)['user_id']
        response = self.app.put(f'/users/{user_id}', json={
            'email': 'test2@gmail.com'
        })
        self.assertEqual(response.status_code, 409)

if __name__ == '__main__':
    unittest.main()
