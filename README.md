# product_review_system
A RESTful API for a *Product Review System* built with Django and Django REST Framework.

##  Features

-  Role-based Authentication (Admin and Regular Users)
-  Admins can manage products (add/edit/delete)
-  Regular users can view products and submit one review per product
-  Reviews include ratings (1–5) and feedback
-  Aggregated average product ratings
-  Token-based Authentication using DRF
---

## ⚙ Tech Stack

- Python 3.11+
- Django 4.x
- Django REST Framework
- SQLite (default, can be changed)
- Token Authentication
---
---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/godwinjohnson2001/product_review_system.git
cd product-review-system
```
### 2. Create a Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # On Windows
# source venv/bin/activate  # On Mac/Linux
```
### 3.  Install Dependencies
```bash
pip install -r requirements.txt
```
### 4.  Apply Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```
### 5. Create a Superuser (Admin)
```bash
python manage.py createsuperuser
```
### 6. Run the Server
```bash
python manage.py runserver
```
## API Authentication
Uses Token Authentication. After login, include the token in the header for protected endpoints:

Authorization: Token your_token_here

## API Endpoints
### User Endpoints
Method	       Endpoint	         Description

POST	       /api/register/	    Register new user
POST	       /api/login/	      Login and get token

###  Product Endpoints
Method	        Endpoint	                    Description	                            Permission

GET	         /api/products/	              List all products	                           All users
GET	         /api/products/<id>/	        Get product detail + avg rating	             All users
POST	       /api/products/	              Create product	                             Admin only
PUT	        /api/products/<id>/	          Update product	                             Admin only
DELETE	     /api/products/<id>/	        Delete product	                             Admin only

### Review Endpoints
Method        	Endpoint	                     Description	                        Permission

POST	      /api/products/<id>/review/	    Submit review for a product	           Authenticated users
GET	       /api/products/<id>/reviews/     	List all reviews for a product	         All users

## Postman Testing
### 1. Register a user
POST /api/register/
```json
{
  "username": "john",
  "password": "password123",
  "is_admin": false
}
```
### 2.  Login:
POST /api/login/
```json
{
  "token": "your_generated_token"
}
```
### 3. Use the token in headers for authenticated requests:
Authorization: Token your_generated_token





