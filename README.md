# LAB - Class 33

## Project: Authentication & Production Server

## Author: Abdallah Toughoj

## Setup

### .env requirements

- asgiref==3.7.2
- Django==4.2.3
- djangorestframework==3.14.0
- djangorestframework-simplejwt==5.2.2
- gunicorn==21.2.0
- packaging==23.1
- psycopg2-binary==2.9.6
- PyJWT==2.8.0
- pytz==2023.3
- sqlparse==0.4.4
- whitenoise==6.5.0

### How to initialize/run your application

- #### python manage.py runserver

### How to use your library (where applicable)

- docker-compose up

### How To Get Tokens:

#### HTTP Method: POST

#### Route: /api/token/

#### Token Required: No

### **Example Request (using ThunderClient):**

#### POST http://127.0.0.1:8000/api/token/

#### Content-Type: application/json

#### {

#### "username": "abdallah",

#### "password": "Abdallah2000"

#### }

### **Example Response:**

#### {

#### "access_token":

#### "YOUR_ACCESS_TOKEN",

#### "refresh_token":

#### "YOUR_REFRESH_TOKEN",

#### }

### How To Refresh Tokens :

#### HTTP Method: POST

#### Route: /refresh-tokens

#### Token Required: Yes

### **Example Request (using ThunderClient):**

#### POST http://127.0.0.1:8000/api/token/refresh/

#### Authorization: Bearer

#### YOUR_REFRESH_TOKEN

### **Example Response:**

#### {

#### "access_token":

#### "NEW_ACCESS_TOKEN",

#### "expires_in": 3600

#### }
