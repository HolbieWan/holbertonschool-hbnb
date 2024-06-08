import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    def setUp(self):
        self.email = "test@laposte.net"
        self.first_name = "John"
        self.last_name = "Doe"
        self.user = User(self.email, self.first_name, self.last_name)

    def test_user_attributes(self):
        user = User("test@laposte.net", "John", "Doe")
        self.assertEqual(user.email, "test@laposte.net")
        self.assertEqual(user.first_name, "John")
        self.assertEqual(user.last_name, "Doe")

    def test_init(self):
        print("Testing init method...")
        print(f"Expected email: {self.email}, Actual email: {self.user.email}")
        print(
            f"Expected first_name: {self.first_name}, Actual first_name: {self.user.first_name}")
        print(
            f"Expected last_name: {self.last_name}, Actual last_name: {self.user.last_name}")
        self.assertEqual(self.user.email, self.email)
        self.assertEqual(self.user.first_name, self.first_name)
        self.assertEqual(self.user.last_name, self.last_name)
        self.assertIsInstance(self.user, BaseModel)

    def test_data_changes(self):
        print("Testing data change...")
        new_email = "toto@gmail.com"
        new_first_name = "Jane"
        new_last_name = "Smith"
        self.user.email = new_email
        self.user.first_name = new_first_name
        self.user.last_name = new_last_name
        self.assertEqual(self.user.email, new_email)
        self.assertEqual(self.user.first_name, new_first_name)
        self.assertEqual(self.user.last_name, new_last_name)

    def test_get_email(self):
        print("Testing get_email method...")
        print(f"Expected: {self.email}")
        print(f"Actual: {self.user.get_email()}")

    def test_set_email(self):
        print("Testing set_email method...")
        new_email = "new_test@gmail.com"
        self.user.set_email(new_email)
        print(f"Expected: {new_email}")
        print(f"Actual: {self.user.email}")

    def test_get_first_name(self):
        print("Testing get_first_name method...")
        print(f"Expected: {self.first_name}")
        print(f"Actual: {self.user.get_first_name()}")

    def test_set_first_name(self):
        print("Testing set_first_name method...")
        new_first_name = "Jane"
        self.user.set_first_name(new_first_name)
        print(f"Expected: {new_first_name}")
        print(f"Actual: {self.user.first_name}")

    def test_get_last_name(self):
        print("Testing get_last_name method...")
        print(f"Expected: {self.last_name}")
        print(f"Actual: {self.user.get_last_name()}")

    def test_set_last_name(self):
        print("Testing set_last_name method...")
        new_last_name = "Smith"
        self.user.set_last_name(new_last_name)
        print(f"Expected: {new_last_name}")
        print(f"Actual: {self.user.last_name}")

    def test_str(self):
        print("Testing __str__ method...")
        print(f"Expected: User: ('{self.email}', '{self.first_name}', '{self.last_name}')")
        print(f"Actual: {self.user.__str__()}")

    def tearDown(self):
        del self.user
