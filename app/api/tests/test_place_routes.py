# app/tests/test_places.py
import unittest
import json
from app import app 
from persistence.data_manager import DataManager
from datetime import datetime  # Ensure datetime is imported

class PlaceAPITestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        self.data_manager = DataManager('data/test_data_places.json')
        self.data_manager.storage = {}
        app.config['DATA_MANAGER_PLACES'] = self.data_manager

    def test_create_place(self):
        response = self.app.post('/places', json={
            'name': 'Test Place',
            'description': 'A nice place to stay',
            'address': '123 Test St',
            'city_id': 'city_123',
            'latitude': 37.7749,
            'longitude': -122.4194,
            'host_id': 'host_456',
            'num_rooms': 3,
            'num_bathrooms': 2,
            'price_per_night': 100,
            'max_guests': 4,
            'amenities': []
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn('place_id', json.loads(response.data))

    def test_get_places(self):
        self.app.post('/places', json={
            'name': 'Test Place',
            'description': 'A nice place to stay',
            'address': '123 Test St',
            'city_id': 'city_123',
            'latitude': 37.7749,
            'longitude': -122.4194,
            'host_id': 'host_456',
            'num_rooms': 3,
            'num_bathrooms': 2,
            'price_per_night': 100,
            'max_guests': 4,
            'amenities': []
        })
        response = self.app.get('/places')
        self.assertEqual(response.status_code, 200)
        places = json.loads(response.data)
        self.assertEqual(len(places), 1)

    def test_get_place(self):
        response = self.app.post('/places', json={
            'name': 'Test Place',
            'description': 'A nice place to stay',
            'address': '123 Test St',
            'city_id': 'city_123',
            'latitude': 37.7749,
            'longitude': -122.4194,
            'host_id': 'host_456',
            'num_rooms': 3,
            'num_bathrooms': 2,
            'price_per_night': 100,
            'max_guests': 4,
            'amenities': []
        })
        place_id = json.loads(response.data)['place_id']
        response = self.app.get(f'/places/{place_id}')
        self.assertEqual(response.status_code, 200)
        place = json.loads(response.data)
        self.assertEqual(place['place_name'], 'Test Place')  # Update to match 'place_name'

    def test_update_place(self):
        response = self.app.post('/places', json={
            'name': 'Test Place',
            'description': 'A nice place to stay',
            'address': '123 Test St',
            'city_id': 'city_123',
            'latitude': 37.7749,
            'longitude': -122.4194,
            'host_id': 'host_456',
            'num_rooms': 3,
            'num_bathrooms': 2,
            'price_per_night': 100,
            'max_guests': 4,
            'amenities': []
        })
        place_id = json.loads(response.data)['place_id']
        response = self.app.put(f'/places/{place_id}', json={
            'name': 'Updated Test Place'
        })
        self.assertEqual(response.status_code, 200)
        place = json.loads(response.data)
        self.assertEqual(place['place_name'], 'Updated Test Place')  # Update to match 'place_name'

    def test_delete_place(self):
        response = self.app.post('/places', json={
            'name': 'Test Place',
            'description': 'A nice place to stay',
            'address': '123 Test St',
            'city_id': 'city_123',
            'latitude': 37.7749,
            'longitude': -122.4194,
            'host_id': 'host_456',
            'num_rooms': 3,
            'num_bathrooms': 2,
            'price_per_night': 100,
            'max_guests': 4,
            'amenities': []
        })
        place_id = json.loads(response.data)['place_id']
        response = self.app.delete(f'/places/{place_id}')
        self.assertEqual(response.status_code, 204)
        response = self.app.get(f'/places/{place_id}')
        self.assertEqual(response.status_code, 404)

    def test_add_amenity_to_place(self):
        response = self.app.post('/places', json={
            'name': 'Test Place',
            'description': 'A nice place to stay',
            'address': '123 Test St',
            'city_id': 'city_123',
            'latitude': 37.7749,
            'longitude': -122.4194,
            'host_id': 'host_456',
            'num_rooms': 3,
            'num_bathrooms': 2,
            'price_per_night': 100,
            'max_guests': 4,
            'amenities': []
        })
        place_id = json.loads(response.data)['place_id']
        amenity_id = "amenity_123"
        response = self.app.post(f'/places/{place_id}/amenities/{amenity_id}')
        self.assertEqual(response.status_code, 200)
        place = json.loads(response.data)
        self.assertIn(amenity_id, place['amenities'])

    def test_remove_amenity_from_place(self):
        response = self.app.post('/places', json={
            'name': 'Test Place',
            'description': 'A nice place to stay',
            'address': '123 Test St',
            'city_id': 'city_123',
            'latitude': 37.7749,
            'longitude': -122.4194,
            'host_id': 'host_456',
            'num_rooms': 3,
            'num_bathrooms': 2,
            'price_per_night': 100,
            'max_guests': 4,
            'amenities': ['amenity_123']
        })
        place_id = json.loads(response.data)['place_id']
        amenity_id = "amenity_123"
        response = self.app.delete(f'/places/{place_id}/amenities/{amenity_id}')
        self.assertEqual(response.status_code, 200)
        place = json.loads(response.data)
        self.assertNotIn(amenity_id, place['amenities'])

if __name__ == '__main__':
    unittest.main()
