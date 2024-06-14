from models.base_model import BaseModel
from datetime import datetime

class Place(BaseModel):
    def __init__(self, name, description, address, city_id, latitude, longitude, host_id, num_rooms, num_bathrooms, price_per_night, max_guests, amenities=None, data_manager=None):
        super().__init__()
        if not all([name, description, address, city_id, latitude, longitude, host_id, num_rooms, num_bathrooms, price_per_night, max_guests]):
            raise ValueError("All fields are required!")
        if not -90 <= latitude <= 90:
            raise ValueError("Latitude must be between -90 and 90 degrees")
        if not -180 <= longitude <= 180:
            raise ValueError("Longitude must be between -180 and 180 degrees")
        if not 0 <= num_rooms <= 100:
            raise ValueError("Number of rooms must be a positive integer between 0 and 100")
        if not 0 <= num_bathrooms <= 100:
            raise ValueError("Number of bathrooms must be a positive integer between 0 and 100")
        if not 0 <= price_per_night <= 10000:
            raise ValueError("Price per night must be a positive value between 0 and 10000")
        if not 1 <= max_guests <= 100:
            raise ValueError("Max guests must be a positive integer between 1 and 100")
        if data_manager and data_manager.place_exists_with_attributes(name, address, city_id, host_id, num_rooms, num_bathrooms, price_per_night, max_guests):
            raise ValueError("Place already exists!")

        self._name = name
        self._description = description
        self._address = address
        self._city_id = city_id
        self._latitude = latitude
        self._longitude = longitude
        self._host_id = host_id
        self._num_rooms = num_rooms
        self._num_bathrooms = num_bathrooms
        self._price_per_night = price_per_night
        self._max_guests = max_guests
        self._amenities = amenities or []
        self.data_manager = data_manager

    @staticmethod
    def from_dict(data, data_manager):
        place = Place(
            name=data['place_name'],
            description=data['description'],
            address=data['address'],
            city_id=data['city_id'],
            latitude=data['latitude'],
            longitude=data['longitude'],
            host_id=data['host_id'],
            num_rooms=data['num_rooms'],
            num_bathrooms=data['num_bathrooms'],
            price_per_night=data['price_per_night'],
            max_guests=data['max_guests'],
            amenities=data.get('amenities', []),
            data_manager=data_manager
        )
        place.id = data['place_id']
        place.created_at = datetime.fromisoformat(data['created_at'])
        place.updated_at = datetime.fromisoformat(data['updated_at'])
        return place

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
        self.save()

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value
        self.save()

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
        self.save()

    @property
    def city_id(self):
        return self._city_id

    @city_id.setter
    def city_id(self, value):
        self._city_id = value
        self.save()

    @property
    def latitude(self):
        return self._latitude

    @latitude.setter
    def latitude(self, value):
        if not -90 <= value <= 90:
            raise ValueError("Latitude must be between -90 and 90 degrees")
        self._latitude = value
        self.save()

    @property
    def longitude(self):
        return self._longitude

    @longitude.setter
    def longitude(self, value):
        if not -180 <= value <= 180:
            raise ValueError("Longitude must be between -180 and 180 degrees")
        self._longitude = value
        self.save()

    @property
    def host_id(self):
        return self._host_id

    @host_id.setter
    def host_id(self, value):
        self._host_id = value
        self.save()

    @property
    def num_rooms(self):
        return self._num_rooms

    @num_rooms.setter
    def num_rooms(self, value):
        if value < 0 or value > 100:
            raise ValueError("Number of rooms must be a positive integer between 0 and 100")
        self._num_rooms = value
        self.save()

    @property
    def num_bathrooms(self):
        return self._num_bathrooms

    @num_bathrooms.setter
    def num_bathrooms(self, value):
        if value < 0 or value > 100:
            raise ValueError("Number of bathrooms must be a positive integer between 0 and 100")
        self._num_bathrooms = value
        self.save()

    @property
    def price_per_night(self):
        return self._price_per_night

    @price_per_night.setter
    def price_per_night(self, value):
        if value < 0 or value > 10000:
            raise ValueError("Price per night must be a positive integer between 0 and 10000")
        self._price_per_night = value
        self.save()

    @property
    def max_guests(self):
        return self._max_guests

    @max_guests.setter
    def max_guests(self, value):
        if value <= 0 or value > 100:
            raise ValueError("Max guests must be a positive integer between 1 and 100")
        self._max_guests = value
        self.save()

    @property
    def amenities(self):
        return self._amenities

    @amenities.setter
    def amenities(self, value):
        self._amenities = value
        self.save()

    def add_amenity(self, amenity_id):
        if amenity_id not in self._amenities:
            self._amenities.append(amenity_id)
            self.save()

    def remove_amenity(self, amenity_id):
        if amenity_id in self._amenities:
            self._amenities.remove(amenity_id)
            self.save()

    def to_dict(self):
        return {
            "place_id": self.id,
            "place_name": self._name,
            "description": self._description,
            "address": self._address,
            "city_id": self._city_id,
            "latitude": self._latitude,
            "longitude": self._longitude,
            "host_id": self._host_id,
            "num_rooms": self._num_rooms,
            "num_bathrooms": self._num_bathrooms,
            "price_per_night": self._price_per_night,
            "max_guests": self._max_guests,
            "amenities": self._amenities,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }
