from flask import Blueprint, jsonify, request, abort
from models.review import Review
from persistence.data_manager import DataManager
from datetime import datetime
data_manager = DataManager()

review_bp = Blueprint('review', __name__)


DATA_FILE = "data_review.json"  # Define the data file


@review_bp.route('/reviews', methods=['POST'])
def create_review():

    data = request.get_json()
    if not data:
        abort(400, 'No review provided')
    place_id = data.get('place_id')
    user_id = data.get('user_id')
    rating = data.get('rating')
    text = data.get('text')
    if not all([place_id, user_id, rating, text]):
        abort(400, 'Missing required fields')
    review = Review(place_id, user_id, rating, text)
    data_manager.save(review)
    data_manager.save_to_json(DATA_FILE)  # Save to JSON file
    return jsonify(review.to_dict()), 201


@review_bp.route('/reviews', methods=['GET'])
def get_reviews():

    review_objects = data_manager.storage.get('Review', {}).values()
    reviews = [review.to_dict() for review in review_objects]
    return jsonify(reviews), 200


@review_bp.route('/reviews/<review_id>', methods=['GET'])
def get_review(review_id):

    review = data_manager.get(review_id, 'Review')
    if review is None:
        abort(404, 'Review not found')
    return jsonify(review.to_dict()), 200


@review_bp.route('/reviews/<review_id>', methods=['PUT'])
def update_review(review_id):

    review = data_manager.get(review_id, 'Review')
    if review is None:
        abort(404, 'Review not found')
    data = request.get_json()
    if not data:
        abort(400, 'No input data provided')
    for key, value in data.items():
        if hasattr(review, key):
            setattr(review, key, value)
    review.updated_at = datetime.utcnow()
    data_manager.save(review)
    data_manager.save_to_json(DATA_FILE)  # Save to JSON file
    return jsonify(review.to_dict()), 200


@review_bp.route('/reviews/<review_id>', methods=['DELETE'])
def delete_review(review_id):

    review = data_manager.get(review_id, 'Review')
    if review is None:
        abort(404, 'Review not found')
    data_manager.delete(review_id, 'Review')
    data_manager.save_to_json(DATA_FILE)  # Save to JSON file
    return jsonify({}), 204
