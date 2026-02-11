from flask import Blueprint, request, jsonify
from routes.restaurant import restaurants

dish_bp = Blueprint("dish", __name__)

dish_id_counter = 1


@dish_bp.route("/api/v1/restaurants/<int:restaurant_id>/dishes", methods=["POST"])
def add_dish(restaurant_id):
    global dish_id_counter

    data = request.get_json()

    for restaurant in restaurants:
        if restaurant["id"] == restaurant_id:

            dish = {
                "id": dish_id_counter,
                "name": data.get("name"),
                "price": data.get("price"),
                "availability": True
            }

            restaurant["dishes"].append(dish)
            dish_id_counter += 1

            return jsonify(dish), 201

    return jsonify({"error": "Restaurant not found"}), 404
@dish_bp.route("/api/v1/restaurants/<int:restaurant_id>/dishes/<int:dish_id>", methods=["PUT"])
def update_dish(restaurant_id, dish_id):

    data = request.get_json()

    for restaurant in restaurants:
        if restaurant["id"] == restaurant_id:
            for dish in restaurant["dishes"]:
                if dish["id"] == dish_id:
                    dish.update(data)
                    return jsonify(dish), 200

    return jsonify({"error": "Dish not found"}), 404
@dish_bp.route("/api/v1/restaurants/<int:restaurant_id>/dishes/<int:dish_id>/disable", methods=["PUT"])
def disable_dish(restaurant_id, dish_id):

    for restaurant in restaurants:
        if restaurant["id"] == restaurant_id:
            for dish in restaurant["dishes"]:
                if dish["id"] == dish_id:
                    dish["availability"] = False
                    return jsonify({"message": "Dish disabled successfully"}), 200

    return jsonify({"error": "Dish not found"}), 404
