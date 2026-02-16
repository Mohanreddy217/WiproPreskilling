from flask import Blueprint, request, jsonify

restaurant_bp = Blueprint("restaurant", __name__)

restaurants = []
restaurant_id_counter = 1


@restaurant_bp.route("/api/v1/restaurants", methods=["POST"])
def create_restaurant():
    global restaurant_id_counter

    data = request.get_json()

    restaurant = {
        "id": restaurant_id_counter,
        "name": data.get("name"),
        "category": data.get("category"),
        "location": data.get("location"),
        "contact": data.get("contact"),
        "approved": False,
        "enabled": True,
        "dishes": []
    }

    restaurants.append(restaurant)
    restaurant_id_counter += 1

    return jsonify(restaurant), 201


@restaurant_bp.route("/api/v1/restaurants/<int:restaurant_id>", methods=["GET"])
def get_restaurant(restaurant_id):
    for restaurant in restaurants:
        if restaurant["id"] == restaurant_id:
            return jsonify(restaurant), 200
    return jsonify({"error": "Restaurant not found"}), 404


@restaurant_bp.route("/api/v1/restaurants/<int:restaurant_id>", methods=["PUT"])
def update_restaurant(restaurant_id):
    data = request.get_json()
    for restaurant in restaurants:
        if restaurant["id"] == restaurant_id:
            restaurant.update(data)
            return jsonify(restaurant), 200
    return jsonify({"error": "Restaurant not found"}), 404


@restaurant_bp.route("/api/v1/restaurants/<int:restaurant_id>/disable", methods=["PUT"])
def disable_restaurant(restaurant_id):
    for restaurant in restaurants:
        if restaurant["id"] == restaurant_id:
            restaurant["enabled"] = False
            return jsonify({"message": "Restaurant disabled"}), 200
    return jsonify({"error": "Restaurant not found"}), 404
