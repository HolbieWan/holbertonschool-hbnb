from flask import Blueprint, jsonify, request, abort
from datetime import datetime
from models.country import Country
from persistence.data_manager import DataManager
data_manager = DataManager()

country_bp = Blueprint('country', __name__)

DATA_FILE = "data_country.json"  # Define the data file


@country_bp.route('/country', methods=['POST'])
def create_country():
    if not request.json or not all(key in request.json for key in ['name', 'code']):
        abort(400, 'Name and code are required')
    try:
        name = request.json['name']
        code = request.json['code']
        country = Country(name, code)
    except ValueError as e:
        abort(400, str(e))
    data_manager.save(country)
    data_manager.save_to_json(DATA_FILE)
    return jsonify(country.to_dict()), 201


@country_bp.route('/country', methods=['GET'])
def get_countries():
    countries = [country.to_dict()
                 for country in data_manager.storage.get('Country', {}).values()]
    return jsonify(countries), 200


@country_bp.route('/country/<country_id>', methods=['GET'])
def get_country(country_id):
    country = data_manager.get(country_id, 'Country')
    if country is None:
        abort(404, 'Country not found')
    return jsonify(country.to_dict()), 200


@country_bp.route('/country/<country_code>', methods=['GET'])
def get_country_code(country_code):
    country = data_manager.get(country_code, 'Country')
    if country is None:
        abort(404, 'Country not found')
    return jsonify(country.to_dict()), 200


@country_bp.route('/country/<country_id>', methods=['PUT'])
def update_country(country_id):
    country = data_manager.get(country_id, 'Country')
    if country is None:
        abort(404, 'Country not found')
    if not request.json:
        abort(400, 'Invalid data')
    new_name = request.json.get('name', country.name)
    new_code = request.json.get('code', country.code)
    try:
        if 'name' in request.json and not new_name:
            abort(400, 'Name is required!')
        country.name = new_name
        country.code = new_code
        country.updated_at = datetime.utcnow()
    except ValueError as e:
        abort(400, str(e))
    data_manager.update(country)
    data_manager.save_to_json(DATA_FILE)
    return jsonify(country.to_dict()), 200


@country_bp.route('/country/<country_id>', methods=['DELETE'])
def delete_country(country_id):
    if not data_manager.delete(country_id, 'Country'):
        abort(404, 'Country not found')
    data_manager.save_to_json(DATA_FILE)  # Save to JSON file
    return '', 204
