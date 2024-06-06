import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    def test_city_attributes(self):
        city = City("New York", "US")
        self.assertEqual(city.name, "New York")
        self.assertEqual(city.country_id, "US")

    def test_city_inherits_from_base_model(self):
        city = City("Paris", "FR")
        self.assertIsInstance(city, BaseModel)

    def test_city_update_attributes(self):
        city = City("London", "UK")
        city.name = "Manchester"
        city.country_id = "GB"
        self.assertEqual(city.name, "Manchester")
        self.assertEqual(city.country_id, "GB")

    def test_city_name_is_string(self):
        city = City("Berlin", "DE")
        self.assertIsInstance(city.name, str)

    def test_city_country_id_is_string(self):
        city = City("Rome", "IT")
        self.assertIsInstance(city.country_id, str)

    def test_city_name_empty_string(self):
        city = City("", "US")
        self.assertEqual(city.name, "")

    def test_city_country_id_empty_string(self):
        city = City("New York", "")
        self.assertEqual(city.country_id, "")

    def test_city_name_contains_special_characters(self):
        city = City("San Francisco!", "US")
        self.assertEqual(city.name, "San Francisco!")

    def test_city_country_id_contains_special_characters(self):
        city = City("New York", "US!")
        self.assertEqual(city.country_id, "US!")

    def test_city_name_with_whitespace(self):
        city = City("   Los Angeles   ", "US")
        self.assertEqual(city.name, "   Los Angeles   ")

    def test_city_country_id_with_whitespace(self):
        city = City("New York", "   US   ")
        self.assertEqual(city.country_id, "   US   ")


if __name__ == '__main__':
    unittest.main()
