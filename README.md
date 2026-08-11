**FastAPI + MongoDB**
A comprehensive RESTful API for managing library student records, built with FastAPI and MongoDB Atlas. This API provides full CRUD (Create, Read, Update, Delete) operations for student management.

Live Demo
API URL: https://fastapi-ls5i.onrender.com/

Interactive Docs: https://fastapi-ls5i.onrender.com/docs

Alternative Docs: https://fastapi-ls5i.onrender.com/redoc

Features
Create - Add new students to the library database

List - Retrieve all students with optional filtering

Retrieve - Get specific student details by ID

Update - Partially update student information (PATCH)

Delete - Remove students from the database

Data Validation - Automatic request validation using Pydantic

MongoDB Atlas - Cloud-hosted NoSQL database

Auto-generated Documentation - Interactive Swagger UI and ReDoc

CORS Ready - Cross-Origin Resource Sharing enabled

Tech Stack
Technology	Purpose
FastAPI	Modern Python web framework
MongoDB Atlas	Cloud NoSQL database
PyMongo	MongoDB driver for Python
Uvicorn	ASGI server for FastAPI
Gunicorn	Production WSGI server
Pydantic	Data validation

API Endpoints
Base URL: /
1. Create a Student
Endpoint: POST /students
Status Code: 201 Created

2. List All Students
Endpoint: GET /students
Status Code: 200 OK

3. Get a Student by ID
Endpoint: GET /students/{id}
Status Code: 200 OK

4. Update a Student
Endpoint: PATCH /students/{id}
Status Code: 204 No Content

5. Delete a Student
Endpoint: DELETE /students/{id}
Status Code: 200 OK

**Run the Application**

uvicorn main:app --reload

**Access the API**

API: https://fastapi-ls5i.onrender.com/

Swagger Docs: https://fastapi-ls5i.onrender.com/docs

ReDoc: https://fastapi-ls5i.onrender.com/redoc

