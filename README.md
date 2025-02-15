# Django Authentication API

This project implements a Django-based authentication system with cookie-based authentication, user registration, login, and protected endpoints. It also includes Swagger API documentation.

## Features
- User registration with email and password.
- OTP verification for registration.
- User login with email and password.
- Protected endpoint to retrieve logged-in user details.
- Logout functionality.
- Swagger API documentation.

## Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/krishpranav/api_task.git
cd api_task
```

### 2. Set Up a Virtual Environment
```bash
python3 -m venv venv
```

- **On macOS/Linux**:
```bash
source venv/bin/activate
```

- **On Windows**:
```bash
venv\Scripts\activate
```

### 3. Install Dependencies
```bash
python3 -m pip install -r requirements.txt
```

### 4. Run Migrations
```bash
python3 manage.py migrate
```

### 5. Run the Development Server
```bash
python3 manage.py runserver
```

### 7. Access the Application
- **Swagger UI**: Open `http://127.0.0.1:8000/swagger/` to explore and test the API.

## API Endpoints
- **POST /api/register/**: Register a new user.
- **POST /api/register/verify/**: Verify OTP for registration.
- **POST /api/login/**: Log in a user.
- **GET /api/me/**: Retrieve details of the logged-in user.
- **POST /api/logout/**: Log out the user.
