import unittest
from models.city import City
from .base_model import BaseModel


class TestCity(unittest.TestCase):
    def test_city_attributes(self):
        city = City("New York", "US")
        self.assertEqual(city.name, "New York")
        self.assertEqual(city.country_id, "US")

    def test_city_inherits_from_base_model(self):
        city = City("Paris", "FR")
        self.assertIsInstance(city, BaseModel)


if __name__ == '__main__':
    unittest.main()
