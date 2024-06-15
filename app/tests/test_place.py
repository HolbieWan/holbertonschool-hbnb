import unittest
from datetime import datetime, timedelta
from time import sleep
from unittest.mock import MagicMock
from models.place import Place
from models.base_model import BaseModel

class TestPlace(unittest.TestCase):

    def setUp(self):
        self.mock_data_manager = MagicMock()
        self.mock_data_manager.place_exists_with_attributes.return_value = False
        self.place = Place(
            name="Test Place",
            description="A nice place to stay",
            address="123 Test St",
            city_id="city_123",
            latitude=37.7749,
            longitude=-122.4194,
            host_id="host_456",
            num_rooms=3,
            num_bathrooms=2,
            price_per_night=100,
            max_guests=4,
            data_manager=self.mock_data_manager
        )

    def test_init(self):
        self.assertIsInstance(self.place, BaseModel)
        self.assertEqual(self.place.name, "Test Place")
        self.assertEqual(self.place.description, "A nice place to stay")
        self.assertEqual(self.place.address, "123 Test St")
        self.assertEqual(self.place.city_id, "city_123")
        self.assertEqual(self.place.latitude, 37.7749)
        self.assertEqual(self.place.longitude, -122.4194)
        self.assertEqual(self.place.host_id, "host_456")
        self.assertEqual(self.place.num_rooms, 3)
        self.assertEqual(self.place.num_bathrooms, 2)
        self.assertEqual(self.place.price_per_night, 100)
        self.assertEqual(self.place.max_guests, 4)
        self.assertIsNotNone(self.place.id)
        self.assertIsInstance(self.place.created_at, datetime)
        self.assertIsInstance(self.place.updated_at, datetime)

    def test_to_dict(self):
        self.place.id = "place_123"
        self.place.created_at = datetime(2023, 6, 1, 12, 0, 0)
        self.place.updated_at = datetime(2023, 6, 2, 12, 0, 0)
        place_dict = self.place.to_dict()
        expected_dict = {
            "place_id": "place_123",
            "place_name": "Test Place",
            "description": "A nice place to stay",
            "address": "123 Test St",
            "city_id": "city_123",
            "latitude": 37.7749,
            "longitude": -122.4194,
            "host_id": "host_456",
            "num_rooms": 3,
            "num_bathrooms": 2,
            "price_per_night": 100,
            "max_guests": 4,
            "amenities": [],
            "created_at": "2023-06-01T12:00:00",
            "updated_at": "2023-06-02T12:00:00"
        }
        self.assertEqual(place_dict, expected_dict)

    def test_created_at_and_updated_at_on_creation(self):
        now = datetime.now()
        self.assertAlmostEqual(self.place.created_at, now, delta=timedelta(seconds=1))
        self.assertAlmostEqual(self.place.updated_at, now, delta=timedelta(seconds=1))

    def test_updated_at_on_update(self):
        old_updated_at = self.place.updated_at
        sleep(2)  # Sleep for 2 seconds to ensure the updated_at timestamp will change
        self.place.name = "Updated Test Place"
        new_updated_at = self.place.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)
        self.assertGreater(new_updated_at, old_updated_at)

    def test_add_amenity(self):
        self.place.add_amenity("amenity_1")
        self.assertIn("amenity_1", self.place.amenities)
        self.assertIn("amenity_1", self.place.to_dict()["amenities"])

    def test_remove_amenity(self):
        self.place.add_amenity("amenity_1")
        self.place.remove_amenity("amenity_1")
        self.assertNotIn("amenity_1", self.place.amenities)
        self.assertNotIn("amenity_1", self.place.to_dict()["amenities"])

    def test_place_already_exists(self):
        self.mock_data_manager.place_exists_with_attributes.return_value = True
        with self.assertRaises(ValueError) as context:
            Place(
                name="Test Place",
                description="A nice place to stay",
                address="123 Test St",
                city_id="city_123",
                latitude=37.7749,
                longitude=-122.4194,
                host_id="host_456",
                num_rooms=3,
                num_bathrooms=2,
                price_per_night=100,
                max_guests=4,
                data_manager=self.mock_data_manager
            )
        self.assertEqual(str(context.exception), "Place already exists!")

    def test_invalid_latitude(self):
        with self.assertRaises(ValueError) as context:
            Place(
                name="Test Place",
                description="A nice place to stay",
                address="123 Test St",
                city_id="city_123",
                latitude=100,
                longitude=-122.4194,
                host_id="host_456",
                num_rooms=3,
                num_bathrooms=2,
                price_per_night=100,
                max_guests=4,
                data_manager=self.mock_data_manager
            )
        self.assertEqual(str(context.exception), "Latitude must be between -90 and 90 degrees")

    def test_invalid_longitude(self):
        with self.assertRaises(ValueError) as context:
            Place(
                name="Test Place",
                description="A nice place to stay",
                address="123 Test St",
                city_id="city_123",
                latitude=37.7749,
                longitude=-200,
                host_id="host_456",
                num_rooms=3,
                num_bathrooms=2,
                price_per_night=100,
                max_guests=4,
                data_manager=self.mock_data_manager
            )
        self.assertEqual(str(context.exception), "Longitude must be between -180 and 180 degrees")

if __name__ == '__main__':
    unittest.main()
