# app/tests/test_country_routes.py
import unittest
import json
from app import app
from persistence.data_manager import DataManager
from datetime import datetime

class CountryAPITestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        self.data_manager = DataManager('data/test_data_countries.json')
        self.data_manager.storage = {}
        app.config['DATA_MANAGER_COUNTRIES'] = self.data_manager

    def test_create_country(self):
        response = self.app.post('/country', json={
            'name': 'Test Country',
            'code': 'TC'
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn('country_id', json.loads(response.data))

    def test_get_countries(self):
        self.app.post('/country', json={
            'name': 'Test Country',
            'code': 'TC'
        })
        response = self.app.get('/country')
        self.assertEqual(response.status_code, 200)
        countries = json.loads(response.data)
        self.assertEqual(len(countries), 1)

    def test_get_country_code(self):
        response = self.app.post('/country', json={
            'name': 'Test Country',
            'code': 'TC'
        })
        country_code = json.loads(response.data)['code']
        response = self.app.get(f'/country/{country_code}')
        self.assertEqual(response.status_code, 200)
        country = json.loads(response.data)
        self.assertEqual(country['code'], 'TC')

    def test_update_country(self):
        response = self.app.post('/country', json={
            'name': 'Test Country',
            'code': 'TC'
        })
        country_id = json.loads(response.data)['country_id']
        response = self.app.put(f'/country/{country_id}', json={
            'name': 'Updated Country',
            'code': 'UC'
        })
        self.assertEqual(response.status_code, 200)
        country = json.loads(response.data)
        self.assertEqual(country['name'], 'Updated Country')
        self.assertEqual(country['code'], 'UC')

    def test_delete_country(self):
        response = self.app.post('/country', json={
            'name': 'Test Country',
            'code': 'TC'
        })
        country_id = json.loads(response.data)['country_id']
        response = self.app.delete(f'/country/{country_id}')
        self.assertEqual(response.status_code, 204)
        response = self.app.get(f'/country/{country_id}')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
