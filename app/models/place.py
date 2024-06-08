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

    def get_name(self, name):
        return self.name
    
    def set_name(self, name):
        self.name = name

    def get_description(self, description):
        return self.description
    
    def set_description(self, description):
        self.description = description

    def get_address(self, address):
        return self.address
    
    def set_address(self, address):
        self.address = address

    def get_city_id(self, city_id):
        return self.city_id
    
    def set_city_id(self, city_id):
        self.city_id = city_id

    def get_latitude(self, latitude):
        return self.latitude
    
    def set_latitude(self, latitude):
        self.latitude = latitude

    def get_longitude(self, longitude):
        return self.longitude
    
    def set_longitude(self, longitude):
        self.longitude = longitude

    def get_host_id(self, host_id):
        return self.host_id
    
    def set_host_id(self, host_id):
        self.host_id = host_id

    def get_num_rooms(self, num_rooms):
        return self.num_rooms
    
    def set_num_rooms(self, num_rooms):
        self.num_rooms = num_rooms

    def get_num_bathrooms(self, num_bathrooms):
        return self.num_bathrooms
    
    def set_num_bathrooms(self, num_bathrooms):
        self.num_bathrooms = num_bathrooms

    def get_price_per_night(self, price_per_night):
        return self.price_per_night
    
    def set_price_per_night(self, price_per_night):
        self.price_per_night = price_per_night

    def get_max_guests(self, max_guests):
        return self.max_guests
    
    def set_max_guests(self, max_guests):
        self.max_guests = max_guests

    def __str__(self):
        return print(f"Place: {self.name , self.description, self.address, self.city_id, self.latitude, self.longitude, self.host_id, self.num_rooms, self.num_bathrooms, self.price_per_night, self.max_guests}")
    

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