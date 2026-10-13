from sql_connection import get_sql_connection

def get_all_orders(connection):
    cursor = connection.cursor()
    
    query = ("SELECT * FROM orders")
    
    
    cursor.execute(query)
    
    response = []
    
    for (order_id,customer_name,total,datetime) in cursor:
        response.append({
            'order_id':order_id,
            'customer_name':customer_name,
            'total':total, 
            'datetime':datetime
        })
        
    return response


if __name__ == '__main__':
    connection = get_sql_connection()
    print(get_all_orders(connection))
    
    