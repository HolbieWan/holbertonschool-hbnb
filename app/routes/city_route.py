from flask import Flask, jsonify, request, abort
from app.models.city import City
from app.persistence.data_manager import DataManager
from datetime import datetime

app = Flask(__name__)
data_manager = DataManager()
DATA_FILE = "data_city.json"


@app.route('/city', methods=['POST'])
def create_city():
    if not request.json or not all(key in request.json for key in ['name', 'country_id']):
        abort(400, 'Name and country_id are required')
    name = request.json['name']
    country_id = request.json['country_id']
    city = City(name, country_id)
    data_manager.save(city)
    data_manager.save_to_json(DATA_FILE)
    return jsonify(city.to_dict()), 201


@app.route('/city', methods=['GET'])
def get_cities():
    cities = [city.to_dict()
              for city in data_manager.storage.get('City', {}).values()]
    return jsonify(cities), 200


@app.route('/city/<city_id>', methods=['GET'])
def get_city(city_id):
    city = data_manager.get(city_id, 'City')
    if city is None:
        abort(404, 'City not found')
    return jsonify(city.to_dict()), 200


@app.route('/city/<city_id>', methods=['PUT'])
def update_city(city_id):
    city = data_manager.get(city_id, 'City')
    if city is None:
        abort(404, 'City not found')
    if not request.json:
        abort(400, 'Invalid data')
    city.name = request.json.get('name', city.name)
    city.country_id = request.json.get('country_id', city.country_id)
    city.updated_at = datetime.utcnow()
    data_manager.update(city)
    data_manager.save_to_json(DATA_FILE)
    return jsonify(city.to_dict()), 200


@app.route('/city/<city_id>', methods=['DELETE'])
def delete_city(city_id):
    if not data_manager.delete(city_id, 'City'):
        abort(404, 'City not found')
    data_manager.save_to_json(DATA_FILE)
    return '', 204


if __name__ == '__main__':
    app.run(debug=True)
