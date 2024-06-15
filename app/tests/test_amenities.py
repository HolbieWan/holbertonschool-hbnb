import unittest
from datetime import datetime, timedelta
from time import sleep
from unittest.mock import MagicMock
from models.amenity import Amenity
from models.base_model import BaseModel

class TestAmenity(unittest.TestCase):

    def setUp(self):
        # Mock the data manager
        self.mock_data_manager = MagicMock()
        self.mock_data_manager.amenity_exists_with_name.return_value = False
        self.amenity = Amenity(name="WiFi", data_manager=self.mock_data_manager)

    def test_init(self):
        self.assertIsInstance(self.amenity, BaseModel)
        self.assertEqual(self.amenity.name, "WiFi")
        self.assertIsNotNone(self.amenity.id)
        self.assertIsInstance(self.amenity.created_at, datetime)
        self.assertIsInstance(self.amenity.updated_at, datetime)

    def test_to_dict(self):
        self.amenity.id = "amenity_123"
        self.amenity.created_at = datetime(2023, 6, 1, 12, 0, 0)
        self.amenity.updated_at = datetime(2023, 6, 2, 12, 0, 0)
        amenity_dict = self.amenity.to_dict()
        expected_dict = {
            "amenity_id": "amenity_123",
            "amenity_name": "WiFi",
            "created_at": "2023-06-01T12:00:00",
            "updated_at": "2023-06-02T12:00:00"
        }
        self.assertEqual(amenity_dict, expected_dict)

    def test_created_at_and_updated_at_on_creation(self):
        now = datetime.now()
        self.assertAlmostEqual(self.amenity.created_at, now, delta=timedelta(seconds=1))
        self.assertAlmostEqual(self.amenity.updated_at, now, delta=timedelta(seconds=1))

    def test_updated_at_on_update(self):
        old_updated_at = self.amenity.updated_at
        sleep(1)  # Sleep for a second to ensure the updated_at timestamp will change
        self.amenity.name = "Updated WiFi"
        new_updated_at = self.amenity.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)
        self.assertGreater(new_updated_at, old_updated_at)

    def test_amenity_already_exists(self):
        self.mock_data_manager.amenity_exists_with_name.return_value = True
        with self.assertRaises(ValueError) as context:
            Amenity(name="WiFi", data_manager=self.mock_data_manager)
        self.assertEqual(str(context.exception), "This amenity already exists!")

    def test_empty_name(self):
        with self.assertRaises(ValueError) as context:
            Amenity(name="", data_manager=self.mock_data_manager)
        self.assertEqual(str(context.exception), "Amenity name is required!")

if __name__ == '__main__':
    unittest.main()
