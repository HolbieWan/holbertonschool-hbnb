import unittest
from datetime import datetime, timedelta
from time import sleep
from app.models.amenity import Amenity
from app.models.base_model import BaseModel

class TestAmenity(unittest.TestCase):

    def setUp(self):
        self.amenity = Amenity(name="WiFi")

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
            "id": "amenity_123",
            "name": "WiFi",
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

if __name__ == '__main__':
    unittest.main()
