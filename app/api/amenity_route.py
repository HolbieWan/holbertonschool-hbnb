# app/api/amenity_route.py
from flask import Blueprint, jsonify, request, abort
from datetime import datetime
from models.amenity import Amenity
from persistence.data_manager import DataManager
data_manager = DataManager()

amenity_bp = Blueprint('amenity', __name__)
DATA_FILE = "data_amenity.json"


@amenity_bp.route('/amenities', methods=['POST'])
def create_amenity():
    if not request.json or not 'name' in request.json:
        abort(400, 'Amenity name is required')
    try:
        name = request.json.get('name', "")
        amenity = Amenity(name)
    except ValueError as e:
        abort(400, str(e))
    data_manager.save(amenity)
    data_manager.save_to_json(DATA_FILE)
    return jsonify(amenity.to_dict()), 201


@amenity_bp.route('/amenities', methods=['GET'])
def get_amenities():
    amenities = [amenity.to_dict()
                 for amenity in data_manager.storage.get('Amenity', {}).values()]
    return jsonify(amenities), 200


@amenity_bp.route('/amenities/<amenity_id>', methods=['GET'])
def get_amenity(amenity_id):
    amenity = data_manager.get(amenity_id, 'Amenity')
    if amenity is None:
        abort(404, 'Amenity not found')
    return jsonify(amenity.to_dict()), 200


@amenity_bp.route('/amenities/<amenity_id>', methods=['PUT'])
def update_amenity(amenity_id):
    amenity = data_manager.get(amenity_id, 'Amenity')
    if amenity is None:
        abort(404, 'Amenity not found')
    if not request.json:
        abort(400, 'Invalid data')
    new_name = request.json.get('name', amenity.name)
    try:
        if 'name' in request.json and not new_name:
            abort(400, 'Name is required!')
        amenity.name = new_name
        amenity.updated_at = datetime.utcnow()
    except ValueError as e:
        abort(400, str(e))
    data_manager.update(amenity)
    data_manager.save_to_json(DATA_FILE)
    return jsonify(amenity.to_dict()), 200



@amenity_bp.route('/amenities/<amenity_id>', methods=['DELETE'])
def delete_amenity(amenity_id):
    if not data_manager.delete(amenity_id, 'Amenity'):
        abort(404, 'Amenity not found')
    data_manager.save_to_json(DATA_FILE)
    return '', 204
