from flask import jsonify
from ..models.product import Product

class ProductController:
    @classmethod
    def get_product(cls, product_id):
        product_instance = Product.get_product(product_id)

        if product_instance:
            response = {
                "brand": {
                    "brand_id": product_instance.brand_id,
                    "brand_name": product_instance.brand_name},
                "category": {
                    "category_id": product_instance.category_id,
                    "category_name": product_instance.category_name},
                "list_price": product_instance.list_price,
                "model_year": product_instance.model_year,
                "product_id": product_instance.product_id,
                "product_name": product_instance.product_name
            }
            return jsonify(response), 200
        else:
            return {"msg": "No se encontron el producto"}