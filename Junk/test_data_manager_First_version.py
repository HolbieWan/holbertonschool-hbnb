import unittest
import json
from persistence.data_manager import DataManager

class TestDataManager(unittest.TestCase):
    
    def setUp(self):
        self.storage_file = "test.json"
        self.data_manager = DataManager(self.storage_file)

    def test_save(self):
        class Entity:
            def __init__(self, id, name):
                self.id = id
                self.name = name
        entity = Entity(id='1', name='John Doe')
        self.data_manager.save(entity)
        self.data_manager.load_data()
        saved_entity = self.data_manager.get('1', 'entity')
        expected_entity = {'id': '1', 'name': 'John Doe'}
        print(f"Expected entity: {expected_entity}, Actual entity: {saved_entity}")
        self.assertEqual(saved_entity, expected_entity)

    def test_save_data(self):
        print("Testing save_data method...")
        self.data_manager.data = {"User": {"123": {"email": "test@gmail.com", "first_name": "John", "last_name": "Doe"}}}
        self.data_manager.save_data()
        with open(self.storage_file, 'r') as f:
            data = json.load(f)
            self.assertEqual(data, self.data_manager.data)
            print(f"Expected data: {self.data_manager.data}, Actual data: {data}")
        
    def test_init(self):
        storage_file = "storage.json"
        data_manager = DataManager(storage_file)
        self.assertEqual(data_manager.storage_file, storage_file)

    def test_load_data_with_existing_file(self):
        # Write initial data to storage file
        initial_data = {'test': {'1234': {'name': 'Test Entity'}}}
        with open(self.storage_file, 'w') as f:
            json.dump(initial_data, f)
        # Load data using DataManager
        loaded_data = self.data_manager.load_data()
        self.assertEqual(loaded_data, initial_data)
    
    def test_get(self):
        print("Testing get method...")
        self.data_manager.data = {"User": {"123": {"email": ")@gmail.com", "first_name": "John", "last_name": "Doe"}}}
        self.assertEqual(self.data_manager.get("123", "User"), {"email": ")@gmail.com", "first_name": "John", "last_name": "Doe"})

    def test_update_existing_entity(self):
        class Entity:
            def __init__(self, id, name):
                self.id = id
                self.name = name
        entity = Entity(id=1234, name='John Doe')

        # Initial data with an entity
        initial_data = {'testentity': {'1234': {'id': '1234', 'name': 'Old Name'}}}
        print(f"Initial data: {initial_data}")
        self.data_manager.data = initial_data
        print(f"Data manager data: {self.data_manager.data}")
        # Create an updated entity
        updated_entity = Entity('1234', 'New Name')
        # Update the entity
        updated_data = self.data_manager.update(updated_entity)
        print(f"Updated data: {updated_data}")
        # Verify the data is updated
        expected_data = {'testentity': {'1234': {'id': '1234', 'name': 'New Name'}}}
        print(f"Expected data: {expected_data}")
        self.assertEqual(self.data_manager.data, expected_data)
       
    
    def test_delete(self):
        print("Testing delete method...")
        self.data_manager.data = {"User": {"123": {"email": "@gmail.com", "first_name": "John", "last_name": "Doe"}}}
        self.data_manager.delete("User", "123")
        self.assertEqual(self.data_manager.data, {'User': {}})
