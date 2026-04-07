# 📐 System Architecture & Design Documentation

## System Overview

This Student Portfolio system implements a classic 3-tier architecture with role-based access control:

```
┌─────────────────────────────────────────────────────────────┐
│                    Frontend (Nuxt 4 + Vue 3)                │
│              Browser-based Single Page Application          │
├─────────────────────────────────────────────────────────────┤
│                     HTTP/REST API Layer                     │
│            FastAPI Running on http://localhost:8000         │
├─────────────────────────────────────────────────────────────┤
│                   Backend (Python FastAPI)                  │
│  • Authentication & Authorization                          │
│  • Business Logic                                           │
│  • Data Validation (Pydantic)                               │
├─────────────────────────────────────────────────────────────┤
│                   Data Layer (MariaDB)                      │
│       cit_curriculum database with users & items tables    │
└─────────────────────────────────────────────────────────────┘
```

## Component Architecture

### Frontend Components

#### Pages
- **index.vue** - Welcome/Home page
- **login.vue** - Authentication page
- **register.vue** - User registration
- **admin/index.vue** - Admin dashboard
- **viewer/index.vue** - Viewer dashboard

#### Composables
- **useAuth.ts** - Centralized authentication logic
  - Login/Logout functionality
  - Token management
  - User state management
  - localStorage integration

#### Middleware
- **auth.ts** - Route protection
  - Checks if user is authenticated
  - Verifies user role
  - Redirects unauthorized access

### Backend Structure

#### Models (SQLAlchemy)
```python
User:
  - id
  - username (unique)
  - email (unique)
  - password (hashed)
  - role (admin/viewer)
  - created_at

Item:
  - id
  - title
  - description
```

#### Schemas (Pydantic)
- Request/Response validation
- Type safety and documentation
- Auto-generated API docs

#### Endpoints
```
Authentication:
  POST /api/register     - Create new user
  POST /api/login        - Authenticate and get token

Users:
  GET  /api/users/       - List all users (admin only)
  GET  /api/users/me     - Get current user
  DELETE /api/users/{id} - Delete user (admin only)

Items:
  GET  /api/items/       - List all items
```

## Authentication Flow

### Login Process

```
1. User enters credentials
   ↓
2. Frontend sends POST /api/login
   ↓
3. Backend validates credentials
   ├─ Check username exists
   ├─ Verify password with bcrypt
   └─ If valid → Generate JWT token
   ↓
4. Return token + user data
   ↓
5. Frontend stores token in localStorage
   ↓
6. Frontend redirects to role-based dashboard
```

### Protected Request Flow

```
1. Frontend needs to access protected resource
   ↓
2. Add JWT token to Authorization header
   ├─ Header: "Authorization: Bearer {token}"
   ↓
3. Backend validates token
   ├─ Verify token signature
   ├─ Check token expiration
   ├─ Extract user info
   └─ Authorize based on role
   ↓
4. Return protected resource or 401 Unauthorized
```

### Route Protection Flow

```
Frontend Route Request
   ↓
auth.ts Middleware Executes
   ├─ Is route public? (login, register, home)
   │  └─ Yes → Allow access
   ├─ Has valid token?
   │  └─ No → Redirect to /login
   ├─ Route requires admin?
   │  └─ User role ≠ admin → Redirect to /
   └─ All checks pass → Allow access
```

## Role-Based Access Control (RBAC)

### Admin Role
**Permissions:**
- Access /admin dashboard
- View user statistics
- Create new users
- Delete users
- Change user roles
- View all items

**Dashboard Features:**
- User management interface
- User statistics cards
- Add user form
- User list with actions

### Viewer Role
**Permissions:**
- Access /viewer dashboard
- View own profile
- View portfolio items
- Logout

**Dashboard Features:**
- Profile information
- Portfolio item display
- Read-only access

### Public Access
- Home page (/)
- Login page (/login)
- Registration page (/register)

## Data Flow Diagrams

### Registration Flow

```
User Input (Form)
   ↓
validate passwords match
   ↓
POST /api/register
   ├─ Check username unique
   ├─ Check email unique
   ├─ Hash password with bcrypt
   ├─ Create user record
   └─ Return user data
   ↓
Show success message
   ↓
Redirect to login page
```

### User Management (Admin)

```
Admin Opens Dashboard
   ↓
fetchUsers() on mount
   ↓
GET /api/users/
   ├─ Validate token
   ├─ Check admin role
   ├─ Return all users
   └─ Render user table
   ↓
Admin clicks "Add User"
   ├─ Show add user form
   ├─ Enter user details
   ├─ POST /api/register
   ├─ Clear form
   └─ Refetch users
   ↓
Admin clicks "Delete"
   ├─ Confirm action
   ├─ DELETE /api/users/{id}
   ├─ Remove from table
   └─ Update statistics
```

## Security Architecture

### Password Security
```
User Input: "password123"
   ↓
Bcrypt Hashing (10 rounds)
   ├─ Generate salt
   ├─ Hash password + salt
   └─ Return hashed value
   ↓
Database Store: $2b$10$...
```

### Token Security
```
Credentials Valid
   ↓
Generate JWT
├─ Header: {"alg": "HS256", "typ": "JWT"}
├─ Payload: {"sub": "username", "exp": 86400}
├─ Sign with SECRET_KEY
└─ Return encoded token
   ↓
Store in localStorage (client-side)
   ↓
Send with each protected request
   ├─ Header: Authorization: Bearer {token}
   ↓
Backend validates
├─ Check token signature
├─ Verify not expired
└─ Extract username
```

### CORS Configuration
```
Allowed Origins:
├─ http://localhost:3000
└─ http://localhost:3001

Allowed Methods:
├─ GET
├─ POST
├─ PUT
└─ DELETE

Allowed Headers:
└─ * (all headers)

Credentials: Allowed
```

## State Management

### Pinia/Vue State (useAuth)
```javascript
useState('user', () => null)           // Current user object
useState('token', () => null)          // JWT token
computed('isAuthenticated')            // Token exists check
```

### Local Storage
```javascript
localStorage.getItem('auth_token')     // JWT token
localStorage.getItem('auth_user')      // User data JSON
```

### Session State
- Token exists in memory (useState)
- User data exists in memory
- Survives page refresh via localStorage
- Cleared on logout

## Error Handling

### Frontend Error Handling
```javascript
try {
  API call
} catch (error) {
  if (error.status === 401) {
    // Token expired/invalid → Logout
  } else if (error.status === 403) {
    // Permission denied → Show error
  } else if (error.status === 400) {
    // Validation error → Show form error
  } else {
    // Unknown error → Show generic message
  }
}
```

### Backend Error Handling
```python
HTTPException(status_code=401, detail="Unauthorized")
HTTPException(status_code=403, detail="Forbidden")
HTTPException(status_code=404, detail="Not found")
HTTPException(status_code=400, detail="Bad request")
```

## Configuration Management

### Environment Variables

**Backend (.env)**
```
DATABASE_URL=mariadb+mariadbconnector://...
SECRET_KEY=your-secret-key
ACCESS_TOKEN_EXPIRE_MINUTES=1440
```

**Frontend (.env)**
```
NUXT_PUBLIC_API_BASE=http://localhost:8000
```

### Runtime Config (Nuxt)
```typescript
runtimeConfig: {
  public: {
    apiBase: 'http://localhost:8000'  // Can be overridden
  }
}
```

## Performance Considerations

### Frontend
- ✅ Lazy loading pages
- ✅ Client-side validation reduces API calls
- ✅ localStorage caching of user data
- ✅ Conditional rendering

### Backend
- ✅ Connection pooling (SQLAlchemy)
- ✅ Database indexing (username, email unique)
- ✅ JWT tokens avoid database lookup on each request
- ⚠️ No pagination yet (TODO: Add for large datasets)

### Database
- ✅ Indexed columns (username, email)
- ✅ Proper data types
- ✅ Foreign key relationships (ready for expansion)

## Scalability Considerations

### Horizontal Scaling
- Stateless API (tokens are self-contained)
- Can run multiple backend instances
- Use load balancer for distribution

### Caching
- Token validation can be cached
- User data cached in localStorage
- Consider Redis for session management

### Database
- Add replication for read scaling
- Implement connection pooling
- Archive old records

## Testing Architecture

### Backend Testing (pytest)
```python
test_auth.py
  - test_register_user
  - test_login_valid
  - test_login_invalid
  - test_password_hashing

test_endpoints.py
  - test_get_users_admin
  - test_get_users_viewer
  - test_delete_user
```

### Frontend Testing (vitest)
```javascript
useAuth.test.ts
  - test login functionality
  - test logout
  - test token persistence

pages/login.test.ts
  - test form validation
  - test error display
  - test navigation
```

## Deployment Architecture

### Development
```
Frontend: http://localhost:3000
Backend: http://localhost:8000
Database: localhost:3306
```

### Production
```
Frontend: CDN / Nginx static hosting
Backend: Docker container / App server
Database: Managed service / Dedicated server
SSL/TLS: HTTPS everywhere
Environment: Variables via .env
```

## Extension Points

### Easy to Add
1. **Email Verification** - Send code on registration
2. **Password Reset** - Email-based recovery
3. **Profile Editing** - Add user settings page
4. **Activity Logging** - Track admin actions
5. **Rate Limiting** - Prevent abuse

### Moderate Complexity
1. **Two-Factor Authentication** - TOTP/SMS
2. **Social Login** - OAuth integration
3. **File Upload** - Portfolio item attachments
4. **Search/Filter** - User list filtering
5. **Audit Trail** - Complete action logging

### Advanced Features
1. **API Key Management** - Developer access
2. **Role Permissions Matrix** - Fine-grained control
3. **Webhook Support** - Event notifications
4. **GraphQL API** - Alternative query interface
5. **Real-time Updates** - WebSocket integration

## Known Limitations & TODOs

- [ ] No pagination for user lists
- [ ] No email verification
- [ ] No password reset
- [ ] No user profile editing
- [ ] No activity logging
- [ ] No rate limiting
- [ ] No API documentation export (OpenAPI already available)
- [ ] No refresh token rotation
- [ ] No audit trail for admin actions

---

**Last Updated:** April 2026
**Version:** 1.0.0
**Architecture Pattern:** REST API + SPA
