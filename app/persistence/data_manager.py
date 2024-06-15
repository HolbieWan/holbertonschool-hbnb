import json
import os
from persistence.ipersistence_manager import IPersistenceManager

class DataManager(IPersistenceManager):
    def __init__(self, data_file):
        self.storage = {}
        self.data_file = data_file
        self.create_directory_if_not_exists()
        self.load_from_json()

    def create_directory_if_not_exists(self):
        directory = os.path.dirname(self.data_file)
        if not os.path.exists(directory):
            os.makedirs(directory)

    def load_from_json(self):
        try:
            with open(self.data_file, 'r') as file:
                data = json.load(file)
                for entity_type, entities in data.items():
                    self.storage[entity_type] = {}
                    for entity_id, entity_data in entities.items():
                        try:
                            entity = self.dict_to_entity(entity_type, entity_data)
                            self.storage[entity_type][entity_id] = entity
                        except ValueError as e:
                            print(f"Skipping invalid {entity_type}: {e}")
        except FileNotFoundError:
            self.storage = {}

    def dict_to_entity(self, entity_type, entity_data):
        module = __import__('models.' + entity_type.lower(), fromlist=[entity_type])
        entity_class = getattr(module, entity_type)
        return entity_class.from_dict(entity_data, self)

    def save(self, entity):
        entity_type = type(entity).__name__
        if entity_type not in self.storage:
            self.storage[entity_type] = {}
        self.storage[entity_type][entity.id] = entity
        self.save_to_json()
        return entity

    def get(self, entity_id, entity_type):
        if entity_type in self.storage and entity_id in self.storage[entity_type]:
            return self.storage[entity_type][entity_id]
        return None

    def get_by_email(self, email):
        users = self.storage.get('User', {}).values()
        for user in users:
            if user.email == email:
                return user
        return None

    def get_country_by_code(self, country_code):
        countries = self.storage.get('Country', {}).values()
        for country in countries:
            if country.code == country_code:
                return country
        return None

    def place_exists_with_attributes(self, name, address, city_id, host_id, num_rooms, num_bathrooms, price_per_night, max_guests):
        places = self.storage.get('Place', {}).values()
        for place in places:
            if (place._name == name and
                place._address == address and
                place._city_id == city_id and
                place._host_id == host_id and
                place._num_rooms == num_rooms and
                place._num_bathrooms == num_bathrooms and
                place._price_per_night == price_per_night and
                place._max_guests == max_guests):
                return True
        return False

    def review_exists_with_attributes(self, place_id, user_id):
        reviews = self.storage.get('Review', {}).values()
        for review in reviews:
            if review._place_id == place_id and review._user_id == user_id:
                return True
        return False

    def city_exists_with_name_and_country(self, name, country_id):
        cities = self.storage.get('City', {}).values()
        for city in cities:
            if city._name == name and city._country_id == country_id:
                return True
        return False

    def amenity_exists_with_name(self, name):
        amenities = self.storage.get('Amenity', {}).values()
        for amenity in amenities:
            if amenity._name == name:
                return True
        return False

    def get_reviews_by_place_id(self, place_id):
        return [review for review in self.storage.get('Review', {}).values() if review.place_id == place_id]

    def get_reviews_by_user_id(self, user_id):
        return [review for review in self.storage.get('Review', {}).values() if review.user_id == user_id]

    def update(self, entity):
        entity_type = type(entity).__name__
        if entity_type in self.storage and entity.id in self.storage[entity_type]:
            self.storage[entity_type][entity.id] = entity
            self.save_to_json()
            return entity
        return None

    def delete(self, entity_id, entity_type):
        if entity_type in self.storage and entity_id in self.storage[entity_type]:
            del self.storage[entity_type][entity_id]
            self.save_to_json()
            return True
        return False

    def save_to_json(self, file_path=None):
        if not file_path:
            file_path = self.data_file
        serializable_storage = {}
        for entity_type, entities in self.storage.items():
            entity_dict = {}
            for entity_id, entity in entities.items():
                entity_data = entity.to_dict()
                entity_dict[entity_id] = entity_data
            serializable_storage[entity_type] = entity_dict
        with open(file_path, 'w') as file:
            json.dump(serializable_storage, file, indent=4)
