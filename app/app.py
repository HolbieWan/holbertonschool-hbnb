from api.users_route import users_bp
from api.review_route import review_bp
from api.place_route import place_bp
from api.country_route import country_bp
from api.city_route import city_bp
from api.amenity_route import amenity_bp
from flask import Flask, send_from_directory
from flask_swagger_ui import get_swaggerui_blueprint
import os


app = Flask(__name__)


app.register_blueprint(amenity_bp)
app.register_blueprint(city_bp)
app.register_blueprint(country_bp)
app.register_blueprint(place_bp)
app.register_blueprint(review_bp)
app.register_blueprint(users_bp)

SWAGGER_URL = '/api/docs'
API_URL = '/swagger.json'

SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Your API Documentation"
    }
)

app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)


@app.route('/swagger.json')
def serve_swagger():
    return send_from_directory(os.getcwd(), 'swagger.json')


if __name__ == "__main__":
    app.run(debug=True)
