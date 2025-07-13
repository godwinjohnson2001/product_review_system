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
