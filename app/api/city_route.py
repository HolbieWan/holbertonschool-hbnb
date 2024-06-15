from flask import Blueprint, jsonify, request, abort, current_app
from datetime import datetime
from models.city import City

city_bp = Blueprint('city', __name__)


@city_bp.route('/cities', methods=['POST'])
def create_city():
    """
    * This route creates a new city *

    Methods: POST

    Request Body:

    - name (str) The city's name
    - country_id (str) The country's id

    Returns:

    - dict: City data


    """

    data_manager = current_app.config['DATA_MANAGER_CITIES']

    if not request.json or not all(key in request.json for
                                   key in ['name', 'country_id']):
        abort(400, 'Name and country_id are required')
    try:
        name = request.json['name']
        country_id = request.json['country_id']
        city = City(name, country_id, data_manager)
    except ValueError as e:
        abort(400, str(e))
    data_manager.save(city)
    return jsonify(city.to_dict()), 201


# ********************************************************************* #


@city_bp.route('/cities', methods=['GET'])
def get_cities():
    """
    * This route retrieves all cities *

    Methods: GET

    Returns:

    - list: List of city data

    """
    data_manager = current_app.config['DATA_MANAGER_CITIES']

    cities = [city.to_dict()
              for city in data_manager.storage.get('City', {}).values()]
    return jsonify(cities), 200


# ********************************************************************* #


@city_bp.route('/cities/<city_id>', methods=['GET'])
def get_city(city_id):
    """
    * This route gets a city by ID *

    Methods: GET

    Parameters:
        city_id: (str) The city's ID

    Returns:

    - dict: City data

    """
    data_manager = current_app.config['DATA_MANAGER_CITIES']
    city = data_manager.get(city_id, 'City')

    if city is None:
        abort(404, 'City not found')
    return jsonify(city.to_dict()), 200


# ********************************************************************* #


@city_bp.route('/cities/<city_id>', methods=['PUT'])
def update_city(city_id):
    """
    * This route updates a city *

    Methods: PUT

    Parameters:
        city_id: (str) The city's ID

    Request Body:

    - name (str) The city's name
    - country_id (str) The country's id

    Returns:

    - dict: City data


    """
    data_manager = current_app.config['DATA_MANAGER_CITIES']
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
    return jsonify(city.to_dict()), 200


# ********************************************************************* #


@city_bp.route('/cities/<city_id>', methods=['DELETE'])
def delete_city(city_id):
    """
    * This route deletes a city *

    Methods: DELETE

    Parameters:
        city_id: (str) The city's ID

    Returns:

    - str: Empty string


    """

    data_manager = current_app.config['DATA_MANAGER_CITIES']

    if not data_manager.delete(city_id, 'City'):
        abort(404, 'City not found')
    return '', 204


# ********************************************************************* #


@city_bp.route('/country/<country_code>/cities', methods=['GET'])
def get_city_by_country_code(country_code):
    """
    * This route retrieves all cities for a country *

    Methods: GET

    Parameters:
        country_code: (str) The country's code

    Returns:

    - list: List of city data


    """
    data_manager = current_app.config['DATA_MANAGER_CITIES']
    cities = []

    for city in data_manager.storage.get('City', {}).values():
        if city.country_id == country_code:
            cities.append(city.to_dict())

    if not cities:
        abort(404, f'No cities found for country code {country_code}')
    return jsonify(cities), 200
