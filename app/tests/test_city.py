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


if __name__ == '__main__':
    unittest.main()
