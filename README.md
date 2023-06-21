# Product Management API

This is a RESTful API for managing products and product types. The project implements CRUD operations (Create, Read, Update, Delete) for products and product types.

## Requirements
Before using this project, make sure the following components are installed:

- Python 3.7 or higher
- pip - Python package manage

# Installation
```shell
git clone https://github.com/your_username/product-management-api.git
cd product-management-api
pip install -r requirements.txt
```
# Running the server
```shell
uvicorn main:app --reload
```

# Using the API
You can use any HTTP client such as curl or Postman, or simply use a web browser to interact with the API.

Here are some examples of API requests:

- Get all product types: GET /product_types/
- Create a new product type: POST /product_types/
- Get product type by ID: GET /product_types/{product_type_id}
- Update product type: PUT /product_types/{product_type_id}
- Delete product type: DELETE /product_types/{product_type_id}
- Get all products: GET /products/
- Create a new product: POST /products/
- Get product by ID: GET /products/{product_id}
- Update product: PUT /products/{product_id}
- Delete product: DELETE /products/{product_id}
