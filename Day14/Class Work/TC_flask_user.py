from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory data
users = [
    {"id": 1, "name": "Raja"},
    {"id": 2, "name": "Rama"}
]

# Home
@app.route("/", methods=["GET"])
def home():
    return "Welcome"

# Get all users
@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users)

# Get single user
@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = next((u for u in users if u["id"] == user_id), None)
    if not user:
        return jsonify({"message": "user not found"}), 404
    return jsonify(user)

# Create user
@app.route("/users", methods=["POST"])
def add_user():
    data = request.json
    new_user = {
        "id": users[-1]["id"] + 1 if users else 1,
        "name": data.get("name")
    }
    users.append(new_user)
    return jsonify(new_user), 201

# PUT & PATCH update user (SINGLE route)
@app.route("/users/<int:user_id>", methods=["PUT", "PATCH"])
def update_user(user_id):
    user = next((u for u in users if u["id"] == user_id), None)
    if not user:
        return jsonify({"message": "user not found"}), 404

    data = request.json

    if "name" in data:
        user["name"] = data["name"]

    return jsonify(user), 200

# DELETE user
@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    user = next((u for u in users if u["id"] == user_id), None)

    if not user:
        return jsonify({"message": "user not found"}), 404

    users.remove(user)
    return jsonify({"message": "user deleted successfully"}), 200



if __name__ == "__main__":
    app.run(debug=True)
