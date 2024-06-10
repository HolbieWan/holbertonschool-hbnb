import json
from app.persistence.ipersistence_manager import IPersistenceManager

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
