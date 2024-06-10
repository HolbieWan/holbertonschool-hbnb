from app.models.place import Place
from app.models.review import Review
import unittest

class TestRelationships(unittest.TestCase):

    def test_place_host_user_relationship(self):
        # Creating a Place instance with required arguments
        place = Place(
            name="Cozy Cabin",
            description="A charming cabin in the woods",
            address="123 Forest Street",
            city_id="city_123",
            latitude=37.7749,
            longitude=-122.4194,
            host_id="host_123",
            num_rooms=2,
            num_bathrooms=1,
            price_per_night=100,
            max_guests=4
        )
        self.assertEqual(place.host_id, "host_123")
        # Retrieve host user object based on host_id and assert its attributes

    def test_review_place_user_relationships(self):
        place_id = "place_123"
        user_id = "user_456"
        review = Review(
            place_id=place_id,
            user_id=user_id,
            rating=5,
            text="Amazing place!"
        )
        self.assertEqual(review.place_id, place_id)
        self.assertEqual(review.user_id, user_id)
        # Retrieve place and user objects based on place_id and user_id and assert their attributes

if __name__ == '__main__':
    unittest.main()
