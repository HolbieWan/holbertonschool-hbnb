import unittest
from datetime import datetime
from unittest.mock import MagicMock, patch
from models.city import City
from models.base_model import BaseModel

class TestCity(unittest.TestCase):

    def setUp(self):
        self.mock_data_manager = MagicMock()
        self.mock_data_manager.city_exists_with_name_and_country.return_value = False
        self.city = City(name="New York", country_id="US", data_manager=self.mock_data_manager)

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
            "city_id": "city_123",
            "city_name": "New York",
            "country_id": "US",
            "created_at": "2023-06-01T12:00:00",
            "updated_at": "2023-06-02T12:00:00"
        }
        self.assertEqual(city_dict, expected_dict)

    @patch('models.base_model.datetime')
    def test_created_at_and_updated_at_on_creation(self, mock_datetime):
        mock_datetime.now.return_value = datetime(2023, 6, 1, 12, 0, 0)
        new_city = City(name="Los Angeles", country_id="US", data_manager=self.mock_data_manager)
        self.assertEqual(new_city.created_at, datetime(2023, 6, 1, 12, 0, 0))
        self.assertEqual(new_city.updated_at, datetime(2023, 6, 1, 12, 0, 0))

    @patch('models.base_model.datetime')
    def test_updated_at_on_update(self, mock_datetime):
        initial_time = datetime(2023, 6, 1, 12, 0, 0)
        updated_time = datetime(2023, 6, 2, 12, 0, 0)
        mock_datetime.now.return_value = initial_time
        city = City(name="San Francisco", country_id="US", data_manager=self.mock_data_manager)
        self.assertEqual(city.updated_at, initial_time)
        mock_datetime.now.return_value = updated_time
        city.name = "Updated San Francisco"
        self.assertEqual(city.updated_at, updated_time)

    def test_city_already_exists(self):
        self.mock_data_manager.city_exists_with_name_and_country.return_value = True
        with self.assertRaises(ValueError) as context:
            City(name="New York", country_id="US", data_manager=self.mock_data_manager)
        self.assertEqual(str(context.exception), "City name must be unique within the same country")

    def test_empty_name(self):
        with self.assertRaises(ValueError) as context:
            City(name="", country_id="US", data_manager=self.mock_data_manager)
        self.assertEqual(str(context.exception), "City name is required!")

    def test_empty_country_id(self):
        with self.assertRaises(ValueError) as context:
            City(name="New York", country_id="", data_manager=self.mock_data_manager)
        self.assertEqual(str(context.exception), "Country ID is required!")

if __name__ == '__main__':
    unittest.main()
