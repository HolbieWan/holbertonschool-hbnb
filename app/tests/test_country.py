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

    def test_name_change(self):
        print("Testing name change...")
        new_name = "Australia"
        self.country.name = new_name
        self.assertEqual(self.country.name, new_name)

    def tearDown(self):
        del self.country
