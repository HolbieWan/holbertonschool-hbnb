import json
from persistence.ipersistence_manager import IPersistenceManager

class DataManager(IPersistenceManager):
    def __init__(self):
        self.storage = {}

    def save(self, entity):
        entity_type = type(entity).__name__
        if entity_type not in self.storage:
            self.storage[entity_type] = {}
        self.storage[entity_type][entity.id] = entity
        return entity

    def get(self, entity_id, entity_type):
        if entity_type in self.storage and entity_id in self.storage[entity_type]:
            return self.storage[entity_type][entity_id]
        return None

    def update(self, entity):
        entity_type = type(entity).__name__
        if entity_type in self.storage and entity.id in self.storage[entity_type]:
            self.storage[entity_type][entity.id] = entity
            return entity
        return None

    def delete(self, entity_id, entity_type):
        if entity_type in self.storage and entity_id in self.storage[entity_type]:
            del self.storage[entity_type][entity_id]
            return True
        return False

    def save_to_json(self, filename):
        serializable_storage = {}
        for entity_type, entities in self.storage.items():
            entity_dict = {}
            for entity_id, entity in entities.items():
                entity_data = entity.to_dict()
                entity_dict[entity_id] = entity_data
            serializable_storage[entity_type] = entity_dict
        with open(filename, 'w') as file:
            json.dump(serializable_storage, file, indent=4)

    def get_by_email(self, email):
        # Check if email already exists among users
        users = self.storage.get('User', {}).values()
        for user in users:
            if user.email == email:
                return user
        return None


    def place_exists_with_attributes(self, name, address, city_id, host_id, num_rooms, num_bathrooms, price_per_night, max_guests):
        #check if a place already exists with the same attributes
        places = self.storage.get('Place', {}).values()
        for place in places:
            if (place.name == name and
                place.address == address and
                place.city_id == city_id and
                place.host_id == host_id and
                place.num_rooms == num_rooms and
                place.num_bathrooms == num_bathrooms and
                place.price_per_night == price_per_night and
                place.max_guests == max_guests):
                return place
        return False
    
    def review_exists_with_attributes(self, place_id, user_id):
        reviews = self.storage.get('Review', {}).values()
        for review in reviews:
            if review.place_id == place_id and review.user_id == user_id:
                return True
        return False
