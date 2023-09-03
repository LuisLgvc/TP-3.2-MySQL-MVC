from flask import jsonify, request
from ..models.product import Product

class ProductController:
    # Ejercicio 2.1
    @classmethod
    def get_product(cls, product_id):
        product_instance = Product.get_product(int(product_id))

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
            return response, 200
        else:
            return {"msg": "No se encontro el producto"}
    
    # Ejercicio 2.2
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
        
    # Ejercicio 2.3
    @classmethod
    def add_product(cls):
        try:
            product_name = request.args.get('product_name', '')
            brand_id = request.args.get('brand_id', '')
            category_id = request.args.get('category_id', '')
            model_year = request.args.get('model_year', '')
            list_price = request.args.get('list_price', '')

            Product.add_product(product_name, brand_id, category_id, model_year, list_price)

            return jsonify({}), 201
        except Exception as e:
            return {"Error": e}
    
    # Ejercicio 2.4
    @classmethod
    def upd_product(cls, product_id):
        try:
            product_name = request.args.get('product_name', '')
            brand_id = request.args.get('brand_id', '')
            category_id = request.args.get('category_id', '')
            model_year = request.args.get('model_year', '')
            list_price = request.args.get('list_price', '')

            Product.upd_product(product_id, product_name, brand_id, category_id, model_year, list_price)
            
            return jsonify({}), 201
        except Exception as e:
            return {"Error": e}
    
    # Ejercicio 2.5
    @classmethod
    def del_product(cls, product_id):
        try:
            Product.del_product(product_id)

            return jsonify({}), 204
        except Exception as e:
            return {"Error": e}