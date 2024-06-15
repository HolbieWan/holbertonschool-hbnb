import unittest
from unittest.mock import MagicMock, patch
from datetime import datetime
from persistence.data_manager import DataManager
from models.user import User
from models.place import Place
from models.review import Review
from models.city import City
from models.country import Country
from models.amenity import Amenity
import os
import json


class TestDataManager(unittest.TestCase):

    def setUp(self):
        self.data_manager = DataManager('data/test_data.json')
        self.user = User(
            email="test@gmail.com",
            first_name="John",
            last_name="Doe",
            data_manager=self.data_manager
        )
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
            data_manager=self.data_manager
        )
        self.review = Review(
            place_id="place_123",
            user_id="user_456",
            rating=5,
            text="Great place!",
            data_manager=self.data_manager
        )
        self.city = City(
            name="New York",
            country_id="US",
            data_manager=self.data_manager
        )
        self.country = Country(
            name="United States",
            code="US"
        )
        self.amenity = Amenity(
            name="WiFi",
            data_manager=self.data_manager
        )

    def tearDown(self):
        # Clean up the test data file after each test
        if os.path.exists('data/test_data.json'):
            os.remove('data/test_data.json')

    def test_init(self):
        self.assertIsInstance(self.data_manager.storage, dict)

    def test_create_directory_if_not_exists(self):
        with patch('os.makedirs') as mock_makedirs:
            dm = DataManager('data/test/test_data.json')
            mock_makedirs.assert_called_once_with('data/test')

    def test_load_from_json(self):
        with open('data/test_data.json', 'w') as file:
            json.dump({
                "User": {
                    self.user.id: self.user.to_dict()
                }
            }, file)
        self.data_manager.load_from_json()
        self.assertIn('User', self.data_manager.storage)
        self.assertIn(self.user.id, self.data_manager.storage['User'])

    def test_dict_to_entity(self):
        user_data = self.user.to_dict()
        entity = self.data_manager.dict_to_entity('User', user_data)
        self.assertIsInstance(entity, User)
        self.assertEqual(entity.email, self.user.email)

    def test_save_user(self):
        saved_user = self.data_manager.save(self.user)
        self.assertEqual(saved_user, self.user)
        self.assertIn('User', self.data_manager.storage)
        self.assertIn(self.user.id, self.data_manager.storage['User'])
        self.assertEqual(self.data_manager.storage['User'][self.user.id], self.user)

    def test_get_user(self):
        self.data_manager.save(self.user)
        retrieved_user = self.data_manager.get(self.user.id, 'User')
        self.assertEqual(retrieved_user, self.user)

    def test_update_user(self):
        self.data_manager.save(self.user)
        self.user.first_name = "Updated John"
        updated_user = self.data_manager.update(self.user)
        self.assertEqual(updated_user.first_name, "Updated John")
        self.assertEqual(self.data_manager.storage['User'][self.user.id].first_name, "Updated John")

    def test_delete_user(self):
        self.data_manager.save(self.user)
        result = self.data_manager.delete(self.user.id, 'User')
        self.assertTrue(result)
        self.assertNotIn(self.user.id, self.data_manager.storage['User'])

    def test_get_by_email(self):
        self.data_manager.save(self.user)
        retrieved_user = self.data_manager.get_by_email(self.user.email)
        self.assertEqual(retrieved_user, self.user)

    def test_get_country_by_code(self):
        self.data_manager.save(self.country)
        retrieved_country = self.data_manager.get_country_by_code(self.country.code)
        self.assertEqual(retrieved_country, self.country)

    def test_place_exists_with_attributes(self):
        self.data_manager.save(self.place)
        exists = self.data_manager.place_exists_with_attributes(
            name=self.place.name,
            address=self.place.address,
            city_id=self.place.city_id,
            host_id=self.place.host_id,
            num_rooms=self.place.num_rooms,
            num_bathrooms=self.place.num_bathrooms,
            price_per_night=self.place.price_per_night,
            max_guests=self.place.max_guests
        )
        self.assertTrue(exists)

    def test_review_exists_with_attributes(self):
        self.data_manager.save(self.review)
        exists = self.data_manager.review_exists_with_attributes(
            place_id=self.review.place_id,
            user_id=self.review.user_id
        )
        self.assertTrue(exists)

    def test_city_exists_with_name_and_country(self):
        self.data_manager.save(self.city)
        exists = self.data_manager.city_exists_with_name_and_country(
            name=self.city.name,
            country_id=self.city.country_id
        )
        self.assertTrue(exists)

    def test_amenity_exists_with_name(self):
        self.data_manager.save(self.amenity)
        exists = self.data_manager.amenity_exists_with_name(self.amenity.name)
        self.assertTrue(exists)

    def test_get_reviews_by_place_id(self):
        self.data_manager.save(self.review)
        reviews = self.data_manager.get_reviews_by_place_id(self.review.place_id)
        self.assertIn(self.review, reviews)

    def test_get_reviews_by_user_id(self):
        self.data_manager.save(self.review)
        reviews = self.data_manager.get_reviews_by_user_id(self.review.user_id)
        self.assertIn(self.review, reviews)

    def test_save_to_json(self):
        self.data_manager.save(self.user)
        self.data_manager.save_to_json()

        with open('data/test_data.json', 'r') as file:
            data = json.load(file)

        self.assertIn('User', data)
        self.assertIn(self.user.id, data['User'])
        self.assertEqual(data['User'][self.user.id], self.user.to_dict())

if __name__ == '__main__':
    unittest.main()
