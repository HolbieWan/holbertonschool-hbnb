# app/tests/test_city_routes.py
import unittest
import json
from app import app
from persistence.data_manager import DataManager

class CityAPITestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        self.data_manager = DataManager('data/test_data_cities.json')
        self.data_manager.storage = {}
        app.config['DATA_MANAGER_CITIES'] = self.data_manager

    def test_create_city(self):
        response = self.app.post('/cities', json={
            'name': 'Test City',
            'country_id': 'country_123'
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn('city_id', json.loads(response.data))

    def test_get_cities(self):
        self.app.post('/cities', json={
            'name': 'Test City',
            'country_id': 'country_123'
        })
        response = self.app.get('/cities')
        self.assertEqual(response.status_code, 200)
        cities = json.loads(response.data)
        self.assertEqual(len(cities), 1)

    def test_get_city(self):
        response = self.app.post('/cities', json={
            'name': 'Test City',
            'country_id': 'country_123'
        })
        city_id = json.loads(response.data)['city_id']
        response = self.app.get(f'/cities/{city_id}')
        self.assertEqual(response.status_code, 200)
        city = json.loads(response.data)
        self.assertEqual(city['city_name'], 'Test City')

    def test_update_city(self):
        response = self.app.post('/cities', json={
            'name': 'Test City',
            'country_id': 'country_123'
        })
        city_id = json.loads(response.data)['city_id']
        response = self.app.put(f'/cities/{city_id}', json={
            'name': 'Updated Test City',
            'country_id': 'country_456'
        })
        self.assertEqual(response.status_code, 200)
        city = json.loads(response.data)
        self.assertEqual(city['city_name'], 'Updated Test City')
        self.assertEqual(city['country_id'], 'country_456')

    def test_delete_city(self):
        response = self.app.post('/cities', json={
            'name': 'Test City',
            'country_id': 'country_123'
        })
        city_id = json.loads(response.data)['city_id']
        response = self.app.delete(f'/cities/{city_id}')
        self.assertEqual(response.status_code, 204)
        response = self.app.get(f'/cities/{city_id}')
        self.assertEqual(response.status_code, 404)

    def test_get_city_by_country_code(self):
        self.app.post('/cities', json={
            'name': 'Test City 1',
            'country_id': 'country_123'
        })
        self.app.post('/cities', json={
            'name': 'Test City 2',
            'country_id': 'country_123'
        })
        response = self.app.get('/country/country_123/cities')
        self.assertEqual(response.status_code, 200)
        cities = json.loads(response.data)
        self.assertEqual(len(cities), 2)

if __name__ == '__main__':
    unittest.main()
