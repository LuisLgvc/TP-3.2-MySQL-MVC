from flask import request, Flask, jsonify
from config import Config
from app.database import DatabaseConnection
from .models.product import Product


def ejercicios_mysql():
    """Crea y configura la aplicación Flask junto con los endpoints y funciones necesarias"""

    app = Flask(__name__, static_folder=Config.STATIC_FOLDER,
                template_folder=Config.TEMPLATE_FOLDER)

    app.config.from_object(Config)

    @app.route('/product', methods=['GET'])
    def obtener_producto():
        product = Product(
            product_id= request.args.get('product_id', '')
        )
        Product.get_product(product)

        return "Exito"

    return app
