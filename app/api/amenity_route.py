from flask import Blueprint, jsonify, request, abort, current_app
from datetime import datetime
from models.amenity import Amenity

amenity_bp = Blueprint('amenity', __name__)


@amenity_bp.route('/amenities', methods=['POST'])
def create_amenity():
    """
    * This route creates a new amenity *

    Methods: POST

    Request Body:

    - name (str) The amenity's name

    Returns:

    - dict: Amenity data


    """

    data_manager = current_app.config['DATA_MANAGER_AMENITIES']

    if not request.json or 'name' not in request.json:
        abort(400, 'Amenity name is required')
    name = request.json.get('name', "")

    try:
        amenity = Amenity(name, data_manager)
    except ValueError as e:
        abort(400, str(e))
    data_manager.save(amenity)
    return jsonify(amenity.to_dict()), 201


# ********************************************************************* #


@amenity_bp.route('/amenities', methods=['GET'])
def get_amenities():
    """
    * This route retrieves all amenities *

    Methods: GET

    Returns:

    - list: List of amenity data


    """
    data_manager = current_app.config['DATA_MANAGER_AMENITIES']
    amenities = [amenity.to_dict()
                 for amenity in
                 data_manager.storage.get('Amenity', {}).values()]
    return jsonify(amenities), 200


# ********************************************************************* #


@amenity_bp.route('/amenities/<amenity_id>', methods=['GET'])
def get_amenity(amenity_id):
    """
    * This route retrieves a specific amenity *

    Methods: GET

    Parameters:
        amenity_id (str) The amenity's id

    Returns:

    - dict: Amenity data


    """

    data_manager = current_app.config['DATA_MANAGER_AMENITIES']
    amenity = data_manager.get(amenity_id, 'Amenity')

    if amenity is None:
        abort(404, 'Amenity not found')
    return jsonify(amenity.to_dict()), 200


# ********************************************************************* #


@amenity_bp.route('/amenities/<amenity_id>', methods=['PUT'])
def update_amenity(amenity_id):
    """
    * This route updates an amenity *

    Methods: PUT

    Parameters:
        amenity_id (str) The amenity's id

    Request Body:

    - name (str) The amenity's name

    Returns:

    - dict: Amenity data


    """

    data_manager = current_app.config['DATA_MANAGER_AMENITIES']
    amenity = data_manager.get(amenity_id, 'Amenity')

    if amenity is None:
        abort(404, 'Amenity not found')
    if not request.json:
        abort(400, 'Invalid data')
    new_name = request.json.get('name', amenity.name)

    try:
        amenity.name = new_name
        amenity.updated_at = datetime.utcnow()
    except ValueError as e:
        abort(400, str(e))
    data_manager.update(amenity)
    return jsonify(amenity.to_dict()), 200


# ********************************************************************* #


@amenity_bp.route('/amenities/<amenity_id>', methods=['DELETE'])
def delete_amenity(amenity_id):
    """
    * This route deletes an amenity *

    Methods: DELETE

    Parameters:
        amenity_id (str) The amenity's id

    Returns:

    - str: Empty string


    """

    data_manager = current_app.config['DATA_MANAGER_AMENITIES']

    if not data_manager.delete(amenity_id, 'Amenity'):
        abort(404, 'Amenity not found')
    return '', 204
