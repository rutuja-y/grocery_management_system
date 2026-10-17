from flask import Flask, jsonify, request
from flask_cors import CORS
import mysql.connector
import json

import products_dao
import orders_dao
import uom_dao
from sql_connection import get_sql_connection

app = Flask(__name__)
CORS(app)

connection = get_sql_connection()

@app.route("/")
def home():
    return "<h1>Grocery Store Management System</h1>"

@app.route("/getUOM",methods=['GET'])
def get_uom():
    response = uom_dao.get_uoms(connection)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

@app.route("/getAllOrders",methods=['GET'])
def get_all_orders():
    response = orders_dao.get_all_orders(connection)
    response = jsonify(response)
    return response
    
@app.route("/getProducts",methods=['GET'])
def get_products():
    response = products_dao.get_all_products(connection)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin','*')
    return response


@app.route("/deleteProduct", methods=['POST'])
def delete_products():
    try:
        product_id = request.form.get('product_id')

        if not product_id:
            return jsonify({
                'error': 'Product ID is required'
            }), 400

        deleted_rows = products_dao.delete_product(
            connection, product_id
        )

        if deleted_rows == 0:
            return jsonify({
                'error': 'Product not found'
            }), 404

        return jsonify({
            'success': True,
            'message': 'Product deleted successfully'
        })

    except mysql.connector.IntegrityError as e:
        connection.rollback()

        if e.errno == 1451:
            return jsonify({
                'error': (
                    'Cannot delete this product because it '
                    'is associated with existing orders. '
                    'Keep it to preserve order history.'
                )
            }), 409

        app.logger.exception("Integrity error deleting product")
        return jsonify({
            'error': 'A database constraint prevented deletion.'
        }), 500

    except (ValueError, TypeError):
        connection.rollback()
        return jsonify({
            'error': 'Invalid product ID.'
        }), 400

    except mysql.connector.Error:
        connection.rollback()
        app.logger.exception("Database error deleting product")
        return jsonify({
            'error': 'A database error occurred while deleting the product.'
        }), 500



@app.route("/insertOrder", methods=['POST'])
def insert_order():
    try:
        request_payload = json.loads(request.form['data'])

        order_id = orders_dao.insert_order(
            connection, request_payload
        )

        return jsonify({'order_id': order_id}), 201

    except mysql.connector.Error:
        connection.rollback()
        app.logger.exception("Error inserting order")
        return jsonify({
            'error': 'Database error while inserting order.'
        }), 500

    except (KeyError, ValueError, TypeError):
        connection.rollback()
        app.logger.exception("Invalid order request")
        return jsonify({
            'error': 'Invalid order data. Check the submitted fields.'
        }), 400


@app.route("/insertProduct",methods=['POST'])
def insert_product():
    request_payload = json.loads(request.form['data'])
    product_id = products_dao.insert_new_product(connection,request_payload)
    response = jsonify({'product_id':product_id})
    response.headers.add('Access-Control-Allow-Origin','*')
    return response
    

if __name__ == "__main__":
    print("Starting Python Flask Server For Grocery Store Management System")
    app.run(port=5000)