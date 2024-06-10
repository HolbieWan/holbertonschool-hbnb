import unittest
from datetime import datetime
from unittest.mock import patch
from app.models.user import User
from app.models.base_model import BaseModel

class TestUser(unittest.TestCase):

    def setUp(self):
        self.user = User(
            email="test@example.com",
            first_name="John",
            last_name="Doe"
        )

    def test_init(self):
        self.assertIsInstance(self.user, BaseModel)
        self.assertEqual(self.user.email, "test@example.com")
        self.assertEqual(self.user.first_name, "John")
        self.assertEqual(self.user.last_name, "Doe")
        self.assertIsNotNone(self.user.id)
        self.assertIsInstance(self.user.created_at, datetime)
        self.assertIsInstance(self.user.updated_at, datetime)

    def test_to_dict(self):
        self.user.id = "user_123"
        self.user.created_at = datetime(2023, 6, 1, 12, 0, 0)
        self.user.updated_at = datetime(2023, 6, 2, 12, 0, 0)
        user_dict = self.user.to_dict()
        expected_dict = {
            "id": "user_123",
            "email": "test@example.com",
            "first_name": "John",
            "last_name": "Doe",
            "created_at": "2023-06-01T12:00:00",
            "updated_at": "2023-06-02T12:00:00"
        }
        self.assertEqual(user_dict, expected_dict)

    @patch('app.models.base_model.datetime')
    def test_created_at_and_updated_at_on_creation(self, mock_datetime):
        mock_datetime.now.return_value = datetime(2023, 6, 1, 12, 0, 0)
        new_user = User(
            email="new@example.com",
            first_name="Jane",
            last_name="Smith"
        )
        self.assertEqual(new_user.created_at, datetime(2023, 6, 1, 12, 0, 0))
        self.assertEqual(new_user.updated_at, datetime(2023, 6, 1, 12, 0, 0))

    @patch('app.models.base_model.datetime')
    def test_updated_at_on_update(self, mock_datetime):
        initial_time = datetime(2023, 6, 1, 12, 0, 0)
        updated_time = datetime(2023, 6, 2, 12, 0, 0)
        mock_datetime.now.return_value = initial_time
        user = User(
            email="test@example.com",
            first_name="John",
            last_name="Doe"
        )
        self.assertEqual(user.updated_at, initial_time)
        mock_datetime.now.return_value = updated_time
        user.first_name = "Updated John"
        self.assertEqual(user.updated_at, updated_time)

if __name__ == '__main__':
    unittest.main()
