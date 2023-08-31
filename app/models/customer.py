from ..database import DatabaseConnection

class Customer:
    def __init__(self, customer_id = None, first_name = None, last_name = None, email = None, phone = None, state = None, street = None, zip_code = None, city = None):
        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.state = state
        self.street = street
        self.zip_code = zip_code
        self.city = city

    @classmethod
    def get_customer(self, customer_id):
        try:
            query = """SELECT SCU.customer_id, SCU.first_name, SCU.last_name, SCU.phone, SCU.email, SCU.street, SCU.city, SCU.state, SCU.zip_code FROM sales.customers AS SCU WHERE SCU.customer_id = %s;"""
            params = (customer_id,)
            result = DatabaseConnection.fetch_one(query, params)
            if result is not None:
                return Customer(
                    customer_id= customer_id,
                    first_name= result[1],
                    phone= result[3],
                    state= result[7],
                    last_name= result[2],
                    street= result[5],
                    email= result[4],
                    zip_code= result[8],
                    city= result[6])
            else:
                return None
        except Exception as e:
            return {"Error": e}
        finally:
            DatabaseConnection.close_connection()
        
    @classmethod
    def get_customers(self, state):
        try:
            query = """SELECT SCU.customer_id, SCU.first_name, SCU.last_name, SCU.phone, SCU.email, SCU.street, SCU.city, SCU.state, SCU.zip_code FROM sales.customers AS SCU WHERE SCU.state LIKE %s;"""
            params = ("%" + state + "%",)
            results = DatabaseConnection.fetch_all(query, params)
            return results
        except Exception as e:
            return {"Error": e}
        finally:
            DatabaseConnection.close_connection()

    @classmethod
    def add_customer(self, first_name, last_name, email, phone, street, city, state, zip_code):
        try:
            query = """INSERT INTO sales.customers (first_name, last_name, email, phone, street, city, state, zip_code)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s);"""
            params = (first_name, last_name, email, phone, street, city, state, zip_code)
            DatabaseConnection.execute_query(query, params)
        except Exception as e:
            return {"Error": e}
        finally:
            DatabaseConnection.close_connection()

    @classmethod
    def del_customer(self, customer_id):
        try:
            query = "DELETE FROM sales.customers WHERE customer_id = %s;"

            params = customer_id,

            DatabaseConnection.execute_query(query, params)
        except Exception as e:
            return {"Error": e}
        finally:
            DatabaseConnection.close_connection()