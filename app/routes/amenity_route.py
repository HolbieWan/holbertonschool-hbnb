# app/api/amenity_route.py
from flask import Flask, jsonify, request, abort
from app.models.amenity import Amenity
from app.persistence.data_manager import DataManager
from datetime import datetime

app = Flask(__name__)
data_manager = DataManager()
DATA_FILE = "data_amenity.json"


@app.route('/amenities', methods=['POST'])
def create_amenity():
    if not request.json or not 'name' in request.json:
        abort(400, 'Amenity name is required')
    name = request.json.get('name', "")
    amenity = Amenity(name)
    data_manager.save(amenity)
    data_manager.save_to_json(DATA_FILE)
    return jsonify(amenity.to_dict()), 201


@app.route('/amenities', methods=['GET'])
def get_amenities():
    amenities = [amenity.to_dict()
                 for amenity in data_manager.storage.get('Amenity', {}).values()]
    return jsonify(amenities), 200


@app.route('/amenities/<amenity_id>', methods=['GET'])
def get_amenity(amenity_id):
    amenity = data_manager.get(amenity_id, 'Amenity')
    if amenity is None:
        abort(404, 'Amenity not found')
    return jsonify(amenity.to_dict()), 200


@app.route('/amenities/<amenity_id>', methods=['PUT'])
def update_amenity(amenity_id):
    amenity = data_manager.get(amenity_id, 'Amenity')
    if amenity is None:
        abort(404, 'Amenity not found')
    if not request.json:
        abort(400, 'Invalid data')
    amenity.name = request.json.get('name', amenity.name)
    amenity.updated_at = datetime.utcnow()
    data_manager.update(amenity)
    data_manager.save_to_json(DATA_FILE)
    return jsonify(amenity.to_dict()), 200


@app.route('/amenities/<amenity_id>', methods=['DELETE'])
def delete_amenity(amenity_id):
    if not data_manager.delete(amenity_id, 'Amenity'):
        abort(404, 'Amenity not found')
    data_manager.save_to_json(DATA_FILE)
    return '', 204


if __name__ == '__main__':
    app.run(debug=True)
