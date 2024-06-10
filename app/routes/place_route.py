from flask import Flask, jsonify, request, abort
from app.models.place import Place
from app.persistence.data_manager import DataManager
from datetime import datetime

app = Flask(__name__)
data_manager = DataManager()

DATA_FILE = "data_place.json"  # Define the data file


@app.route('/places', methods=['POST'])
def create_place():
    data = request.get_json()
    if not data:
        abort(400, 'No input data provided')
    name = data.get('name')
    description = data.get('description')
    address = data.get('address')
    city_id = data.get('city_id')
    latitude = data.get('latitude')
    longitude = data.get('longitude')
    host_id = data.get('host_id')
    num_rooms = data.get('num_rooms')
    num_bathrooms = data.get('num_bathrooms')
    price_per_night = data.get('price_per_night')
    max_guests = data.get('max_guests')
    if not all([name, address, city_id, host_id, num_rooms, num_bathrooms, price_per_night, max_guests]):
        abort(400, 'Missing required fields')
    place = Place(name, description, address, city_id, latitude, longitude,
                  host_id, num_rooms, num_bathrooms, price_per_night, max_guests)
    data_manager.save(place)
    data_manager.save_to_json(DATA_FILE)  # Save to JSON file
    return jsonify(place.to_dict()), 201


@app.route('/places', methods=['GET'])
def get_places():
    place_objects = data_manager.storage.get('Place', {}).values()
    places = [place.to_dict() for place in place_objects]
    return jsonify(places), 200


@app.route('/places/<place_id>', methods=['GET'])
def get_place(place_id):
    place = data_manager.get(place_id, 'Place')
    if place is None:
        abort(404, 'Place not found')
    return jsonify(place.to_dict()), 200


@app.route('/places/<place_id>', methods=['PUT'])
def update_place(place_id):
    place = data_manager.get(place_id, 'Place')
    if place is None:
        abort(404, 'Place not found')
    data = request.get_json()
    if not data:
        abort(400, 'No input data provided')
    for key, value in data.items():
        if hasattr(place, key):
            setattr(place, key, value)
    place.updated_at = datetime.utcnow()
    data_manager.save(place)
    data_manager.save_to_json(DATA_FILE)  # Save to JSON file
    return jsonify(place.to_dict()), 200


@app.route('/places/<place_id>', methods=['DELETE'])
def delete_place(place_id):
    place = data_manager.get(place_id, 'Place')
    if place is None:
        abort(404, 'Place not found')
    data_manager.delete(place_id, 'Place')
    data_manager.save_to_json(DATA_FILE)  # Save to JSON file
    return jsonify({}), 204


if __name__ == '__main__':
    app.run(debug=True)
