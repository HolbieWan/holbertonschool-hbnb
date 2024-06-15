# app/tests/test_amenity_routes.py
import unittest
import json
from app import app
from persistence.data_manager import DataManager

class AmenityAPITestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        self.data_manager = DataManager('data/test_data_amenities.json')
        self.data_manager.storage = {}
        app.config['DATA_MANAGER_AMENITIES'] = self.data_manager

    def test_create_amenity(self):
        response = self.app.post('/amenities', json={
            'name': 'WiFi'
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn('amenity_id', json.loads(response.data))

    def test_get_amenities(self):
        self.app.post('/amenities', json={
            'name': 'WiFi'
        })
        response = self.app.get('/amenities')
        self.assertEqual(response.status_code, 200)
        amenities = json.loads(response.data)
        self.assertEqual(len(amenities), 1)

    def test_get_amenity(self):
        response = self.app.post('/amenities', json={
            'name': 'WiFi'
        })
        amenity_id = json.loads(response.data)['amenity_id']
        response = self.app.get(f'/amenities/{amenity_id}')
        self.assertEqual(response.status_code, 200)
        amenity = json.loads(response.data)
        self.assertEqual(amenity['amenity_name'], 'WiFi')

    def test_update_amenity(self):
        response = self.app.post('/amenities', json={
            'name': 'WiFi'
        })
        amenity_id = json.loads(response.data)['amenity_id']
        response = self.app.put(f'/amenities/{amenity_id}', json={
            'name': 'Updated WiFi'
        })
        self.assertEqual(response.status_code, 200)
        amenity = json.loads(response.data)
        self.assertEqual(amenity['amenity_name'], 'Updated WiFi')

    def test_delete_amenity(self):
        response = self.app.post('/amenities', json={
            'name': 'WiFi'
        })
        amenity_id = json.loads(response.data)['amenity_id']
        response = self.app.delete(f'/amenities/{amenity_id}')
        self.assertEqual(response.status_code, 204)
        response = self.app.get(f'/amenities/{amenity_id}')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
