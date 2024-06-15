import unittest
from datetime import datetime, timedelta
from models.country import Country

class TestCountry(unittest.TestCase):

    def setUp(self):
        self.country = Country(name="United States", code="US")

    def test_init(self):
        self.assertIsInstance(self.country, Country)
        self.assertEqual(self.country.name, "United States")
        self.assertEqual(self.country.code, "US")
        self.assertIsNotNone(self.country.id)
        self.assertIsInstance(self.country.created_at, datetime)
        self.assertIsInstance(self.country.updated_at, datetime)

    def test_to_dict(self):
        self.country.id = "country_123"
        self.country.created_at = datetime(2023, 6, 1, 12, 0, 0)
        self.country.updated_at = datetime(2023, 6, 2, 12, 0, 0)

        country_dict = self.country.to_dict()

        expected_dict = {
            "country_id": "country_123",
            "name": "United States",
            "code": "US",
            "created_at": "2023-06-01T12:00:00",
            "updated_at": "2023-06-02T12:00:00"
        }

        self.assertEqual(country_dict, expected_dict)

    def test_created_at_on_creation(self):
        now = datetime.now()
        self.assertLessEqual(now - self.country.created_at, timedelta(seconds=1))

    def test_updated_at_on_update(self):
        initial_time = self.country.updated_at
        self.country.name = "USA"
        self.assertNotEqual(self.country.updated_at, initial_time)

    def test_get_country_code_valid(self):
        valid_country = Country(name="Spain")
        self.assertEqual(valid_country.code, "ES")

    def test_get_country_code_invalid(self):
        with self.assertRaises(ValueError) as context:
            Country(name="InvalidCountryName")
        self.assertEqual(str(context.exception), "Invalid country name!")

    def test_empty_name(self):
        with self.assertRaises(ValueError) as context:
            Country(name="")
        self.assertEqual(str(context.exception), "Name is required!")

    def test_set_empty_name(self):
        with self.assertRaises(ValueError) as context:
            self.country.name = ""
        self.assertEqual(str(context.exception), "Name cannot be empty")

    def test_set_empty_code(self):
        with self.assertRaises(ValueError) as context:
            self.country.code = ""
        self.assertEqual(str(context.exception), "Code cannot be empty")

if __name__ == '__main__':
    unittest.main()
