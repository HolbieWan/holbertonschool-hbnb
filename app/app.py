from api.users_route import users_bp
from api.review_route import review_bp
from api.place_route import place_bp
from api.country_route import country_bp
from api.city_route import city_bp
from api.amenity_route import amenity_bp
from flask import Flask, send_from_directory
from flask_swagger_ui import get_swaggerui_blueprint
from persistence.data_manager import DataManager
import os
port = os.getenv('PORT')


# Initialize Flask app
app = Flask(__name__)


# Initialize DataManagers with the appropriate JSON file paths
data_manager_users = DataManager("data/data_users.json")
data_manager_reviews = DataManager("data/data_reviews.json")
data_manager_places = DataManager("data/data_places.json")
data_manager_countries = DataManager("data/data_countries.json")
data_manager_cities = DataManager("data/data_cities.json")
data_manager_amenities = DataManager("data/data_amenities.json")

# Set the data_manager for each blueprint in the app configuration
app.config['DATA_MANAGER_USERS'] = data_manager_users
app.config['DATA_MANAGER_REVIEWS'] = data_manager_reviews
app.config['DATA_MANAGER_PLACES'] = data_manager_places
app.config['DATA_MANAGER_COUNTRIES'] = data_manager_countries
app.config['DATA_MANAGER_CITIES'] = data_manager_cities
app.config['DATA_MANAGER_AMENITIES'] = data_manager_amenities

# Register blueprints
app.register_blueprint(amenity_bp)
app.register_blueprint(city_bp)
app.register_blueprint(country_bp)
app.register_blueprint(place_bp)
app.register_blueprint(review_bp)
app.register_blueprint(users_bp)

# Swagger setup
SWAGGER_URL = '/api/docs'
API_URL = '/swagger.yaml'

SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Your API Documentation"
    }
)

app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)


@app.route('/swagger.yaml')
def serve_swagger():
    return send_from_directory(os.getcwd(), 'swagger.yaml')


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=port)
