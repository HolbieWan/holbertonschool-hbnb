import unittest
from datetime import datetime, timedelta
from unittest.mock import MagicMock
from models.review import Review

class TestReview(unittest.TestCase):

    def setUp(self):
        self.mock_data_manager = MagicMock()
        self.mock_data_manager.review_exists_with_attributes.return_value = False
        self.review = Review(
            place_id="123",
            user_id="456",
            rating=5,
            text="Great place!",
            data_manager=self.mock_data_manager
        )

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
            "review_id": "review_123",
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

    def test_invalid_rating(self):
        with self.assertRaises(ValueError) as context:
            Review(place_id="123", user_id="456", rating=6, text="Great place!", data_manager=self.mock_data_manager)
        self.assertEqual(str(context.exception), "Rating must be between 1 and 5")

    def test_missing_fields(self):
        with self.assertRaises(ValueError) as context:
            Review(place_id="123", user_id="", rating=5, text="Great place!", data_manager=self.mock_data_manager)
        self.assertEqual(str(context.exception), "All fields are required!")

    def test_duplicate_review(self):
        self.mock_data_manager.review_exists_with_attributes.return_value = True
        with self.assertRaises(ValueError) as context:
            Review(place_id="123", user_id="456", rating=5, text="Great place!", data_manager=self.mock_data_manager)
        self.assertEqual(str(context.exception), "Review already exists for this user and place")

if __name__ == '__main__':
    unittest.main()
