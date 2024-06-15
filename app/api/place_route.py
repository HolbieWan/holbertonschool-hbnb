from flask import Blueprint, jsonify, request, abort, current_app
from models.place import Place
from datetime import datetime

place_bp = Blueprint('place', __name__)


@place_bp.route('/places', methods=['POST'])
def create_place():
    """
    * This route creates a new place *

    Methods: POST

    Request Body:

    - name (str) The place's name
    - description (str) The place's description
    - address (str) The place's address
    - city_id (str) The city's id
    - latitude (float) The place's latitude
    - longitude (float) The place's longitude
    - host_id (str) The host's id
    - num_rooms (int) The number of rooms in the place
    - num_bathrooms (int) The number of bathrooms in the place
    - price_per_night (float) The price per night
    - max_guests (int) The maximum number of guests in the place
    - amenities (list) A list of amenity ids

    Returns:

    - dict: Place data


    """

    data_manager = current_app.config['DATA_MANAGER_PLACES']

    if not request.json:
        abort(400, 'No input data provided')

    name = request.json.get('name')
    description = request.json.get('description')
    address = request.json.get('address')
    city_id = request.json.get('city_id')

    try:
        latitude = float(request.json.get('latitude'))
        longitude = float(request.json.get('longitude'))
        host_id = request.json.get('host_id')
        num_rooms = int(request.json.get('num_rooms'))
        num_bathrooms = int(request.json.get('num_bathrooms'))
        price_per_night = float(request.json.get('price_per_night'))
        max_guests = int(request.json.get('max_guests'))
    except ValueError as e:
        abort(400, str(e))
    amenities = request.json.get('amenities', [])

    if not all([name, address, city_id, host_id, num_rooms, num_bathrooms,
                price_per_night, max_guests]):
        abort(400, 'Missing required fields')
    if data_manager.place_exists_with_attributes(name, address, city_id,
                                                 host_id,
                                                 num_rooms, num_bathrooms,
                                                 price_per_night,
                                                 max_guests):
        abort(409, 'A similar place already exists')
    try:
        place = Place(name, description, address, city_id, latitude,
                      longitude,
                      host_id, num_rooms, num_bathrooms, price_per_night,
                      max_guests, amenities, data_manager)
    except ValueError as e:
        abort(400, str(e))
    data_manager.save(place)
    return jsonify(place.to_dict()), 201

# ********************************************************************* #


@place_bp.route('/places', methods=['GET'])
def get_places():
    data_manager = current_app.config['DATA_MANAGER_PLACES']
    place_objects = data_manager.storage.get('Place', {}).values()
    places = []
    for place in place_objects:
        place_dict = place.to_dict()
        city = data_manager.get(place_dict['city_id'], 'City')
        place_dict['city'] = city.to_dict() if city else None
        amenities = [data_manager.get(amenity_id, 'Amenity').to_dict(
        ) for amenity_id in place_dict['amenities'] if
            data_manager.get(amenity_id, 'Amenity')]
        place_dict['amenities'] = amenities
        places.append(place_dict)
    return jsonify(places), 200


# ********************************************************************* #


@place_bp.route('/places/<place_id>', methods=['GET'])
def get_place(place_id):
    """
    * This route gets a place by ID *

    Methods: GET

    Parameters:
        place_id: (str) The place's ID

    Returns:

    - dict: Place data


    """
    data_manager = current_app.config['DATA_MANAGER_PLACES']
    place = data_manager.get(place_id, 'Place')

    if place is None:
        abort(404, 'Place not found')

    place_dict = place.to_dict()
    city = data_manager.get(place_dict['city_id'], 'City')
    place_dict['city'] = city.to_dict() if city else None
    amenities = [data_manager.get(amenity_id, 'Amenity').to_dict(
    ) for amenity_id in place_dict['amenities'] if
        data_manager.get(amenity_id, 'Amenity')]
    place_dict['amenities'] = amenities
    return jsonify(place_dict), 200


# ********************************************************************* #


@place_bp.route('/places/<place_id>', methods=['PUT'])
def update_place(place_id):
    """
    * This route updates a place *

    Methods: PUT

    Parameters:
        place_id: (str) The place's ID

    Request Body:

    - name (str) The place's name
    - description (str) The place's description
    - address (str) The place's address
    - city_id (str) The city's id
    - latitude (float) The place's latitude
    - longitude (float) The place's longitude
    - host_id (str) The host's id
    - num_rooms (int) The number of rooms in the place
    - num_bathrooms (int) The number of bathrooms in the place
    - price_per_night (float) The price per night
    - max_guests (int) The maximum number of guests in the place
    - amenities (list) A list of amenity ids

    Returns:

    - dict: Place data



    """
    data_manager = current_app.config['DATA_MANAGER_PLACES']
    place = data_manager.get(place_id, 'Place')

    if place is None:
        abort(404, 'Place not found')
    data = request.get_json()

    if not data:
        abort(400, 'No input data provided')
    try:
        for key, value in data.items():
            if hasattr(place, key):
                if not value:
                    abort(400, f"Empty value provided for {key}")
                setattr(place, key, value)
        place.updated_at = datetime.utcnow()
        data_manager.save(place)
    except ValueError as e:
        abort(400, str(e))
    return jsonify(place.to_dict()), 200

# ********************************************************************* #


@place_bp.route('/places/<place_id>/amenities/<amenity_id>', methods=['POST'])
def add_amenity_to_place(place_id, amenity_id):
    """
    * This route adds an amenity to a place *

    Methods: POST

    Parameters:
        place_id: (str) The place's ID
        amenity_id: (str) The amenity's ID

    Returns:

    - dict: Place data

    """

    data_manager = current_app.config['DATA_MANAGER_PLACES']
    place = data_manager.get(place_id, 'Place')

    if place is None:
        abort(404, 'Place not found')
    if amenity_id in place.amenities:
        abort(409, 'Amenity already added to the place')
    place.add_amenity(amenity_id)
    data_manager.save(place)
    return jsonify(place.to_dict()), 200


# ********************************************************************* #

@place_bp.route('/places/<place_id>/amenities/<amenity_id>',
                methods=['DELETE'])
def remove_amenity_from_place(place_id, amenity_id):
    """
    * This route removes an amenity from a place *

    Methods: DELETE

    Parameters:

        place_id: (str) The place's ID
        amenity_id: (str) The amenity's ID


    Returns:

    - dict: Place data

    """

    data_manager = current_app.config['DATA_MANAGER_PLACES']
    place = data_manager.get(place_id, 'Place')

    if place is None:
        abort(404, 'Place not found')
    place.remove_amenity(amenity_id)
    data_manager.save(place)
    return jsonify(place.to_dict()), 200


# ********************************************************************* #


@place_bp.route('/places/<place_id>', methods=['DELETE'])
def delete_place(place_id):
    """
    * This route deletes a place *

    Methods: DELETE

    Parameters:
        place_id: (str) The place's ID


    Returns:

    - str: Empty string

    """
    data_manager = current_app.config['DATA_MANAGER_PLACES']
    place = data_manager.get(place_id, 'Place')

    if place is None:
        abort(404, 'Place not found')
    data_manager.delete(place_id, 'Place')
    return '', 204
