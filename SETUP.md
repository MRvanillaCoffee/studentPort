# Student Portfolio - Login & Role-Based Access System

A full-stack web application with login authentication and role-based access control (RBAC) supporting Admin and Viewer roles.

## Features

✅ **User Authentication** - Secure login with JWT tokens
✅ **Role-Based Access Control** - Admin and Viewer roles with different permissions
✅ **Admin Dashboard** - Manage users, view statistics, add/remove users
✅ **Viewer Dashboard** - View personal portfolio and profile
✅ **Database Integration** - MariaDB with SQLAlchemy ORM
✅ **Modern Frontend** - Nuxt 4 with Vue 3 and TypeScript
✅ **Password Hashing** - Bcrypt encryption for security
✅ **CORS Support** - Frontend-Backend communication

## Project Structure

```
studentPort/
├── backend/                 # Python FastAPI Backend
│   ├── main.py             # FastAPI app and routes
│   ├── models.py           # SQLAlchemy models
│   ├── schemas.py          # Pydantic schemas
│   ├── database.py         # Database configuration
│   ├── init_db.py          # Database initialization script
│   ├── requirements.txt    # Python dependencies
│   └── __init__.py
│
└── frontend/student-port/  # Nuxt.js Frontend
    ├── pages/              # Page components
    │   ├── index.vue       # Home page
    │   ├── login.vue       # Login page
    │   ├── register.vue    # Registration page
    │   ├── admin/
    │   │   └── index.vue   # Admin dashboard
    │   └── viewer/
    │       └── index.vue   # Viewer dashboard
    ├── composables/        # Vue composables
    │   └── useAuth.ts      # Authentication composable
    ├── middleware/         # Route middleware
    │   └── auth.ts         # Authentication middleware
    ├── nuxt.config.ts      # Nuxt configuration
    ├── package.json        # Node dependencies
    └── tsconfig.json       # TypeScript configuration
```

## Backend Setup

### Prerequisites
- Python 3.8+
- MariaDB/MySQL Server running

### Installation

1. **Navigate to backend directory:**
   ```bash
   cd backend
   ```

2. **Create virtual environment:**
   ```bash
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Update database configuration** in `database.py`:
   ```python
   SQLALCHEMY_DATABASE_URL = "mariadb+mariadbconnector://root:your_password@localhost:3306/cit_curriculum"
   ```

5. **Initialize database with default users:**
   ```bash
   python init_db.py
   ```
   
   This creates:
   - Admin user: `admin` / `password123`
   - Viewer user: `viewer` / `password123`

6. **Run the backend server:**
   ```bash
   uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```

   The API will be available at `http://localhost:8000`
   - API docs: `http://localhost:8000/docs`
   - ReDoc: `http://localhost:8000/redoc`

## Frontend Setup

### Prerequisites
- Node.js 16+ and npm

### Installation

1. **Navigate to frontend directory:**
   ```bash
   cd frontend/student-port
   ```

2. **Install dependencies:**
   ```bash
   npm install
   ```

3. **Run development server:**
   ```bash
   npm run dev
   ```

   The frontend will be available at `http://localhost:3000`

## API Endpoints

### Authentication

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/register` | Register new user |
| POST | `/api/login` | Login and get JWT token |
| GET | `/api/users/me` | Get current user info |

### Users

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/items/` | Get all items |

### Example Login Request

```bash
curl -X POST http://localhost:8000/api/login \
  -H "Content-Type: application/json" \
  -d '{"username":"admin","password":"password123"}'
```

### Example Response

```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer",
  "user": {
    "id": 1,
    "username": "admin",
    "email": "admin@studentport.com",
    "role": "admin",
    "created_at": "2024-01-15T10:30:00"
  }
}
```

## Default Credentials

| Role | Username | Password |
|------|----------|----------|
| Admin | admin | password123 |
| Viewer | viewer | password123 |

⚠️ **Important:** Change these credentials in production!

## User Roles

### Admin Role
- Access to admin dashboard
- View all users statistics
- Create new users
- Delete users
- Change user roles

### Viewer Role
- Access to viewer dashboard
- View personal profile
- View portfolio items
- View own information only

## Security Features

1. **Password Hashing**: Bcrypt encryption with salt
2. **JWT Tokens**: Secure token-based authentication
3. **Role-Based Access Control**: Middleware-based route protection
4. **CORS**: Configured for frontend-backend communication
5. **HTTP-only Cookies**: Token stored securely (optional enhancement)

## Database Schema

### Users Table

```sql
CREATE TABLE users (
  id INT PRIMARY KEY AUTO_INCREMENT,
  username VARCHAR(50) UNIQUE NOT NULL,
  password VARCHAR(255) NOT NULL,
  email VARCHAR(100) UNIQUE NOT NULL,
  role VARCHAR(20) NOT NULL DEFAULT 'viewer',
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
```

### Items Table

```sql
CREATE TABLE items (
  id INT PRIMARY KEY AUTO_INCREMENT,
  title VARCHAR(255),
  description VARCHAR(1000)
);
```

## Troubleshooting

### Backend Issues

**ModuleNotFoundError: No module named 'mariadb'**
```bash
pip install mariadb
```

**Database connection error**
- Ensure MariaDB is running
- Check credentials in `database.py`
- Verify database `cit_curriculum` exists

**Port 8000 already in use**
```bash
uvicorn main:app --reload --port 8001
```

### Frontend Issues

**Port 3000 already in use**
```bash
npm run dev -- --port 3001
```

**API connection error**
- Check that backend is running on `http://localhost:8000`
- Check CORS configuration in backend `main.py`
- Check browser console for error messages

## Next Steps / Enhancements

- [ ] Email verification for registration
- [ ] Password reset functionality
- [ ] User profile editing
- [ ] Portfolio item management (CRUD)
- [ ] File upload for portfolio items
- [ ] Search and filter functionality
- [ ] Pagination for user lists
- [ ] Audit logs for admin actions
- [ ] Rate limiting on API endpoints
- [ ] Testing (pytest for backend, vitest for frontend)

## Environment Variables

Create `.env` files if needed:

**Backend (.env)**
```
DATABASE_URL=mariadb+mariadbconnector://root:password@localhost:3306/cit_curriculum
SECRET_KEY=your-super-secret-key
ACCESS_TOKEN_EXPIRE_MINUTES=1440
```

**Frontend (.env)**
```
NUXT_PUBLIC_API_BASE=http://localhost:8000
```

## Development Commands

### Backend
```bash
# Run with auto-reload
uvicorn main:app --reload

# Run database initialization
python init_db.py

# Install new package
pip install package-name
```

### Frontend
```bash
# Development server
npm run dev

# Build for production
npm run build

# Generate static site
npm run generate

# Preview production build
npm run preview
```

## License

MIT License

## Support

For issues or questions, please check:
1. Backend API docs: `http://localhost:8000/docs`
2. Frontend console for errors
3. Database logs for connection issues
