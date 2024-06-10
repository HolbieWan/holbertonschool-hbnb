import unittest
from datetime import datetime
from unittest.mock import patch
from app.models.city import City
from app.models.base_model import BaseModel

class TestCity(unittest.TestCase):

    def setUp(self):
        self.city = City(name="New York", country_id="US")

    def test_init(self):
        self.assertIsInstance(self.city, BaseModel)
        self.assertEqual(self.city.name, "New York")
        self.assertEqual(self.city.country_id, "US")
        self.assertIsNotNone(self.city.id)
        self.assertIsInstance(self.city.created_at, datetime)
        self.assertIsInstance(self.city.updated_at, datetime)

    def test_to_dict(self):
        self.city.id = "city_123"
        self.city.created_at = datetime(2023, 6, 1, 12, 0, 0)
        self.city.updated_at = datetime(2023, 6, 2, 12, 0, 0)
        city_dict = self.city.to_dict()
        expected_dict = {
            "id": "city_123",
            "name": "New York",
            "state_id": "US",
            "created_at": "2023-06-01T12:00:00",
            "updated_at": "2023-06-02T12:00:00"
        }
        self.assertEqual(city_dict, expected_dict)

    @patch('app.models.base_model.datetime')
    def test_created_at_and_updated_at_on_creation(self, mock_datetime):
        mock_datetime.now.return_value = datetime(2023, 6, 1, 12, 0, 0)
        new_city = City(name="Los Angeles", country_id="US")
        self.assertEqual(new_city.created_at, datetime(2023, 6, 1, 12, 0, 0))
        self.assertEqual(new_city.updated_at, datetime(2023, 6, 1, 12, 0, 0))

    @patch('app.models.base_model.datetime')
    def test_updated_at_on_update(self, mock_datetime):
        initial_time = datetime(2023, 6, 1, 12, 0, 0)
        updated_time = datetime(2023, 6, 2, 12, 0, 0)
        mock_datetime.now.return_value = initial_time
        city = City(name="San Francisco", country_id="US")
        self.assertEqual(city.updated_at, initial_time)
        mock_datetime.now.return_value = updated_time
        city.name = "Updated San Francisco"
        self.assertEqual(city.updated_at, updated_time)

if __name__ == '__main__':
    unittest.main()
