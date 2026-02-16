from flask import Blueprint, jsonify
from routes.restaurant import restaurants
from routes.order import orders

admin_bp = Blueprint("admin", __name__)


@admin_bp.route("/api/v1/admin/restaurants/<int:restaurant_id>/approve", methods=["PUT"])
def approve_restaurant(restaurant_id):
    for restaurant in restaurants:
        if restaurant["id"] == restaurant_id:
            restaurant["approved"] = True
            return jsonify({"message": "Restaurant approved"}), 200
    return jsonify({"error": "Restaurant not found"}), 404


@admin_bp.route("/api/v1/admin/restaurants", methods=["GET"])
def get_all_restaurants():
    return jsonify(restaurants), 200


@admin_bp.route("/api/v1/admin/orders", methods=["GET"])
def get_all_orders():
    return jsonify(orders), 200
