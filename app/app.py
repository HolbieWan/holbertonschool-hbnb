from flask import Flask
from api.amenity_route import amenity_bp
from api.city_route import city_bp
from api.country_route import country_bp
from api.place_route import place_bp
from api.review_route import review_bp
from api.users_route import users_bp

app = Flask(__name__)

app.register_blueprint(amenity_bp)
app.register_blueprint(city_bp)
app.register_blueprint(country_bp)
app.register_blueprint(place_bp)
app.register_blueprint(review_bp)
app.register_blueprint(users_bp)

if __name__ == "__main__":
    app.run(debug=True)
