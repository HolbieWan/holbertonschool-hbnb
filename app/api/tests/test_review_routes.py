import unittest
import json
from app import app
from persistence.data_manager import DataManager
from models.review import Review
import os

class TestReviewAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        self.data_manager = DataManager('data/test_data_reviews.json')
        self.data_manager.storage = {}
        app.config['DATA_MANAGER_REVIEWS'] = self.data_manager

    def tearDown(self):
        if os.path.exists('data/test_data_reviews.json'):
            os.remove('data/test_data_reviews.json')

    def test_create_review(self):
        response = self.app.post('/places/1/reviews', json={
            'user_id': 'user_1',
            'rating': 5,
            'text': 'Great place!'
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn('review_id', json.loads(response.data))

    def test_get_reviews_by_user(self):
        self.app.post('/places/1/reviews', json={
            'user_id': 'user_1',
            'rating': 5,
            'text': 'Great place!'
        })
        response = self.app.get('/users/user_1/reviews')
        self.assertEqual(response.status_code, 200)
        reviews = json.loads(response.data)
        self.assertEqual(len(reviews), 1)

    def test_get_reviews_by_place(self):
        self.app.post('/places/1/reviews', json={
            'user_id': 'user_1',
            'rating': 5,
            'text': 'Great place!'
        })
        response = self.app.get('/places/1/reviews')
        self.assertEqual(response.status_code, 200)
        reviews = json.loads(response.data)
        self.assertEqual(len(reviews), 1)

    def test_get_review(self):
        response = self.app.post('/places/1/reviews', json={
            'user_id': 'user_1',
            'rating': 5,
            'text': 'Great place!'
        })
        review_id = json.loads(response.data)['review_id']
        response = self.app.get(f'/reviews/{review_id}')
        self.assertEqual(response.status_code, 200)
        review = json.loads(response.data)
        self.assertEqual(review['text'], 'Great place!')

    def test_update_review(self):
        response = self.app.post('/places/1/reviews', json={
            'user_id': 'user_1',
            'rating': 5,
            'text': 'Great place!'
        })
        review_id = json.loads(response.data)['review_id']
        response = self.app.put(f'/reviews/{review_id}', json={
            'rating': 4,
            'text': 'Good place!'
        })
        self.assertEqual(response.status_code, 200)
        review = json.loads(response.data)
        self.assertEqual(review['rating'], 4)
        self.assertEqual(review['text'], 'Good place!')

    def test_delete_review(self):
        response = self.app.post('/places/1/reviews', json={
            'user_id': 'user_1',
            'rating': 5,
            'text': 'Great place!'
        })
        review_id = json.loads(response.data)['review_id']
        response = self.app.delete(f'/reviews/{review_id}')
        self.assertEqual(response.status_code, 204)
        response = self.app.get(f'/reviews/{review_id}')
        self.assertEqual(response.status_code, 404)

    def test_get_all_reviews(self):
        self.app.post('/places/1/reviews', json={
            'user_id': 'user_1',
            'rating': 5,
            'text': 'Great place!'
        })
        response = self.app.get('/reviews')
        self.assertEqual(response.status_code, 200)
        reviews = json.loads(response.data)
        self.assertEqual(len(reviews), 1)

if __name__ == '__main__':
    unittest.main()
