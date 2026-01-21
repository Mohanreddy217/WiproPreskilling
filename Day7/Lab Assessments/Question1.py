from flask import Flask, request, jsonify

app = Flask(__name__)

users = [
    {"id": 1, "name": "Mohan", "email": "mohan@gmail.com"},
    {"id": 2, "name": "Pranay", "email": "pranay123@gmail.com"}
]


@app.route("/", methods=["GET"])
def home():
    return "Welcome this is flask"


@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users), 200


@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    for user in users:
        if user["id"] == user_id:
            return jsonify(user), 200
    return jsonify({"message": "User not found"}), 404


@app.route("/users", methods=["POST"])   # ✅ FIXED
def add_user():
    data = request.get_json()

    new_user = {
        "id": len(users) + 1,
        "name": data.get("name"),
        "email": data.get("email")
    }

    users.append(new_user)
    return jsonify(new_user), 201


@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    data = request.get_json()

    for user in users:
        if user["id"] == user_id:
            user["name"] = data.get("name")
            return jsonify(user), 200

    return jsonify({"message": "User not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)
