# app/tests/test_users.py
import unittest
import json
from app.routes.users_route import app, data_manager

class UserAPITestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        data_manager.storage = {}

    def test_create_user(self):
        response = self.app.post('/users', json={
            'email': 'test@example.com',
            'first_name': 'Test',
            'last_name': 'User'
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn('id', json.loads(response.data))

    def test_get_users(self):
        self.app.post('/users', json={
            'email': 'test@example.com',
            'first_name': 'Test',
            'last_name': 'User'
        })
        response = self.app.get('/users')
        self.assertEqual(response.status_code, 200)
        users = json.loads(response.data)
        self.assertEqual(len(users), 1)

    def test_get_user(self):
        response = self.app.post('/users', json={
            'email': 'test@example.com',
            'first_name': 'Test',
            'last_name': 'User'
        })
        user_id = json.loads(response.data)['id']
        response = self.app.get(f'/users/{user_id}')
        self.assertEqual(response.status_code, 200)
        user = json.loads(response.data)
        self.assertEqual(user['email'], 'test@example.com')

    def test_update_user(self):
        response = self.app.post('/users', json={
            'email': 'test@example.com',
            'first_name': 'Test',
            'last_name': 'User'
        })
        user_id = json.loads(response.data)['id']
        response = self.app.put(f'/users/{user_id}', json={
            'first_name': 'Updated'
        })
        self.assertEqual(response.status_code, 200)
        user = json.loads(response.data)
        self.assertEqual(user['first_name'], 'Updated')

    def test_delete_user(self):
        response = self.app.post('/users', json={
            'email': 'test@example.com',
            'first_name': 'Test',
            'last_name': 'User'
        })
        user_id = json.loads(response.data)['id']
        response = self.app.delete(f'/users/{user_id}')
        self.assertEqual(response.status_code, 204)
        response = self.app.get(f'/users/{user_id}')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
