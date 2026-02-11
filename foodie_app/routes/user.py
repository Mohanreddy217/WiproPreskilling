from flask import Blueprint, request, jsonify

user_bp = Blueprint("user", __name__)

users = []
user_id_counter = 1


@user_bp.route("/api/v1/users/register", methods=["POST"])
def register_user():
    global user_id_counter

    data = request.get_json()

    if not data.get("name") or not data.get("email"):
        return jsonify({"error": "Name and Email required"}), 400

    user = {
        "id": user_id_counter,
        "name": data["name"],
        "email": data["email"]
    }

    users.append(user)
    user_id_counter += 1

    return jsonify(user), 201
