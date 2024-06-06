import unittest
from models.amenity import Amenity
from datetime import datetime


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
        self.assertIsNotNone(self.amenity.id)
        self.assertIsNotNone(self.amenity.created_at)
        self.assertIsNotNone(self.amenity.updated_at)

    def test_name_change(self):
        print("Testing name change...")
        new_name = "Gym"
        self.amenity.name = new_name
        self.assertEqual(self.amenity.name, new_name)

    def test_created_at_change(self):
        print("Testing created_at change...")
        new_created_at = datetime.now()
        self.amenity.created_at = new_created_at
        self.assertEqual(self.amenity.created_at, new_created_at)

    def test_updated_at_change(self):
        print("Testing updated_at change...")
        new_updated_at = datetime.now()
        self.amenity.updated_at = new_updated_at
        self.assertEqual(self.amenity.updated_at, new_updated_at)


if __name__ == '__main__':
    unittest.main()
