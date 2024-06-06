import json
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models.city import City
from models.country import Country
from .ipersistence_manager import IPersistenceManager


class DataManager(IPersistenceManager):
    def __init__(self, storage_file):
        self.storage_file = storage_file
        self.data = self.load_data()

    def load_data(self):
        try:
            with open(self.storage_file, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

    def save_data(self):
        with open(self.storage_file, 'w') as f:
            json.dump(self.data, f)

    def save(self, entity):
        entity_type = type(entity).__name__.lower()
        if entity_type not in self.data:
            self.data[entity_type] = {}
        self.data[entity_type][entity.id] = entity.__dict__
        self.save_data()

    def get(self, entity_id, entity_type):
        return self.data.get(entity_type, {}).get(entity_id)

    def update(self, entity):
        entity_type = type(entity).__name__.lower()
        if entity_type in self.data and entity.id in self.data[entity_type]:
            self.data[entity_type][entity.id] = entity.__dict__
            self.save_data()

    def delete(self, entity_id, entity_type):
        if entity_type in self.data and entity_id in self.data[entity_type]:
            del self.data[entity_type][entity_id]
            self.save_data()
