from sql_connection import get_sql_connection

def get_all_products(connection): 
    cursor = connection.cursor()

    query = ("select products.product_id, products.name, products.uom_id, products.price_per_unit, uom.uom_name from products inner join uom on products.uom_id=uom.uom_id")

    cursor.execute(query)

    response = []
    for(product_id,name,uom_id,price_per_unit,uom_name) in cursor:
        response.append({
            'product_id': product_id,
            'name': name,
            'uom_id': uom_id,
            'price_per_unit': price_per_unit,
            'uom_name': uom_name
        })
        
    return response
    

def insert_new_product(connection, product):
    cursor = connection.cursor()

    try:
        name = product.get('product_name')
        uom_id = product.get('uom_id')
        price = product.get('price_per_unit')

        if not name or not str(name).strip():
            raise ValueError("Product name is required.")

        if uom_id in (None, ''):
            raise ValueError("Please select a unit.")

        price = float(price)

        if price <= 0:
            raise ValueError("Price must be greater than zero.")

        query = """
            INSERT INTO products (name, uom_id, price_per_unit)
            VALUES (%s, %s, %s)
        """

        cursor.execute(query, (name.strip(), int(uom_id), price))
        connection.commit()

        return cursor.lastrowid

    except Exception:
        connection.rollback()
        raise

    finally:
        cursor.close()



def delete_product(connection, product_id):
    cursor = connection.cursor()

    try:
        query = "DELETE FROM products WHERE product_id = %s"
        cursor.execute(query, (int(product_id),))
        deleted_rows = cursor.rowcount

        connection.commit()
        return deleted_rows

    except Exception:
        connection.rollback()
        raise

    finally:
        cursor.close()

    
    return cursor.lastrowid

def edit_product(connection,product_id,product):
    cursor = connection.cursor()
    #query = ("UPDATE products SET ")
    pass

if __name__ == '__main__':
    connection = get_sql_connection()
    #print(get_all_products(connection))
    #product = {
    #    'product_name':'milk',
    #    'uom_id':'1',
    #    'price_per_unit':'35'
    #}
    #insert_new_product(connection,product)
    #delete_product(connection,2)
    #print(get_all_products(connection))