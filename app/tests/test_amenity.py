import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    def setUp(self):
        self.name = "Swimming Pool"
        self.amenity = Amenity(self.name)

    def tearDown(self):
        del self.amenity

    def test_init(self):
        print("Testing init method...")
        print(f"Expected name: {self.name}, Actual name: {self.amenity.name}")
        print(f"Amenity ID: {self.amenity.id}")
        print(f"Created at: {self.amenity.created_at}")
        print(f"Updated at: {self.amenity.updated_at}")

        self.assertEqual(self.amenity.name, self.name)
        self.assertIsInstance(self.amenity, Amenity)
        self.assertIsNotNone(self.amenity.id)
        self.assertIsNotNone(self.amenity.created_at)
        self.assertIsNotNone(self.amenity.updated_at)


if __name__ == '__main__':
    unittest.main()
