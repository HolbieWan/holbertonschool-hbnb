import unittest
from unittest.mock import MagicMock
from models.place import Place
from models.review import Review
from models.user import User
from models.city import City
from models.amenity import Amenity

class TestRelationships(unittest.TestCase):

    def setUp(self):
        # Mock DataManager to avoid actual data persistence and retrieval
        self.mock_data_manager = MagicMock()
        self.mock_data_manager.place_exists_with_attributes.return_value = False
        self.mock_data_manager.review_exists_with_attributes.return_value = False
        self.mock_data_manager.city_exists_with_name_and_country.return_value = False
        self.mock_data_manager.amenity_exists_with_name.return_value = False

        # Create User instance
        self.user = User(
            email="host@example.com",
            first_name="Host",
            last_name="User",
            data_manager=self.mock_data_manager
        )
        self.user.id = "host_123"

        # Create City instance
        self.city = City(
            name="San Francisco",
            country_id="US",
            data_manager=self.mock_data_manager
        )
        self.city.id = "city_123"

        # Create Amenity instance
        self.amenity = Amenity(
            name="WiFi",
            data_manager=self.mock_data_manager
        )
        self.amenity.id = "amenity_123"

        # Create Place instance
        self.place = Place(
            name="Cozy Cabin",
            description="A charming cabin in the woods",
            address="123 Forest Street",
            city_id=self.city.id,
            latitude=37.7749,
            longitude=-122.4194,
            host_id=self.user.id,
            num_rooms=2,
            num_bathrooms=1,
            price_per_night=100,
            max_guests=4,
            amenities=[self.amenity.id],
            data_manager=self.mock_data_manager
        )
        self.place.id = "place_123"

        # Create Review instance
        self.review = Review(
            place_id=self.place.id,
            user_id=self.user.id,
            rating=5,
            text="Amazing place!",
            data_manager=self.mock_data_manager
        )
        self.review.id = "review_123"

    def test_place_host_user_relationship(self):
        self.assertEqual(self.place.host_id, self.user.id)
        self.assertEqual(self.place.host_id, "host_123")

    def test_review_place_user_relationships(self):
        self.assertEqual(self.review.place_id, self.place.id)
        self.assertEqual(self.review.user_id, self.user.id)
        self.assertEqual(self.review.place_id, "place_123")
        self.assertEqual(self.review.user_id, "host_123")

    def test_place_city_relationship(self):
        self.assertEqual(self.place.city_id, self.city.id)
        self.assertEqual(self.place.city_id, "city_123")

    def test_place_amenity_relationship(self):
        self.assertIn(self.amenity.id, self.place.amenities)
        self.assertIn("amenity_123", self.place.amenities)

    def test_adding_amenity_to_place(self):
        new_amenity = Amenity(name="Pool", data_manager=self.mock_data_manager)
        new_amenity.id = "amenity_456"
        self.place.add_amenity(new_amenity.id)
        self.assertIn(new_amenity.id, self.place.amenities)

    def test_removing_amenity_from_place(self):
        self.place.remove_amenity(self.amenity.id)
        self.assertNotIn(self.amenity.id, self.place.amenities)

if __name__ == '__main__':
    unittest.main()
