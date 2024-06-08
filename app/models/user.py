from .base_model import BaseModel


class User(BaseModel):
    def __init__(self, email, first_name, last_name):
        super().__init__()
        self.email = email
        self.first_name = first_name
        self.last_name = last_name

    def get_email(self):
        return self.email
    
    def set_email(self, email):
        self.email = email

    def get_first_name(self):
        return self.first_name
    
    def set_first_name(self, first_name):
        self.first_name = first_name

    def get_last_name(self):
        return self.last_name
    
    def set_last_name(self, last_name):
        self.last_name = last_name

    def __str__(self):
        return print(f"User: {self.email, self.first_name, self.last_name}")
    

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