from flask import jsonify, request
from ..models.customer import Customer

class CustomerController:

    # Ejercicio 1.1
    @classmethod
    def get_customer(cls, customer_id):
        customer_result = Customer.get_customer(customer_id)
        print(customer_result)
        if customer_result:
            customer = {
                "customer_id": customer_result[0],
                "first_name": customer_result[1],
                "last_name": customer_result[2],
                "email": customer_result[4],
                "phone": customer_result[3],
                "street": customer_result[5],
                "city": customer_result[6],
                "state": customer_result[7],
                "zip_code": customer_result[8]
                }
            return jsonify(customer), 200
        else:
            return jsonify({"message": "Cliente no encontrado"}), 404
    
    # Ejercicio 1.2
    @classmethod
    def get_customers(cls):
        state = request.args.get('state', '')
        customer_model = Customer()
        results = customer_model.get_customers(state)

        if results:
            customers = []
            for row in results:
                customer = {
                    "customer_id": row[0],
                    "first_name": row[1],
                    "last_name": row[2],
                    "email": row[3],
                    "phone": row[4],
                    "street": row[5],
                    "city": row[6],
                    "state": row[7],
                    "zip_code": row[8]
                }
                customers.append(customer)

            response_data = {
                "customers": customers,
                "total": len(customers)
            }
            return jsonify(response_data), 200
        else:
            return jsonify({"customers": [], "total": 0}), 200
    
    # Ejercicio 1.3
    @classmethod
    def add_customer(cls):
        customer_data = request.args
        required_fields = ['first_name', 'last_name', 'email']
        # Verifica si todos los campos requeridos están presentes y no son cadenas vacías.
        for field in required_fields:
            if not customer_data.get(field):
                return jsonify({"error": f"El campo '{field}' es obligatorio"}), 400
        params = (
            customer_data.get('first_name'), 
            customer_data.get('last_name'),
            customer_data.get('email'),
            customer_data.get('phone'),
            customer_data.get('street'),
            customer_data.get('city'),
            customer_data.get('state'),
            customer_data.get('zip_code')
        )
        Customer.add_customer(params)
        return jsonify({}), 201
    
    # Ejercicio 1.4
    @classmethod
    def upd_customer(cls, customer_id):
        customer_data = request.args

        params = (
            customer_data.get('first_name'), 
            customer_data.get('last_name'),
            customer_data.get('email'),
            customer_data.get('phone'),
            customer_data.get('street'),
            customer_data.get('city'),
            customer_data.get('state'),
            customer_data.get('zip_code'),
            customer_id
        )
        Customer.upd_customer(params)
        return jsonify({}), 201
    
    # Ejercicio 1.5
    @classmethod
    def del_customer(cls, customer_id):
        try:
            Customer.del_customer(customer_id)

            return jsonify({}), 204
        except Exception as e:
            return {"Error": e}