## Grocery Store Management System

A web-based Grocery Store Management System built using **Python, Flask, MySQL, HTML, CSS, JavaScript, jQuery, and Bootstrap**. This application helps manage grocery products, units of measurement, and customer orders through a simple and user-friendly interface.

## Overview

The Grocery Store Management System is designed to simplify everyday grocery store operations. It provides a centralized way to manage product information, maintain pricing details, and record customer orders along with their corresponding order items.

The backend uses Flask to expose REST-style HTTP endpoints, while MySQL stores product and order information in a relational database.

##  Features

- **Product Management**
  - Add new grocery products.
  - View available products and their prices.
  - Associate products with units of measurement.
  - Handle deletion requests while preserving existing order references.

- **Order Management**
  - Record customer names and order dates.
  - Add multiple products to an order.
  - Store product quantities and individual line totals.
  - Calculate and save the overall order total.
  - Maintain relationships between orders and their details.

- **Unit of Measurement Management**
  - Retrieve available units of measurement.
  - Associate products with the appropriate units.

- **Database Management**
  - Store data in MySQL.
  - Use primary and foreign keys to maintain relationships.
  - Use parameterized SQL queries for database operations.

- **User Interface**
  - Web-based interface using HTML, CSS, JavaScript, jQuery, and Bootstrap.
  - AJAX requests for communication between the frontend and Flask backend.

##  Tech Stack

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Flask | Web application and API endpoints |
| MySQL | Relational database |
| mysql-connector-python | Python–MySQL connectivity |
| HTML5 | Page structure |
| CSS3 | Styling |
| JavaScript | Frontend functionality |
| jQuery | AJAX requests and DOM manipulation |
| Bootstrap | Responsive UI components |
| Flask-CORS | Cross-origin request support |

##  Project Structure

```text
grocery-store-management/
│
├── backend/
│   ├── server.py
│   ├── products_dao.py
│   ├── orders_dao.py
│   ├── uom_dao.py
│   └── sql_connection.py
│
├── ui/
│   ├── index.html
│   ├── manage-product.html
│   ├── order.html
│   ├── css/
│   └── js/
│       └── custom/
│           ├── common.js
│           ├── manage-product.js
│           └── order.js
│
├── README.md
```

##  API Endpoints

The following endpoints are present in the Flask backend.

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Displays the application welcome page |
| GET | `/getUOM` | Retrieves units of measurement |
| GET | `/getProducts` | Retrieves product information |
| POST | `/insertProduct` | Adds a product |
| POST | `/deleteProduct` | Deletes a product when permitted by database constraints |
| POST | `/insertOrder` | Creates an order and its associated order details |

##  Testing

You can test the application by following these steps:

1. Start the MySQL server.
2. Start the Flask backend.
3. Open the frontend.
4. Add a product with a valid unit and price.
5. Verify that the product appears in the product list.
6. Create an order with one or more products.
7. Verify that the order and its details are stored in MySQL.
8. Try deleting a product that has already been used in an order and confirm that the application handles the foreign key restriction appropriately.


##  Future Improvements

- Product search, filtering, and category management.
- Product stock and inventory tracking.
- Update and edit product functionality.
- Soft deletion for discontinued products.
- Sales reports and revenue analytics.
- User authentication and role-based access control.
- Improved input validation and automated tests.
- Deployment to a cloud hosting platform.

##  Learning Outcomes

This project demonstrates practical experience with:

- Building a Python web application using Flask.
- Connecting a backend application to a MySQL database.
- Designing relational tables and foreign key relationships.
- Implementing CRUD-style product operations.
- Handling parent-child relationships in order processing.
- Connecting a frontend to a backend using AJAX.
- Managing database transactions and integrity constraints.


---

*Built as a hands-on project to explore database-driven web application development and grocery store operations.*
