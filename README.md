# Student Portfolio

Student Portfolio is a full-stack web application with role-based login (admin/viewer), built with FastAPI + MariaDB on the backend and Nuxt on the frontend.

## Project Structure

- backend: FastAPI API, database models, authentication
- frontend/student-port: Nuxt application (pages, middleware, composables)

## Features

- Login with JWT token
- Role-based authorization (admin, viewer)
- User management (admin)
- Viewer dashboard
- API documentation via Swagger

## Run Locally

### 1) Backend

- Open terminal in backend
- Create and activate virtual environment
- Install dependencies
- Start API server

Example commands:

```powershell
cd backend
pip install -r requirements.txt
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

Backend URL:

- http://localhost:8000
- Swagger: http://localhost:8000/docs

### 2) Frontend

- Open terminal in frontend/student-port
- Install dependencies
- Start Nuxt dev server

Example commands:

```powershell
cd frontend/student-port
npm install
npm run dev
```

Frontend URL:

- http://localhost:3000

## API Summary

- POST /api/register: Create user
- POST /api/login: Login and get token
- GET /api/users/me: Current user profile
- GET /api/items/: List items (authenticated)
- GET /api/users/: List users (admin)
- DELETE /api/users/{user_id}: Delete user (admin)

## Notes

- Update SECRET_KEY in backend/main.py before production.
- Ensure database schema matches backend models.
- If login fails, check backend logs and browser Network tab for response details.
