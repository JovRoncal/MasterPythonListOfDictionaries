product_list = [
    {"name": "Laptop", "category": "Electronics", "price": 750, "stock": 50, "supplier_email": "supplier1@gmail.com"},
    {"name": "Desk Chair", "category": "Furniture", "price": 100, "stock": 200, "supplier_email": "supplier2@gmail.com"},
    {"name": "Smartwatch", "category": "Electronics", "price": 200, "stock": 150, "supplier_email": "supplier3@gmail.com"},
    {"name": "Notebook", "category": "Stationery", "price": 55, "stock": 0, "supplier_email": "supplier4@gmail.com"},
    {"name": "Running Shoes", "category": "Apparel", "price": 80, "stock": 100, "supplier_email": "supplier5@gmail.com"}
]

# Printing product details
for product in product_list:
    print(f"Product Name: {product['name']}, Category: {product['category']}, Price: {product['price']}, Stock: {product['stock']}, Supplier Email: {product['supplier_email']}")