# 🚀 FastAPI Task Management System

A backend REST API for managing users and tasks, built with **FastAPI, SQLAlchemy, PostgreSQL, Pydantic, JWT Authentication, and Alembic**.

This project was built as a learning project to understand how modern Python backend applications are designed, authenticated, connected to databases, validated, and maintained.

The project focuses on building a practical Task Management API while learning important FastAPI and backend-development concepts.

---

## ✨ Features

### 👤 User Management

* User registration
* User login
* JWT-based authentication
* Secure password hashing
* Get user information
* Update user profile
* Update password
* Delete user
* Email validation

### 🔐 Authentication & Authorization

* JWT access tokens
* OAuth2 Bearer authentication
* Protected API routes
* Password hashing using Argon2
* Authentication dependencies
* Current-user dependency injection

### 📝 Task Management

* Create tasks
* Get all tasks
* Get a task by ID
* Update tasks
* Delete tasks
* Associate tasks with users
* Task ownership validation

### 🗄️ Database

* PostgreSQL
* SQLAlchemy ORM
* SQLAlchemy 2.x
* Alembic database migrations
* Relational data modelling

### 📚 API Documentation

FastAPI automatically provides interactive API documentation:

* Swagger UI
* ReDoc
* OpenAPI schema

---

## 🛠️ Tech Stack

| Technology        | Purpose                     |
| ----------------- | --------------------------- |
| Python            | Programming language        |
| FastAPI           | Backend web framework       |
| SQLAlchemy        | ORM / database interaction  |
| PostgreSQL        | Relational database         |
| Pydantic          | Request/response validation |
| Pydantic Settings | Configuration management    |
| JWT               | Authentication              |
| Argon2            | Password hashing            |
| Alembic           | Database migrations         |
| Uvicorn           | ASGI server                 |

---

## 📁 Project Structure

```text
FastAPI_Task_Management_System/
│
├── src/
│   ├── ...
│   └── ...
│
├── migrations/
│   └── ...
│
├── main.py
├── alembic.ini
├── migrate.bat
├── push.bat
├── requirements.txt
├── .gitignore
└── README.md
```

The application code is organized inside `src/`, while `migrations/` contains database migration history.

---

# ⚙️ Getting Started

## 1. Clone the repository

```bash
git clone https://github.com/pandeyaditya0022ee/FastAPI_Task_Management_System.git

cd FastAPI_Task_Management_System
```

## 2. Create a virtual environment

### Windows

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

# 🔐 Environment Variables

Create a `.env` file in the project root.

Example:

```env
DATABASE_URL=postgresql://username:password@localhost:5432/task_management

SECRET_KEY=your-secret-key

ALGORITHM=HS256

ACCESS_TOKEN_EXPIRE_MINUTES=30
```

> Never commit real credentials, database passwords, API keys, or JWT secrets to GitHub.

---

# 🗄️ Database Setup

Make sure PostgreSQL is running.

Create a database:

```sql
CREATE DATABASE task_management;
```

Configure the database connection in your `.env` file.

---

# 🔄 Database Migrations

This project uses **Alembic** for database schema migrations.

Create a migration after changing your SQLAlchemy models:

```bash
alembic revision --autogenerate -m "describe your changes"
```

Apply migrations:

```bash
alembic upgrade head
```

Rollback the latest migration:

```bash
alembic downgrade -1
```

Alembic allows the database schema to evolve without manually recreating the database.

---

# ▶️ Running the Application

Start the FastAPI server:

```bash
uvicorn main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

---

# 📚 API Documentation

Once the server is running:

### Swagger UI

```text
http://127.0.0.1:8000/docs
```

### ReDoc

```text
http://127.0.0.1:8000/redoc
```

FastAPI automatically generates these interfaces from the application's OpenAPI schema.

---

# 🔑 Authentication Flow

The API uses JWT Bearer authentication.

Typical authentication flow:

```text
Register
   │
   ▼
Login
   │
   ▼
JWT Access Token
   │
   ▼
Authorization: Bearer <token>
   │
   ▼
Protected API
```

Example HTTP header:

```http
Authorization: Bearer <access_token>
```

Protected endpoints use the authenticated user to determine which resources they are allowed to access.

---

# 📝 Task API

Typical task operations include:

```text
POST    /tasks
GET     /tasks
GET     /tasks/{task_id}
PATCH   /tasks/{task_id}
DELETE  /tasks/{task_id}
```

A task can contain information such as:

```json
{
    "title": "Learn FastAPI",
    "description": "Build a production-style REST API",
    "status": "pending"
}
```

---

# 🧠 What I Learned

This project is also a learning exercise covering:

* FastAPI routing
* Path parameters
* Query parameters
* Request bodies
* Pydantic schemas
* Response models
* Dependency Injection
* SQLAlchemy ORM
* PostgreSQL
* Database relationships
* JWT authentication
* Password hashing
* OAuth2 Bearer authentication
* Middleware
* Exception handling
* Environment variables
* Alembic migrations
* REST API design
* API documentation

---

# 🎯 Learning Goal

The goal of this project is not only to create a Task Management API, but to gradually understand how real-world FastAPI backend systems are designed.

The project will evolve from a simple CRUD API into a more complete backend application while introducing advanced backend concepts step by step.

---

# 👨‍💻 Author

**Aditya Pandey**

GitHub:

https://github.com/pandeyaditya0022ee

---

## ⭐ If you find this project useful

Feel free to fork the repository, experiment with the code, and build your own features.
