from flask import Blueprint, jsonify, request, abort, current_app
from datetime import datetime
from models.user import User

users_bp = Blueprint('users', __name__)


@users_bp.route('/')
def home():
    """
    * This is the home route *

    Returns:

    - str: Welcoming message

    """
    return "Welcome to our HBTN custom API!"


# ********************************************************************* #


@users_bp.route('/users', methods=['POST'])
def create_user():
    """
    * This route creates a new user *

    Methods: POST

    Request Body:
    - email (str) The user's email
    - first_name (str) The user's first name
    - last_name: (str) The user's last name

    Returns:

    - dict: User data

    """

    data_manager = current_app.config['DATA_MANAGER_USERS']
    data = request.json

    if not data or 'email' not in data:
        abort(400, 'Email is required')

    email = data.get('email')
    first_name = data.get('first_name')
    last_name = data.get('last_name')

    # Check if email is valid
    if not User.is_valid_email_format(email):
        abort(400, 'Invalid email format!')

    # Check if fields are strings
    if not isinstance(email, str) or not isinstance(first_name, str) \
            or not isinstance(last_name, str):
        abort(400, 'Fields must be of string type')

    # Check if fields are not empty
    if not email.strip() or not first_name.strip() or not last_name.strip():
        abort(400, 'Fields cannot be empty')

    # Check if email already exists
    if data_manager.get_by_email(email):
        abort(409, 'Email already exists!')

    try:
        user = User(email, first_name, last_name, data_manager)
    except ValueError as e:
        abort(400, str(e))

    data_manager.save(user)

    return jsonify(user.to_dict()), 201


# ********************************************************************* #


@users_bp.route('/users', methods=['GET'])
def get_users():
    """
    * This route gets all users *

    Methods: GET

    Returns:

    - list: List of users

    """
    data_manager = current_app.config['DATA_MANAGER_USERS']

    users = [user.to_dict()
             for user in data_manager.storage.get('User', {}).values()]
    return jsonify(users), 200


# ********************************************************************* #


@users_bp.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    """
    * This route gets a user by ID *

    Methods: GET

    Parameters:
        users_id: (str) The user's ID

    Returns:

    - dict: User data

    """

    data_manager = current_app.config['DATA_MANAGER_USERS']
    user = data_manager.get(user_id, 'User')

    if user is None:
        abort(404, 'User not found')
    return jsonify(user.to_dict()), 200


# ********************************************************************* #


@users_bp.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    """
    * This route updates a user *

    Methods: PUT

    Parameters:
        user_id (str): The user's ID

    Request Body:

    - email: (str) The user's email
    - first_name: (str) The user's first name
    - last_name: (str) The user's last name

    Returns:

    - dict: User data


    """

    data_manager = current_app.config['DATA_MANAGER_USERS']
    user = data_manager.get(user_id, 'User')

    if user is None:
        abort(404, 'User not found')

    data = request.json
    if not data:
        abort(400, 'Invalid data')

    new_email = data.get('email', user.email)
    new_first_name = data.get('first_name', user.first_name)
    new_last_name = data.get('last_name', user.last_name)

    # Check if new email is valid
    if 'email' in data and not User.is_valid_email_format(new_email):
        abort(400, 'Invalid email format!')

    # Check if fields are strings
    if 'email' in data and not isinstance(new_email, str):
        abort(400, 'Email must be a string')
    if 'first_name' in data and not isinstance(new_first_name, str):
        abort(400, 'First name must be a string')
    if 'last_name' in data and not isinstance(new_last_name, str):
        abort(400, 'Last name must be a string')

    # Check if fields are not empty
    if 'email' in data and not new_email.strip():
        abort(400, 'Email cannot be empty')
    if 'first_name' in data and not new_first_name.strip():
        abort(400, 'First name cannot be empty')
    if 'last_name' in data and not new_last_name.strip():
        abort(400, 'Last name cannot be empty')

    # Check if new email already exists
    if new_email != user.email and data_manager.get_by_email(new_email):
        abort(409, 'Email already exists')

    try:
        user.email = new_email
        user.first_name = new_first_name
        user.last_name = new_last_name
        user.updated_at = datetime.utcnow()
    except ValueError as e:
        abort(400, str(e))

    data_manager.update(user)
    return jsonify(user.to_dict()), 200


# ********************************************************************* #


@users_bp.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    """
    * This route deletes a user *

    Methods: DELETE

    Parameters:
        user_id (str): The user's ID

    Returns:

    - str: Empty string


    """

    data_manager = current_app.config['DATA_MANAGER_USERS']

    if not data_manager.delete(user_id, 'User'):
        abort(404, 'User not found')
    return '', 204
