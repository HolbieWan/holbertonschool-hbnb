from flask import Blueprint, jsonify, request, abort
from models.user import User
from persistence.data_manager import DataManager
from datetime import datetime
data_manager = DataManager()


users_bp = Blueprint('users', __name__)

DATA_FILE = "data_users.json"


@users_bp.route('/')
def index():
    return "Hello, World!"


@users_bp.route('/users', methods=['POST'])
def create_user():

    if not request.json or not 'email' in request.json:
        abort(400, 'Email is required')
    email = request.json['email']
    first_name = request.json.get('first_name', "")
    last_name = request.json.get('last_name', "")
    # Check for unique email
    for user in data_manager.storage.get('User', {}).values():
        if user.email == email:
            abort(409, 'Email already exists')
    user = User(email, first_name, last_name)
    data_manager.save(user)
    data_manager.save_to_json(DATA_FILE)
    return jsonify(user.to_dict()), 201


@users_bp.route('/users', methods=['GET'])
def get_users():

    users = [user.to_dict()
             for user in data_manager.storage.get('User', {}).values()]
    return jsonify(users), 200


@users_bp.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):

    user = data_manager.get(user_id, 'User')
    if user is None:
        abort(404, 'User not found')
    return jsonify(user.to_dict()), 200


@users_bp.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):

    user = data_manager.get(user_id, 'User')
    if user is None:
        abort(404, 'User not found')
    if not request.json:
        abort(400, 'Invalid data')
    user.email = request.json.get('email', user.email)
    user.first_name = request.json.get('first_name', user.first_name)
    user.last_name = request.json.get('last_name', user.last_name)
    user.updated_at = datetime.utcnow()
    data_manager.update(user)
    data_manager.save_to_json(DATA_FILE)
    return jsonify(user.to_dict()), 200


@users_bp.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):

    if not data_manager.delete(user_id, 'User'):
        abort(404, 'User not found')
    data_manager.save_to_json(DATA_FILE)
    return '', 204
