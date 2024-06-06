import unittest
from models.user import User
from models.base_model import BaseModel

class TestUser(unittest.TestCase):
    def setUp(self):
        self.email = "test@laposte.net"
        self.first_name = "John"
        self.last_name = "Doe"
        self.user = User(self.email, self.first_name, self.last_name)
        
    def test_country_attributes(self):
        user = User("test@laposte.net", "John", "Doe")
        self.assertEqual(user.email, "test@laposte.net")
        self.assertEqual(user.first_name, "John")
        self.assertEqual(user.last_name, "Doe")
        
    def test_init(self):
        print("Testing init method...")
        print(f"Expected email: {self.email}, Actual email: {self.user.email}")
        print(f"Expected first_name: {self.first_name}, Actual first_name: {self.user.first_name}")
        print(f"Expected last_name: {self.last_name}, Actual last_name: {self.user.last_name}")
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

    def tearDown(self):
        del self.user