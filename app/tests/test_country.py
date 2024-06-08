import unittest
from models.country import Country
from models.base_model import BaseModel
from datetime import datetime


class TestCountry(unittest.TestCase):
    def test_country_attributes(self):
        country = Country("United States", "US")
        self.assertEqual(country.name, "United States")
        self.assertEqual(country.code, "US")

    def setUp(self):
        self.name = "France"
        self.code = "FR"
        self.country = Country(self.name, self.code)

    def test_init(self):
        print("Testing init method...")
        print(f"Expected name: {self.name}, Actual name: {self.country.name}")
        print(f"Country code: {self.country.code}")
        self.assertEqual(self.country.name, self.name)
        self.assertEqual(self.country.code, self.code)

    def test_set_name(self):
        print("Testing set_name method...")
        new_name = "Australia"
        self.country.set_name(new_name)
        self.assertEqual(self.country.name, new_name)

    def test_set_code(self):
        print("Testing set_code method...")
        new_code = "AU"
        self.country.set_code(new_code)
        self.assertEqual(self.country.code, new_code)

    def get_name(self):
        print("Testing get_name method...")
        self.assertEqual(self.country.get_name(), self.name)

    def get_code(self):
        print("Testing get_code method...")
        self.assertEqual(self.country.get_code(), self.code)

    def test_name_change(self):
        print("Testing name change...")
        new_name = "Australia"
        self.country.name = new_name
        self.assertEqual(self.country.name, new_name)

    def test_code_change(self):
        print("Testing code change...")
        new_code = "AU"
        self.country.code = new_code
        self.assertEqual(self.country.code, new_code)

    def tearDown(self):
        del self.country
