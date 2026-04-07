# 🚀 Quick Start Guide - Student Portfolio Login System

I've successfully created a complete login system with role-based access control! Here's what was set up:

## ✅ What's Been Created

### Backend (FastAPI + MariaDB)
- ✅ User authentication system with JWT tokens
- ✅ Password hashing with bcrypt
- ✅ Two user roles: **Admin** and **Viewer**
- ✅ Admin dashboard API endpoints
- ✅ User registration/login endpoints
- ✅ Database models for users and items
- ✅ CORS configuration for frontend communication

### Frontend (Nuxt 4 + Vue 3)
- ✅ Beautiful login page
- ✅ User registration page
- ✅ Admin dashboard (manage users, view statistics)
- ✅ Viewer dashboard (view profile and portfolio)
- ✅ Route protection middleware
- ✅ Authentication composable
- ✅ Responsive design with Tailwind CSS

## 📋 Files Created

### Backend
```
backend/
├── models.py           # Database models (User, Item)
├── schemas.py          # Pydantic request/response models
├── main.py             # FastAPI app with all endpoints
├── __init__.py         # Package initialization
├── init_db.py          # Database initialization script
└── requirements.txt    # Python dependencies
```

### Frontend
```
frontend/student-port/
├── pages/
│   ├── index.vue              # Home page
│   ├── login.vue              # Login page
│   ├── register.vue           # Registration page
│   ├── admin/index.vue        # Admin dashboard
│   └── viewer/index.vue       # Viewer dashboard
├── composables/
│   └── useAuth.ts             # Authentication logic
├── middleware/
│   └── auth.ts                # Route protection
└── nuxt.config.ts             # Updated with API config
```

## 🚀 Getting Started

### Step 1: Install Backend Dependencies

```bash
# Navigate to backend
cd backend

# Install packages
pip install -r requirements.txt
```

### Step 2: Configure Database Connection

Edit `backend/database.py` and update the connection string:

```python
SQLALCHEMY_DATABASE_URL = "mariadb+mariadbconnector://root:YOUR_PASSWORD@127.0.0.1:3306/cit_curriculum"
```

### Step 3: Initialize Database

```bash
# Create tables and add default users
python init_db.py
```

You'll see:
```
✓ Created admin user (username: admin, password: password123)
✓ Created viewer user (username: viewer, password: password123)
✓ Database initialization complete!
```

### Step 4: Start Backend Server

```bash
# Run FastAPI server
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

Check it's running: http://localhost:8000/docs

### Step 5: Install Frontend Dependencies

```bash
# In a new terminal, navigate to frontend
cd frontend/student-port

# Install packages
npm install
```

### Step 6: Start Frontend Server

```bash
npm run dev
```

Access the app: http://localhost:3000

## 🔑 Default Credentials

| Role | Username | Password |
|------|----------|----------|
| **Admin** | admin | password123 |
| **Viewer** | viewer | password123 |

## 🎯 What You Can Do

### As Admin
- Login to admin dashboard
- View user statistics (total users, admins, viewers)
- Add new users
- Delete users
- Change user roles

### As Viewer
- Login to viewer dashboard
- View personal profile
- View portfolio items
- Logout

## 🔐 Security Features Implemented

✅ JWT token authentication
✅ Bcrypt password hashing
✅ Role-based access control
✅ Protected routes
✅ CORS configuration
✅ Secure token storage in localStorage

## 🐛 Troubleshooting

### Database Connection Error
1. Ensure MariaDB is running
2. Check credentials in `backend/database.py`
3. Verify database `cit_curriculum` exists

```sql
CREATE DATABASE IF NOT EXISTS cit_curriculum;
```

### Backend won't start
```bash
# May need to reinstall database driver
pip install --upgrade mariadb
```

### Frontend won't connect to backend
1. Check backend is running on http://localhost:8000
2. Check browser console (F12) for errors
3. Verify CORS settings in `backend/main.py`

## 📚 API Endpoints

```
POST   /api/register          - Register new user
POST   /api/login             - Login user
GET    /api/users/me          - Get current user
GET    /api/items/            - Get all items

API Documentation: http://localhost:8000/docs
```

## 🎨 UI Features

- **Responsive Design** - Works on mobile, tablet, desktop
- **Gradient Backgrounds** - Modern visual design
- **Form Validation** - Client-side validation
- **Error Handling** - User-friendly error messages
- **Loading States** - Visual feedback during actions

## 🔄 Next Steps

1. **Test the system:**
   - Login with admin/password123
   - Login with viewer/password123
   - Try unauthorized access

2. **Customize:**
   - Change SECRET_KEY in `backend/main.py` for production
   - Modify colors/styling in component files
   - Add more functionality as needed

3. **Database:**
   - Add more users directly
   - Modify user table schema
   - Add more tables/models

4. **Production:**
   - Change default passwords
   - Add environment variables
   - Use HTTPS
   - Add more security measures

## 📖 Documentation

See `SETUP.md` for detailed documentation including:
- Full API reference
- Database schema
- Environment variables
- Advanced configuration
- Deployment guide

## 💡 Tips

- Use browser DevTools (F12) to debug
- Check terminal console for backend logs
- Use http://localhost:8000/docs for API testing
- Check network tab to monitor API calls

---

**You're all set! Start building your student portfolio system! 🎓**

For detailed setup, see: `SETUP.md`
