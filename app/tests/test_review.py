import unittest
from datetime import datetime, timedelta
from app.models.review import Review

class TestReview(unittest.TestCase):

    def setUp(self):
        self.review = Review(place_id="123", user_id="456", rating=5, text="Great place!")

    def test_init(self):
        self.assertIsInstance(self.review, Review)
        self.assertEqual(self.review.place_id, "123")
        self.assertEqual(self.review.user_id, "456")
        self.assertEqual(self.review.rating, 5)
        self.assertEqual(self.review.text, "Great place!")
        self.assertIsNotNone(self.review.id)
        self.assertIsInstance(self.review.created_at, datetime)
        self.assertIsInstance(self.review.updated_at, datetime)

    def test_to_dict(self):
        self.review.id = "review_123"
        self.review.created_at = datetime(2023, 6, 1, 12, 0, 0)
        self.review.updated_at = datetime(2023, 6, 2, 12, 0, 0)
        review_dict = self.review.to_dict()
        expected_dict = {
            "id": "review_123",
            "place_id": "123",
            "user_id": "456",
            "rating": 5,
            "text": "Great place!",
            "created_at": "2023-06-01T12:00:00",
            "updated_at": "2023-06-02T12:00:00"
        }
        self.assertEqual(review_dict, expected_dict)

    def test_created_at_on_creation(self):
        now = datetime.now()
        self.assertLessEqual(now - self.review.created_at, timedelta(seconds=1))

    def test_updated_at_on_update(self):
        initial_time = self.review.updated_at
        self.review.text = "Amazing place!"
        self.assertNotEqual(self.review.updated_at, initial_time)

if __name__ == '__main__':
    unittest.main()
