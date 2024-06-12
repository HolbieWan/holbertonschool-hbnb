from flask import Blueprint, jsonify, request, abort
from datetime import datetime
from models.city import City
from persistence.data_manager import DataManager
data_manager = DataManager()

city_bp = Blueprint('city', __name__)
DATA_FILE = "data_city.json"


@city_bp.route('/city', methods=['POST'])
def create_city():
    if not request.json or not all(key in request.json for key in ['name', 'country_id']):
        abort(400, 'Name and country_code are required')
    try:
        name = request.json['name']
        country_id = request.json['country_id']
        city = City(name, country_id)
    except ValueError as e:
        abort(400, str(e))
    data_manager.save(city)
    data_manager.save_to_json(DATA_FILE)
    return jsonify(city.to_dict()), 201


@city_bp.route('/city', methods=['GET'])
def get_cities():
    cities = [city.to_dict()
              for city in data_manager.storage.get('City', {}).values()]
    return jsonify(cities), 200


@city_bp.route('/city/<city_id>', methods=['GET'])
def get_city(city_id):
    city = data_manager.get(city_id, 'City')
    if city is None:
        abort(404, 'City not found')
    return jsonify(city.to_dict()), 200


@city_bp.route('/city/<city_id>', methods=['PUT'])
def update_city(city_id):
    city = data_manager.get(city_id, 'City')
    if city is None:
        abort(404, 'City not found')
    if not request.json:
        abort(400, 'Invalid data')
    new_name = request.json.get('name', city.name)
    new_country_id = request.json.get('country_id', city.country_id)
    try:
        if 'name' in request.json and not new_name:
            abort(400, 'Name is required!')
        if 'country_id' in request.json and not new_country_id:
            abort(400, 'Country ID is required!')
        city.name = new_name
        city.country_id = new_country_id
        city.updated_at = datetime.utcnow()
    except ValueError as e:
        abort(400, str(e))
    data_manager.update(city)
    data_manager.save_to_json(DATA_FILE)
    return jsonify(city.to_dict()), 200


@city_bp.route('/city/<city_id>', methods=['DELETE'])
def delete_city(city_id):
    if not data_manager.delete(city_id, 'City'):
        abort(404, 'City not found')
    data_manager.save_to_json(DATA_FILE)
    return '', 204
