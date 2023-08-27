from ..database import DatabaseConnection

class Product:
    def __init__(self, product_id = None, product_name = None, brand_id = None, category_id = None, model_year = None, list_price = None):
        self.product_id = product_id
        self.product_name = product_name
        self.brand_id = brand_id
        self.category_id = category_id
        self.model_year = model_year
        self.list_price = list_price

    @classmethod
    def get_product(product):
        try:
            query = """SELECT * FROM production.products AS PRP INNER JOIN production.brands AS PRD ON PRP.brand_id = PRD.brand_id INNER JOIN production.categories AS PRC ON PRP.category_id = PRC.category_id WHERE PRP.product_id = %s;"""
            params = product.product_id,
            result = DatabaseConnection.fetch_one(query, params)
            if result is not None:
                return {
                    "brand": {
                        "brand_id": result[6],
                        "brand_name": result[7]},
                    "category": {
                        "category_id": result[8],
                        "category_name": result[9]},
                    "list_price": result[5],
                    "model_year": result[4],
                    "product_id": result[0],
                    "product_name": result[1]
                }, 200
            else:
                return {"msg": "No se encontro el producto"}, 404
        except:
            return {'Error': 'Ha ocurrido un erorr'}, 400
        finally:
            DatabaseConnection.close_connection()