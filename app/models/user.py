from .base_model import BaseModel
from .place import Place # House, Apartment, Room


class User(BaseModel):
    def __init__(self, email, first_name, last_name):
        super().__init__()
        self.email = email
        self.first_name = first_name
        self.last_name = last_name

"""
class Owner(User, Place, House, Apartment, Room):
    def __init__(self, email, password, first_name, last_name, places, reviews, house, apartment, room):
        super().__init__(email, password, first_name, last_name)
        self.places = places
        self.reviews = reviews
        self.house = house
        self.apartment = apartment
        self.room = room
"""