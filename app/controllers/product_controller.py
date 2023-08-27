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
            return {"msg": "No se encontro el producto"}
        
    @classmethod
    def get_products(cls, brand_name, category_name):
        product_model = Product()
        results = product_model.get_products(brand_name, category_name)
        product_list = []
        if len(results) > 0:
            for result in results:
                product_list.append({
                    "brand": {
                        "brand_id": result[4],
                        "brand_name": result[5]},
                    "category": {
                        "category_id": result[6],
                        "category_name": result[7]},
                    "list_price": result[3],
                    "model_year": result[2],
                    "product_id": result[0],
                    "product_name": result[1]
                })
            return jsonify({"products": product_list, "total": len(product_list)}), 200   
        else:
            return jsonify({"Mensaje": "No se encontraron coincidencias"}), 404