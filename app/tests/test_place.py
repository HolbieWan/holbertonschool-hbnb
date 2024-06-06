import unittest
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    def setUp(self):
        self.name = "Cédric"
        self.description = "A beautiful place to stay in Nantes."
        self.address = "Rue de la Paix"
        self.city_id = "0001"
        self.latitude = 37.773972
        self.longitude = -122.431297
        self.host_id = "0001"
        self.number_rooms = 2
        self.number_bathrooms = 1
        self.price_by_night = 100
        self.max_guests = 10
        self.place = Place(self.name, self.description, self.address, self.city_id, self.latitude, self.longitude, self.host_id, self.number_rooms, self.number_bathrooms, self.price_by_night, self.max_guests)

    def test_user_attributes(self):
        place = Place("Cédric", "A beautiful place to stay in Nantes.", "Rue de la Paix", "0001", 37.773972, -122.431297, "0001", 2, 1, 4, 100, 10)
        self.assertEqual(place.name, "Cédric")
        self.assertEqual(place.description, "A beautiful place to stay in Nantes.")
        self.assertEqual(place.address, "Rue de la Paix")
        self.assertEqual(place.city_id, "0001")
        self.assertEqual(place.latitude, 37.773972)
        self.assertEqual(place.longitude, -122.431297)
        self.assertEqual(place.host_id, "0001")
        self.assertEqual(place.num_rooms, 2)
        self.assertEqual(place.num_bathrooms, 1)
        self.assertEqual(place.max_guests, 4)
        self.assertEqual(place.price_per_night, 100)
        self.assertEqual(place.max_guests, 10)


    def test_init(self):
        print("Testing init method...")
        print(f"Expected name: {self.name}, Actual name: {self.place.name}")
        print(f"Expected description: {self.description}, Actual description: {self.place.description}")
        print(f"Expected address: {self.address}, Actual address: {self.place.address}")
        print(f"Expected city_id: {self.city_id}, Actual city_id: {self.place.city_id}")
        print(f"Expected latitude: {self.latitude}, Actual latitude: {self.place.latitude}")
        print(f"Expected longitude: {self.longitude}, Actual longitude: {self.place.longitude}")
        print(f"Expected host_id: {self.host_id}, Actual host_id: {self.place.host_id}")
        print(f"Expected number_rooms: {self.number_rooms}, Actual number_rooms: {self.place.num_rooms}")
        print(f"Expected number_bathrooms: {self.number_bathrooms}, Actual number_bathrooms: {self.place.num_bathrooms}")
        print(f"Expected max_guest: {self.max_guest}, Actual max_guest: {self.place.max_guests}")
        print(f"Expected price_by_night: {self.price_by_night}, Actual price_by_night: {self.place.price_per_night}")
        print(f"Expected max_guests: {self.max_guests}, Actual max_guests: {self.place.max_guests}")
        self.assertEqual(self.place.name, self.name)
        self.assertEqual(self.place.description, self.description)
        self.assertEqual(self.place.address, self.address)
        self.assertEqual(self.place.city_id, self.city_id)
        self.assertEqual(self.place.latitude, self.latitude)
        self.assertEqual(self.place.longitude, self.longitude)
        self.assertEqual(self.place.host_id, self.host_id)
        self.assertEqual(self.place.num_rooms, self.number_rooms)
        self.assertEqual(self.place.num_bathrooms, self.number_bathrooms)
        self.assertEqual(self.place.max_guests, self.max_guest)
        self.assertEqual(self.place.price_per_night, self.price_by_night)
        self.assertEqual(self.place.max_guests, self.max_guests)
        self.assertIsInstance(self.place, BaseModel)

    def test_data_changes(self):
        print("Testing data change...")
        new_name = "Jean"
        new_description = "A beautiful place to stay in Paris."
        new_address = "Rue de la Liberté"
        new_city_id = "0002"
        new_latitude = 48.8566
        new_longitude = 2.3522
        new_host_id = "0002"
        new_number_rooms = 3
        new_number_bathrooms = 2
        new_max_guest = 6
        new_price_by_night = 200
        new_max_guests = 12
        self.place.name = new_name
        self.place.description = new_description
        self.place.address = new_address
        self.place.city_id = new_city_id
        self.place.latitude = new_latitude
        self.place.longitude = new_longitude
        self.place.host_id = new_host_id
        self.place.num_rooms = new_number_rooms
        self.place.num_bathrooms = new_number_bathrooms
        self.place.max_guests = new_max_guest
        self.place.price_per_night = new_price_by_night
        self.place.max_guests = new_max_guests
        self.assertEqual(self.place.name, new_name)
        self.assertEqual(self.place.description, new_description)
        self.assertEqual(self.place.address, new_address)
        self.assertEqual(self.place.city_id, new_city_id)
        self.assertEqual(self.place.latitude, new_latitude)
        self.assertEqual(self.place.longitude, new_longitude)
        self.assertEqual(self.place.host_id, new_host_id)
        self.assertEqual(self.place.num_rooms, new_number_rooms)
        self.assertEqual(self.place.num_bathrooms, new_number_bathrooms)
        self.assertEqual(self.place.max_guests, new_max_guest)
        self.assertEqual(self.place.price_per_night, new_price_by_night)
        self.assertEqual(self.place.max_guests, new_max_guests)

    def tearDown(self):
        del self.place     