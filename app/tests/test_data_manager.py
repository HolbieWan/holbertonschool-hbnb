import unittest
import json
import os
from persistence.data_manager import DataManager

class Entity:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class TestDataManager(unittest.TestCase):

    def setUp(self):
        self.storage_file = "test.json"
        self.data_manager = DataManager(self.storage_file)
        self.data_manager.data = {}  # Ensure data is empty before each test

    def tearDown(self):
        try:
            os.remove(self.storage_file)
        except FileNotFoundError:
            pass

    def test_load_data_existing_file(self):
        initial_data = {"entity": {"1": {"id": "1", "name": "John Doe"}}}
        with open(self.storage_file, 'w') as f:
            json.dump(initial_data, f)
        data_manager = DataManager(self.storage_file)
        self.assertEqual(data_manager.data, initial_data)

    def test_load_data_file_not_found(self):
        data_manager = DataManager(self.storage_file)
        self.assertEqual(data_manager.data, {})

    def test_save_data(self):
        self.data_manager.data = {"entity": {"1": {"id": "1", "name": "John Doe"}}}
        self.data_manager.save_data()
        with open(self.storage_file, 'r') as f:
            data = json.load(f)
            self.assertEqual(data, self.data_manager.data)

    def test_save(self):
        entity = Entity(id='1', name='John Doe')
        self.data_manager.save(entity)
        print(f"Saved Data: {self.data_manager.data}")
        expected_data = {'entity': {"1": {'id': "1", 'name': 'John Doe'}}}
        print(f"Expected Data: {expected_data}")
        self.assertEqual(self.data_manager.data, expected_data)
        print(f"Ok")
        with open(self.storage_file, 'r') as f:
            data = json.load(f)
            self.assertEqual(data, expected_data)
            print(f"Data: {data}")
            print(f"Expected Data: {expected_data}")

    def test_get_existing_entity(self):
        self.data_manager.data = {'entity': {"1": {'id': "1", 'name': 'John Doe'}}}
        result = self.data_manager.get("1", 'entity')
        self.assertEqual(result, {'id': '1', 'name': 'John Doe'})

    def test_get_non_existing_entity(self):
        self.data_manager.data = {'entity': {}}
        result = self.data_manager.get(1, 'entity')
        self.assertIsNone(result)

    def test_get_all_entities(self):
        self.data_manager.data = {
            'entity': {
                '1': {'id': '1', 'name': 'John Doe'},
                '2': {'id': '2', 'name': 'Jane Doe'}
            }
        }
        result = list(self.data_manager.get_all('entity'))
        expected_result = [
            {'id': '1', 'name': 'John Doe'},
            {'id': '2', 'name': 'Jane Doe'}
        ]
        self.assertEqual(result, expected_result)

    def test_update_existing_entity(self):
        self.data_manager.data = {'entity': {'1': {'id': '1', 'name': 'Old Name'}}}
        updated_entity = Entity('1', 'New Name')
        self.data_manager.update(updated_entity)
        expected_data = {'entity': {'1': {'id': '1', 'name': 'New Name'}}}
        self.assertEqual(self.data_manager.data, expected_data)
        self.data_manager.save_data()
        with open(self.storage_file, 'r') as f:
            data = json.load(f)
            self.assertEqual(data, expected_data)
            print(f"Data: {data}")
            print(f"Expected Data: {expected_data}")

    def test_update_non_existing_entity(self):
        self.data_manager.data = {'entity': {}}
        new_entity = Entity('1', 'New Name')

    def test_delete_existing_entity(self):
        self.data_manager.data = {'entity': {'1': {'id': '1', 'name': 'John Doe'}}}
        self.data_manager.delete('entity', '1')
        self.assertEqual(self.data_manager.data, {'entity': {}})
        self.data_manager.save_data()
        with open(self.storage_file, 'r') as f:
            data = json.load(f)
            self.assertEqual(data, {'entity': {}})

    def test_delete_non_existing_entity(self):
        self.data_manager.data = {'entity': {}}
        self.data_manager.delete('entity', '1')
        self.assertEqual(self.data_manager.data, {'entity': {}})

if __name__ == '__main__':
    unittest.main()
