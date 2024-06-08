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

    def test_get_set_user_id(self):
        self.assertEqual(self.review.get_user_id(), "user1")
        self.review.set_user_id("user3")
        self.assertEqual(self.review.get_user_id(), "user3")

    def test_get_set_place_id(self):
        self.assertEqual(self.review.get_place_id(), "place1")
        self.review.set_place_id("place3")
        self.assertEqual(self.review.get_place_id(), "place3")

    def test_get_set_rating(self):
        self.assertEqual(self.review.get_rating(), 4)
        self.review.set_rating(3)
        self.assertEqual(self.review.get_rating(), 3)

    def test_get_set_comment(self):
        self.assertEqual(self.review.get_comment(), "Great place!")
        self.review.set_comment("Not so great")
        self.assertEqual(self.review.get_comment(), "Not so great")


if __name__ == '__main__':
    unittest.main()
