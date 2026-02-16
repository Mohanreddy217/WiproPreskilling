from flask import Blueprint, request, jsonify

user_bp = Blueprint("user", __name__)

users = []
user_id_counter = 1


@user_bp.route("/api/v1/users/register", methods=["POST"])
def register_user():
    global user_id_counter
    data = request.get_json()

    user = {
        "id": user_id_counter,
        "name": data.get("name"),
        "email": data.get("email")
    }

    users.append(user)
    user_id_counter += 1

    return jsonify(user), 201


@user_bp.route("/api/v1/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    for user in users:
        if user["id"] == user_id:
            return jsonify(user), 200
    return jsonify({"error": "User not found"}), 404
