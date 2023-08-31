from flask import request, Flask, jsonify
from config import Config
from app.database import DatabaseConnection
from .models.product import Product
from .models.customer import Customer
from .controllers.product_controller import ProductController
from .controllers.customer_controller import CustomerController


def ejercicios_mysql():
    """Crea y configura la aplicación Flask junto con los endpoints y funciones necesarias"""

    app = Flask(__name__, static_folder=Config.STATIC_FOLDER,
                template_folder=Config.TEMPLATE_FOLDER)

    app.config.from_object(Config)

    @app.route('/customer/<int:customer_id>', methods=['GET'])
    def get_customer(customer_id):
        return CustomerController.get_customer(customer_id)
    
    @app.route('/customers', methods=['GET'])
    def get_customers():
        return CustomerController.get_customers()

    @app.route('/customers', methods=['POST'])
    def add_customer():
        return CustomerController.add_customer()
    
    @app.route('/customer/<int:customer_id>', methods=['DELETE'])
    def del_customer(customer_id):
        return CustomerController.del_customer(customer_id)
    
    @app.route('/product/<int:product_id>', methods=['GET'])
    def get_product(product_id):
        return ProductController.get_product(product_id)
    
    @app.route('/products/<string:brand_name>/<string:category_name>', methods=['GET'])
    def get_products(brand_name, category_name):
        return ProductController.get_products(brand_name, category_name)

    @app.route('/addproduct', methods=['POST'])
    def add_product():
        return ProductController.add_product()
    
    @app.route('/updproduct/<int:product_id>', methods=['PUT'])
    def upd_product(product_id):
        return ProductController.upd_product(product_id)
    
    @app.route('/delproduct/<int:product_id>', methods=['DELETE'])
    def del_product(product_id):
        return ProductController.del_product(product_id)

    return app
