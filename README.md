pip install fastapi uvicorn sqlalchemy psycopg2-binary python-dotenv



python -m uvicorn app.main:app --reload


Public

GET /products

GET /products/{id}

POST /analytics/product-view/{id}

POST /analytics/enquiry-click/{id}

Admin

POST /auth/login

POST /products

PUT /products/{id}

DELETE /products/{id}

POST /products/{id}/image