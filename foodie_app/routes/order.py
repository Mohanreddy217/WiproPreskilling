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

    user_orders = [order for order in orders if order["user_id"] == user_id]

    return jsonify(user_orders), 200
@order_bp.route("/api/v1/orders/restaurant/<int:restaurant_id>", methods=["GET"])
def get_orders_by_restaurant(restaurant_id):

    restaurant_orders = [order for order in orders if order["restaurant_id"] == restaurant_id]

    return jsonify(restaurant_orders), 200
