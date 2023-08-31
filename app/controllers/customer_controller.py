from flask import jsonify, request
from ..models.customer import Customer

class CustomerController:
    @classmethod
    def get_customer(cls, customer_id):
        customer_instance = Customer.get_customer(customer_id)
        if customer_instance:
            response = {
                "city": customer_instance.city,
                "customer_id": customer_instance.customer_id,
                "email": customer_instance.email,
                "first_name": customer_instance.first_name,
                "last_name": customer_instance.last_name,
                "phone": customer_instance.phone,
                "state": customer_instance.state,
                "street": customer_instance.street,
                "zip_code": customer_instance.zip_code
            }
            return jsonify(response), 200
        else:
            return {"msg": "No se encontro el producto"}
        
    @classmethod
    def get_customers(cls):
        state = request.args.get('state', '')
        customer_model = Customer()
        results = customer_model.get_customers(state)

        if len(results) > 0:
            return jsonify({
                 "customers": [
                    {
                        "city": customer[6],
                        "customer_id": customer[0],
                        "email": customer[4],
                        "first_name": customer[1],
                        "last_name": customer[2],
                        "phone": customer[3],
                        "state": customer[7],
                        "street": customer[5],
                        "zip_code": customer[8]
                    }
                    for customer in results
                ],
                "total": len(results)
            }), 200
        else:
            return jsonify({"Mensaje": "No se encontraron coincidencias"}), 404
        
    @classmethod
    def add_customer(cls):
        try:
            data = request.args
            first_name = data.get('first_name', '')
            last_name = data.get('last_name', '')
            email = data.get('email', '')
            phone = data.get('phone', '')
            street = data.get('street', '')
            city = data.get('city', '')
            state = data.get('state', '')
            zip_code = data.get('zip_code', '')

            Customer.add_customer(first_name, last_name, email, phone, street, city, state, zip_code)

            return jsonify({}), 201
        except Exception as e:
            return {"Error": e}
        
    @classmethod
    def del_customer(cls, customer_id):
        try:
            Customer.del_customer(customer_id)

            return jsonify({}), 204
        except Exception as e:
            return {"Error": e}