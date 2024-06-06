import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    def setUp(self):
        self.review = Review("user1", "place1", 4, "Great place!")

    def test_review_attributes(self):

        self.assertEqual(self.review.user_id, "user1")
        self.assertEqual(self.review.place_id, "place1")
        self.assertEqual(self.review.rating, 4)
        self.assertEqual(self.review.comment, "Great place!")

    def test_review_inheritance(self):

        self.assertIsInstance(self.review, BaseModel)

    def test_modify_review_attributes(self):
        self.review.user_id = "user2"
        self.review.place_id = "place2"
        self.review.rating = 5
        self.review.comment = "Excellent service!"

        self.assertEqual(self.review.user_id, "user2")
        self.assertEqual(self.review.place_id, "place2")
        self.assertEqual(self.review.rating, 5)
        self.assertEqual(self.review.comment, "Excellent service!")


if __name__ == '__main__':
    unittest.main()
