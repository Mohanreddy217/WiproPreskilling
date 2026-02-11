from flask import Blueprint, jsonify
from routes.restaurant import restaurants

admin_bp = Blueprint("admin", __name__)


@admin_bp.route("/api/v1/admin/restaurants/<int:restaurant_id>/approve", methods=["PUT"])
def approve_restaurant(restaurant_id):

    for restaurant in restaurants:
        if restaurant["id"] == restaurant_id:
            restaurant["approved"] = True
            return jsonify({"message": "Restaurant approved successfully"}), 200

    return jsonify({"error": "Restaurant not found"}), 404
