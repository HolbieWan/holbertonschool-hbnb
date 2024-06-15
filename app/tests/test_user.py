import unittest
from datetime import datetime
from unittest.mock import patch, MagicMock
from models.user import User
from models.base_model import BaseModel

class TestUser(unittest.TestCase):

    def setUp(self):
        self.mock_data_manager = MagicMock()
        self.mock_data_manager.get_by_email.return_value = None  # Ensure no email exists
        self.user = User(
            email="test@gmail.com",
            first_name="John",
            last_name="Doe",
            data_manager=self.mock_data_manager
        )

    def test_init(self):
        self.assertIsInstance(self.user, BaseModel)
        self.assertEqual(self.user.email, "test@gmail.com")
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
            "user_id": "user_123",
            "email": "test@gmail.com",
            "first_name": "John",
            "last_name": "Doe",
            "created_at": "2023-06-01T12:00:00",
            "updated_at": "2023-06-02T12:00:00"
        }
        self.assertEqual(user_dict, expected_dict)

    @patch('models.base_model.datetime')
    def test_created_at_and_updated_at_on_creation(self, mock_datetime):
        mock_datetime.now.return_value = datetime(2023, 6, 1, 12, 0, 0)
        new_user = User(
            email="new@gmail.com",
            first_name="Jane",
            last_name="Smith",
            data_manager=self.mock_data_manager
        )
        self.assertEqual(new_user.created_at, datetime(2023, 6, 1, 12, 0, 0))
        self.assertEqual(new_user.updated_at, datetime(2023, 6, 1, 12, 0, 0))

    @patch('models.base_model.datetime')
    def test_updated_at_on_update(self, mock_datetime):
        initial_time = datetime(2023, 6, 1, 12, 0, 0)
        updated_time = datetime(2023, 6, 2, 12, 0, 0)
        mock_datetime.now.return_value = initial_time
        user = User(
            email="test@gmail.com",
            first_name="John",
            last_name="Doe",
            data_manager=self.mock_data_manager
        )
        self.assertEqual(user.updated_at, initial_time)
        mock_datetime.now.return_value = updated_time
        user.first_name = "Updated John"
        self.assertEqual(user.updated_at, updated_time)

    def test_invalid_email_format(self):
        invalid_email = "invalid-email"
        with self.assertRaises(ValueError) as context:
            User(email=invalid_email, first_name="John", last_name="Doe", data_manager=self.mock_data_manager)
        self.assertEqual(str(context.exception), "Invalid email format!")

    def test_missing_fields(self):
        with self.assertRaises(ValueError) as context:
            User(email="", first_name="John", last_name="Doe", data_manager=self.mock_data_manager)
        self.assertEqual(str(context.exception), "Email is required!")
        with self.assertRaises(ValueError) as context:
            User(email="test@gmail.com", first_name="", last_name="Doe", data_manager=self.mock_data_manager)
        self.assertEqual(str(context.exception), "First name is required!")
        with self.assertRaises(ValueError) as context:
            User(email="test@gmail.com", first_name="John", last_name="", data_manager=self.mock_data_manager)
        self.assertEqual(str(context.exception), "Last name is required!")

    def test_duplicate_email(self):
        self.mock_data_manager.get_by_email.return_value = True
        with self.assertRaises(ValueError) as context:
            User(email="test@gmail.com", first_name="John", last_name="Doe", data_manager=self.mock_data_manager)
        self.assertEqual(str(context.exception), "Email already exists!")

if __name__ == '__main__':
    unittest.main()
