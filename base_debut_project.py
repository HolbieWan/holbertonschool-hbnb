class Places:
    def __init__(self, name, description, address, city, latitude, longitude, host, nb_rooms, bathrooms, price_night, max_guests, amenities, reviews):
        self.name = name
        self.description = description
        self.address = address
        self.city = city
        self.latitude = latitude
        self.longitude = longitude
        self.host = host
        self.nb_rooms = nb_rooms
        self.bathrooms = bathrooms
        self.price_night = price_night
        self.max_guests = max_guests
        self.amenities = amenities
        self.reviews = reviews


class Users:
    def __init__(self, email, password, first_name, last_name):
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.places = []
        self.reviews = []


class Reviews:
    def __init__(self, place_id, user_id, text):
        self.place_id = place_id
        self.user_id = user_id
        self.text = text


class Amenities:
    def __init__(self, wifi, kitchen, ac, tv, parking, washing_machine, dryer, heating, elevator, dishwasher):
        self.wifi = wifi
        self.kitchen = kitchen
        self.ac = ac
        self.tv = tv
        self.parking = parking
        self.washing_machine = washing_machine
        self.dryer = dryer
        self.heating = heating
        self.elevator = elevator
        self.dishwasher = dishwasher


class Country:
    def __init__(self, name, code):
        self.name = name
        self.code = code


class City(Country):
    def __init__(self, name, code, country, places):
        super().__init__(name, code)
        self.country = country
        self.places = places


class House(Places):
    def __init__(self, name, description, address, city, latitude, longitude, host, nb_rooms, bathrooms, price_night, max_guests, amenities, reviews, house_rules):
        super().__init__(name, description, address, city, latitude, longitude,
                         host, nb_rooms, bathrooms, price_night, max_guests, amenities, reviews)
        self.house_rules = house_rules


class Apartment(Places):
    def __init__(self, name, description, address, city, latitude, longitude, host, nb_rooms, bathrooms, price_night, max_guests, amenities, reviews, apartment_rules):
        super().__init__(name, description, address, city, latitude, longitude,
                         host, nb_rooms, bathrooms, price_night, max_guests, amenities, reviews)
        self.apartment_rules = apartment_rules


class Room(Places):
    def __init__(self, name, description, address, city, latitude, longitude, host, nb_rooms, bathrooms, price_night, max_guests, amenities, reviews, room_rules):
        super().__init__(name, description, address, city, latitude, longitude,
                         host, nb_rooms, bathrooms, price_night, max_guests, amenities, reviews)
        self.room_rules = room_rules


class Owner(Users, Places):
    def __init__(self, email, password, first_name, last_name, places, reviews):
        super().__init__(email, password, first_name, last_name)
        self.places = places
        self.reviews = reviews


class Reviewers(Users, Places):
    def __init__(self, email, password, first_name, last_name, places, reviews):
        super().__init__(email, password, first_name, last_name)
        self.places = places
        self.reviews = reviews
