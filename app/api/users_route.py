from flask import Blueprint, jsonify, request, abort
from datetime import datetime
from models.user import User
from persistence.data_manager import DataManager

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
    if data_manager.get_by_email(email):
        abort(409, 'Email already exists!')
    try:
        user = User(email, first_name, last_name)
    except ValueError as e:
        abort(400, str(e))
    data_manager.save(user)
    data_manager.save_to_json(DATA_FILE)
    return jsonify(user.to_dict()), 201


@users_bp.route('/users', methods=['GET'])
def get_users():
    users = [user.to_dict() for user in data_manager.storage.get('User', {}).values()]
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
    new_email = request.json.get('email', user.email)
    new_first_name = request.json.get('first_name', user.first_name)
    new_last_name = request.json.get('last_name', user.last_name)
    if new_email != user.email and data_manager.get_by_email(new_email):
        abort(409, 'Email already exists')
    try:
        if 'email' in request.json and not User.is_valid_email_format(new_email):
            abort(400, 'Invalid email format!')
        if 'first_name' in request.json and not new_first_name:
            abort(400, 'First name is required!')
        if 'last_name' in request.json and not new_last_name:
            abort(400, 'Last name is required!')
        user.email = new_email
        user.first_name = new_first_name
        user.last_name = new_last_name
        user.updated_at = datetime.utcnow()
    except ValueError as e:
        abort(400, str(e))
    data_manager.update(user)
    data_manager.save_to_json(DATA_FILE)
    return jsonify(user.to_dict()), 200


@users_bp.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    if not data_manager.delete(user_id, 'User'):
        abort(404, 'User not found')
    data_manager.save_to_json(DATA_FILE)
    return '', 204
