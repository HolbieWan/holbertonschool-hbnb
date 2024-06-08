from flask import Flask, jsonify, request
from email_validator import validate_email, EmailNotValidError
from datetime import datetime
from models.user import User


app = Flask(__name__)

users = {}


@app.route("/")
def home():
    return "Welcome to our HBNB!"


@app.route("/users", methods=["POST"])
def add_user():

    user_data = request.get_json()
    email = user_data.get("email")

    try:
        validate_email(email)
    except EmailNotValidError as e:
        return jsonify({"error": "Invalid email"}), 400

    first_name = user_data.get("first_name")
    last_name = user_data.get("last_name")

    if not all([email, first_name, last_name]):
        return jsonify({"error": "first name, last name and email are required"}), 400

    new_user = User(email, first_name, last_name)
    users[new_user.id] = new_user.to_dict()

    return jsonify({
        "message": "User added",
        "user": new_user.to_dict()
    }), 201


@app.route("/users", methods=["GET"])
def get_users():
    users_list = []
    for user in users.values():
        user_data = {
            "email": user["email"],
            "first_name": user["first_name"],
            "last_name": user["last_name"]
        }
        users_list.append(user_data)

        return jsonify(users_list)


@ app.route("/users/<user_id>", methods=["GET"])
def get_user(user_id):

    user = users.get(user_id)

    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404


@ app.route("/users/<user_id>", methods=["PUT"])
def update_user(user_id):

    user_data = request.get_json()
    user = users.get(user_id)

    if not user:
        return jsonify({"error": "User not found"}), 404

    email = user_data.get("email", user["email"])
    first_name = user_data.get("first_name", user["first_name"])
    last_name = user_data.get("last_name", user["last_name"])

    try:
        validate_email(email)
    except EmailNotValidError as e:
        return jsonify({"error": "Invalid email"}), 400

    user["email"] = email
    user["first_name"] = first_name
    user["last_name"] = last_name
    user["updated_at"] = datetime.now().isoformat()

    return jsonify({
        "message": "User updated",
        "user": user
    })


@ app.route("/users/<user_id>", methods=["DELETE"])
def delete_user(user_id):

    if user_id not in users:
        return jsonify({"error": "User not found"}), 404

    del users[user_id]
    return jsonify({"message": "User deleted"})


if __name__ == "__main__":
    app.run()
