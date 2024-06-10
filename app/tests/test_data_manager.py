import unittest
from app.persistence.data_manager import DataManager
import os
import json


class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def to_dict(self):
        return {'id': self.id, 'name': self.name}


class TestDataManager(unittest.TestCase):

    def setUp(self):
        self.data_manager = DataManager()
        self.user = User(id=1, name="Test User")

    def test_save_user(self):
        saved_user = self.data_manager.save(self.user)
        self.assertEqual(saved_user, self.user)
        self.assertIn('User', self.data_manager.storage)
        self.assertIn(1, self.data_manager.storage['User'])
        self.assertEqual(self.data_manager.storage['User'][1], self.user)

    def test_get_user(self):
        self.data_manager.save(self.user)
        retrieved_user = self.data_manager.get(1, 'User')
        self.assertEqual(retrieved_user, self.user)

    def test_update_user(self):
        self.data_manager.save(self.user)
        self.user.name = "Updated User"
        updated_user = self.data_manager.update(self.user)
        self.assertEqual(updated_user.name, "Updated User")
        self.assertEqual(
            self.data_manager.storage['User'][1].name, "Updated User")

    def test_delete_user(self):
        self.data_manager.save(self.user)
        result = self.data_manager.delete(1, 'User')
        self.assertTrue(result)
        self.assertNotIn(1, self.data_manager.storage['User'])

    def test_save_to_json(self):
        self.data_manager.save(self.user)
        filename = 'test_storage.json'
        self.data_manager.save_to_json(filename)

        with open(filename, 'r') as file:
            data = json.load(file)

        self.assertIn('User', data)
        self.assertIn('1', data['User'])
        self.assertEqual(data['User']['1'], {'id': 1, 'name': "Test User"})

        # Clean up the file after test
        os.remove(filename)


if __name__ == '__main__':
    unittest.main()
