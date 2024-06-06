from .base_model import BaseModel

# @abstact_class


class Place(BaseModel):
    def __init__(self, name, description, address, city_id, latitude, longitude, host_id, num_rooms, num_bathrooms, price_per_night, max_guests):
        super().__init__()
        self.name = name
        self.description = description
        self.address = address
        self.city_id = city_id
        self.latitude = latitude
        self.longitude = longitude
        self.host_id = host_id
        self.num_rooms = num_rooms
        self.num_bathrooms = num_bathrooms
        self.price_per_night = price_per_night
        self.max_guests = max_guests

"""
class House(Place):
    def __init__(self, name, description, address, city_id, latitude, longitude, host_id, nb_rooms, nb_bathrooms, price_per_night, max_guests, amenities, reviews, house_rules):
        super().__init__(name, description, address, city_id, latitude, longitude,
                         host_id, nb_rooms, nb_bathrooms, price_per_night, max_guests, amenities, reviews)
        self.amenities = amenities
        self.reviews = reviews
        self.house_rules = house_rules


class Apartment(Place):
    def __init__(self, name, description, address, city_id, latitude, longitude, host_id, nb_rooms, nb_bathrooms, price_per_night, max_guests, amenities, reviews, apartment_rules):
        super().__init__(name, description, address, city_id, latitude, longitude,
                         host_id, nb_rooms, nb_bathrooms, price_per_night, max_guests, amenities, reviews)
        self.amenities = amenities
        self.reviews = reviews
        self.apartment_rules = apartment_rules


class Room(Place):
    def __init__(self, name, description, address, city_id, latitude, longitude, host, nb_rooms, nb_bathrooms, price_per_night, max_guests, amenities, reviews, room_rules):
        super().__init__(name, description, address, city_id, latitude, longitude,
                         host, nb_rooms, nb_bathrooms, price_per_night, max_guests, amenities, reviews)
        self.amenities = amenities
        self.reviews = reviews
        self.room_rules = room_rules
"""