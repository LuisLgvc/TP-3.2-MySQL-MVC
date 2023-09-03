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

    # Ejercicio 1.1
    @classmethod
    def get_customer(self, customer_id):
        try:
            query = "SELECT * FROM sales.customers WHERE customer_id = %s"
            params = (customer_id,)
            
            result = DatabaseConnection.fetch_one(query, params)
            return result
        except Exception as e:
            return {"Error": e}
        finally:
            DatabaseConnection.close_connection()
    
    # Ejercicio 1.2
    @classmethod
    def get_customers(self, state):
        try:
            query = "SELECT * FROM sales.customers WHERE state = %s"
            params = (state,)
            results = DatabaseConnection.fetch_all(query, params)
            return results
        except Exception as e:
            return {"Error": e}
        finally:
            DatabaseConnection.close_connection()

    # Ejercicio 1.3
    @classmethod
    def add_customer(self, params):
        try:
            query = """INSERT INTO sales.customers (first_name, last_name, email, phone, street, city, state, zip_code) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
            DatabaseConnection.execute_query(query, params)
        except Exception as e:
            return {"Error": e}
        finally:
            DatabaseConnection.close_connection()

    # Ejercicio 1.4
    @classmethod
    def upd_customer(self, params):
        try:
            query = """UPDATE sales.customers SET first_name = %s, last_name = %s, email = %s, phone = %s, street = %s, city = %s, state = %s, zip_code = %s WHERE customer_id = %s"""
            DatabaseConnection.execute_query(query, params)
        except Exception as e:
            return {"Error": e}
        finally:
            DatabaseConnection.close_connection()

    # Ejercicio 1.5
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