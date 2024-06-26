from flask import Blueprint, jsonify, request, abort, current_app
from models.country import Country
from datetime import datetime

country_bp = Blueprint('country', __name__)


@country_bp.route('/country', methods=['POST'])
def create_country():
    """
    * This route creates a new country *

    Methods: POST

    Request Body:

    - name (str) The country's name
    - code (str) The country's code

    Returns:

    - dict: Country data


    """

    data_manager = current_app.config['DATA_MANAGER_COUNTRIES']

    if not request.json or 'name' not in request.json:
        abort(400, 'Name is required')

    name = request.json['name']
    code = request.json.get('code', None)

    try:
        country = Country(name, code)
        data_manager.save(country)
    except ValueError as e:
        abort(400, str(e))
    return jsonify(country.to_dict()), 201


# ********************************************************************* #

@country_bp.route('/country', methods=['GET'])
def get_countries():
    """
    * This route retrieves all countries *

    Methods: GET

    Returns:

    - list: List of country data


    """

    data_manager = current_app.config['DATA_MANAGER_COUNTRIES']

    countries = [country.to_dict()
                 for country in
                 data_manager.storage.get('Country', {}).values()]
    return jsonify(countries), 200


# ********************************************************************* #


@country_bp.route('/country/<country_code>', methods=['GET'])
def get_country_code(country_code):
    """
    * This route gets a country by code *

    Methods: GET

    Parameters:
        country_code: (str) The country's code

    Returns:

    - dict: Country data


    """
    data_manager = current_app.config['DATA_MANAGER_COUNTRIES']
    country = data_manager.get_country_by_code(country_code)

    if country is None:
        abort(404, 'Country not found')
    return jsonify(country.to_dict()), 200


# ********************************************************************* #


@country_bp.route('/country/<country_id>', methods=['PUT'])
def update_country(country_id):
    """
    * This route updates a country *

    Methods: PUT

    Parameters:
        country_id: (str) The country's ID

    Request Body:

    - name (str) The country's name
    - code (str) The country's code

    Returns:

    - dict: Country data


    """

    data_manager = current_app.config['DATA_MANAGER_COUNTRIES']
    country = data_manager.get(country_id, 'Country')

    if country is None:
        abort(404, 'Country not found')
    data = request.get_json()

    if not data:
        abort(400, 'Invalid data')
    new_name = data.get('name', country.name)
    new_code = data.get('code', country.code)

    try:
        if 'name' in data and not new_name:
            abort(400, 'Name is required!')
        country.name = new_name
        country.code = new_code
        country.updated_at = datetime.utcnow()
        data_manager.save(country)
    except ValueError as e:
        abort(400, str(e))
    return jsonify(country.to_dict()), 200


# ********************************************************************* #

@country_bp.route('/country/<country_id>', methods=['DELETE'])
def delete_country(country_id):
    """
    * This route deletes a country *

    Methods: DELETE

    Parameters:
        country_id: (str) The country's ID

    Returns:

    - str: Empty string


    """
    data_manager = current_app.config['DATA_MANAGER_COUNTRIES']

    if not data_manager.delete(country_id, 'Country'):
        abort(404, 'Country not found')
    return '', 204
