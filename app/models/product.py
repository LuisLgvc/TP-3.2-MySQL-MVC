from ..database import DatabaseConnection

class Product:
    def __init__(self, product_id = None, product_name = None, brand_id = None, category_id = None, model_year = None, list_price = None, brand_name = None, category_name = None):
        self.product_id = product_id
        self.product_name = product_name
        self.brand_id = brand_id
        self.category_id = category_id
        self.model_year = model_year
        self.list_price = list_price
        self.brand_name = brand_name
        self.category_name = category_name

    @classmethod
    def get_product(self, product_id):
        query = """SELECT PRP.product_id, PRP.product_name, PRP.model_year, PRP.list_price, PRP.brand_id, PRD.brand_name, PRP.category_id, PRC.category_name FROM production.products AS PRP INNER JOIN production.brands AS PRD ON PRP.brand_id = PRD.brand_id INNER JOIN production.categories AS PRC ON PRP.category_id = PRC.category_id WHERE PRP.product_id = %s;"""
        params = (product_id,)
        result = DatabaseConnection.fetch_one(query, params)
        if result is not None:
            return Product(
                product_id= product_id,
                product_name= result[1],
                model_year= result[2],
                list_price= result[3],
                brand_id= result[4],
                brand_name= result[5],
                category_id= result[6],
                category_name= result[7]
            )
        else:
            return None