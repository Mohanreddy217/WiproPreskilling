from flask import Blueprint, request, jsonify

order_bp = Blueprint("order", __name__)

orders = []
order_id_counter = 1


@order_bp.route("/api/v1/orders", methods=["POST"])
def place_order():
    global order_id_counter
    data = request.get_json()

    order = {
        "id": order_id_counter,
        "user_id": data.get("user_id"),
        "restaurant_id": data.get("restaurant_id"),
        "dish_id": data.get("dish_id"),
        "status": "Placed"
    }

    orders.append(order)
    order_id_counter += 1

    return jsonify(order), 201


@order_bp.route("/api/v1/orders/user/<int:user_id>", methods=["GET"])
def get_orders_by_user(user_id):
    return jsonify([o for o in orders if o["user_id"] == user_id]), 200


@order_bp.route("/api/v1/orders/restaurant/<int:restaurant_id>", methods=["GET"])
def get_orders_by_restaurant(restaurant_id):
    return jsonify([o for o in orders if o["restaurant_id"] == restaurant_id]), 200


@order_bp.route("/api/v1/orders/<int:order_id>", methods=["PUT"])
def update_order(order_id):
    data = request.get_json()
    for order in orders:
        if order["id"] == order_id:
            order["status"] = data.get("status")
            return jsonify(order), 200
    return jsonify({"error": "Order not found"}), 404


@order_bp.route("/api/v1/orders/<int:order_id>/cancel", methods=["PUT"])
def cancel_order(order_id):
    for order in orders:
        if order["id"] == order_id:
            order["status"] = "Cancelled"
            return jsonify(order), 200
    return jsonify({"error": "Order not found"}), 404
