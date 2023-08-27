from flask import request, Flask, jsonify
from config import Config
from app.database import DatabaseConnection
from .models.product import Product
from .controllers.product_controller import ProductController


def ejercicios_mysql():
    """Crea y configura la aplicación Flask junto con los endpoints y funciones necesarias"""

    app = Flask(__name__, static_folder=Config.STATIC_FOLDER,
                template_folder=Config.TEMPLATE_FOLDER)

    app.config.from_object(Config)

    @app.route('/product/<int:product_id>', methods=['GET'])
    def get_product(product_id):
        return ProductController.get_product(product_id)

    return app
