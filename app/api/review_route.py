from flask import Blueprint, jsonify, request, abort, current_app
from models.review import Review
from datetime import datetime

review_bp = Blueprint('review', __name__)


@review_bp.route('/places/<place_id>/reviews', methods=['POST'])
def create_review(place_id):
    """
    * This route creates a new review for a place *

    Methods: POST

    Request Body:
    - user_id (str) The user's id
    - rating (int) The review's rating
    - text: (str) The review's text

    Returns:

    - dict: Review data



    """
    data_manager = current_app.config['DATA_MANAGER_REVIEWS']

    if not request.json:
        abort(400, 'No input data provided')

    user_id = request.json.get('user_id')
    rating = request.json.get('rating')
    text = request.json.get('text')

    if not all([user_id, rating, text]):
        abort(400, 'Missing required fields')
    try:
        rating = int(rating)
    except ValueError:
        abort(400, 'Rating must be an integer')
    try:
        review = Review(place_id, user_id, rating, text, data_manager)
    except ValueError as e:
        abort(400, str(e))
    data_manager.save(review)
    return jsonify(review.to_dict()), 201


# ********************************************************************* #


@review_bp.route('/users/<user_id>/reviews', methods=['GET'])
def get_reviews_by_user(user_id):
    """
    * This route gets all reviews by a user *

    Methods: GET

    Returns:

    - list: List of reviews by user


    """

    data_manager = current_app.config['DATA_MANAGER_REVIEWS']
    reviews = data_manager.get_reviews_by_user_id(user_id)
    return jsonify([review.to_dict() for review in reviews]), 200


# ********************************************************************* #


@review_bp.route('/places/<place_id>/reviews', methods=['GET'])
def get_reviews_by_place(place_id):
    """
    * This route gets all reviews by a place *

    Methods: GET

    Returns:

    - list: List of reviews by place


    """
    data_manager = current_app.config['DATA_MANAGER_REVIEWS']
    reviews = data_manager.get_reviews_by_place_id(place_id)
    return jsonify([review.to_dict() for review in reviews]), 200


# ********************************************************************* #


@review_bp.route('/reviews/<review_id>', methods=['GET'])
def get_review(review_id):
    """
    * This route gets a review by ID *

    Methods: GET

    Parameters:
        review_id: (str) The review's ID

    Returns:

    - dict: Review data


    """
    data_manager = current_app.config['DATA_MANAGER_REVIEWS']
    review = data_manager.get(review_id, 'Review')

    if review is None:
        abort(404, 'Review not found')
    return jsonify(review.to_dict()), 200


# ********************************************************************* #

@review_bp.route('/reviews/<review_id>', methods=['PUT'])
def update_review(review_id):
    """
    * This route updates a review *

    Methods: PUT

    Parameters:
        review_id: (str) The review's ID

    Request Body:

    - rating (int) The review's rating
    - text: (str) The review's text

    Returns:

    - dict: Review data


    """

    data_manager = current_app.config['DATA_MANAGER_REVIEWS']
    review = data_manager.get(review_id, 'Review')

    if review is None:
        abort(404, 'Review not found')
    data = request.get_json()

    if not data:
        abort(400, 'No input data provided')
    try:
        for key, value in data.items():
            if key in ['rating', 'text']:
                setattr(review, key, value)
        review.updated_at = datetime.utcnow()
        data_manager.save(review)
    except ValueError as e:
        abort(400, str(e))
    return jsonify(review.to_dict()), 200


# ********************************************************************* #


@review_bp.route('/reviews/<review_id>', methods=['DELETE'])
def delete_review(review_id):
    """
    * This route deletes a review *

    Methods: DELETE

    Parameters:
        review_id: (str) The review's ID

    Returns:

    - str: Empty string

    """

    data_manager = current_app.config['DATA_MANAGER_REVIEWS']
    review = data_manager.get(review_id, 'Review')

    if review is None:
        abort(404, 'Review not found')
    data_manager.delete(review_id, 'Review')
    return '', 204


# ********************************************************************* #

@review_bp.route('/reviews', methods=['GET'])
def get_reviews():
    """
    * This route gets all reviews *

    Methods: GET

    Returns:

    - list: List of reviews

    """

    data_manager = current_app.config['DATA_MANAGER_REVIEWS']
    reviews = [review.to_dict()
               for review in data_manager.storage.get('Review', {}).values()]
    return jsonify(reviews), 200
