from flask import Flask
from routes.restaurant import restaurant_bp
from routes.dish import dish_bp
from routes.user import user_bp
from routes.order import order_bp
from routes.admin import admin_bp

app = Flask(__name__)

app.register_blueprint(restaurant_bp)
app.register_blueprint(dish_bp)
app.register_blueprint(user_bp)
app.register_blueprint(order_bp)
app.register_blueprint(admin_bp)

if __name__ == "__main__":
    app.run(debug=True)
