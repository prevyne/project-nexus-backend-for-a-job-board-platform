# Project Nexus Job Board Platform - Backend API

This repository contains the backend service for a Job Board Platform. It provides a RESTful API for managing job postings, categories, and user authentication, built with Django and Django Rest Framework.

## Key Features

* **Job Management**: Full CRUD (Create, Read, Update, Delete) operations for job postings.
* **Categorization**: Ability to create and assign categories to jobs.
* **Role-Based Access Control**: Differentiates between Admins (full access) and Users (read-only access).
* **Optimized Search**: Indexed database fields for efficient filtering by location and category.
* **API Documentation**: Interactive API documentation powered by Swagger UI.

## Technologies Used

* **Backend**: Django, Django Rest Framework
* **Database**: PostgreSQL
* **Authentication**: JSON Web Tokens (JWT)
* **API Documentation**: drf-yasg (Swagger)

## Project Setup

To get a local copy up and running, follow these steps.

### Prerequisites

* Python 3.8+
* PostgreSQL installed and running.

### Installation

1.  **Clone the repository:**
    ```sh
    git clone https://github.com/prevyne/project-nexus-backend-for-a-job-board-platform.git
    cd project-nexus-backend-for-a-job-board-platform
    ```

2.  **Create and activate a virtual environment:**
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install the dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

4.  **Set up the database:**
    Connect to PostgreSQL and create a database and user for the project.
    ```sql
    CREATE DATABASE job_board_db;
    CREATE USER job_board_user WITH PASSWORD 'your_password';
    GRANT ALL PRIVILEGES ON DATABASE job_board_db TO job_board_user;
    ```

5.  **Configure environment settings:**
    Update the `DATABASES` setting in `job_board/settings.py` with your database credentials.

6.  **Run database migrations:**
    ```sh
    python manage.py migrate
    ```

7.  **Create a superuser:**
    This account will have the 'admin' role.
    ```sh
    python manage.py createsuperuser
    ```

8.  **Run the development server:**
    ```sh
    python manage.py runserver
    ```
    The API will be available at `http://127.0.0.1:8000/`.

## API Usage

The primary source for API endpoint details is the interactive Swagger documentation.

* **API Documentation**: `http://127.0.0.1:8000/api/docs/`

### Authentication

The API uses JWT for authentication. To access protected endpoints, you must first obtain an access token.

1.  **Register a user** at the `/api/register/` endpoint.
2.  **Obtain a token** by sending a POST request with your `username` and `password` to `/api/token/`.
3.  **Include the token** in the `Authorization` header for all subsequent requests to protected endpoints.
    ```
    Authorization: Bearer <your_access_token>
    ```