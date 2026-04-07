# 🔧 Troubleshooting Guide

## Common Issues & Solutions

### Backend Issues

#### 1. `ModuleNotFoundError: No module named 'fastapi'`
**Cause:** Dependencies not installed
**Solution:**
```bash
cd backend
pip install -r requirements.txt
```

#### 2. `ModuleNotFoundError: No module named 'mariadb'`
**Cause:** MariaDB connector not installed
**Solution:**
```bash
pip install mariadb
# Or reinstall all dependencies
pip install --upgrade -r requirements.txt
```

#### 3. `Error: (2003, "Can't connect to MySQL server on 'localhost' (111)")`
**Cause:** MariaDB/MySQL server not running
**Solution:**
- **Windows:** Start MySQL Service
  - Services app → MySQL → Right-click → Start
  - Or: `net start MySQL80`
- **Mac:** `brew services start mariadb`
- **Linux:** `sudo systemctl start mariadb`

#### 4. `Error: Unknown database 'cit_curriculum'`
**Cause:** Database doesn't exist
**Solution:**
```sql
-- In MySQL client
CREATE DATABASE cit_curriculum;
```

#### 5. `Error: Access denied for user 'root'`
**Cause:** Wrong password in database.py
**Solution:**
1. Update `backend/database.py`:
```python
SQLALCHEMY_DATABASE_URL = "mariadb+mariadbconnector://root:YOUR_ACTUAL_PASSWORD@127.0.0.1:3306/cit_curriculum"
```

#### 6. Port 8000 already in use
**Cause:** Another service using port 8000
**Solution:**
```bash
# Run on different port
uvicorn main:app --reload --port 8001

# Then update frontend config:
# nuxt.config.ts → apiBase: http://localhost:8001
```

#### 7. `TypeError: 'NoneType' object is not iterable` when fetching users
**Cause:** No users in database
**Solution:**
```bash
# Initialize database
python init_db.py
```

#### 8. CORS error in browser console
**Cause:** Frontend and backend not communicating
**Solution:**
1. Ensure backend is running: `http://localhost:8000/docs`
2. Check browser console for exact error
3. Verify `allow_origins` in `main.py` includes frontend URL
4. Make sure you're using `http://` not `https://`

### Frontend Issues

#### 1. `npm: command not found`
**Cause:** Node.js not installed
**Solution:**
- Download from https://nodejs.org/
- Install (includes npm)
- Restart terminal/IDE

#### 2. `Port 3000 already in use`
**Cause:** Another app using port 3000
**Solution:**
```bash
npm run dev -- --port 3001
# Then access: http://localhost:3001
```

#### 3. `ERR! peer dep missing`
**Cause:** Dependency version mismatch
**Solution:**
```bash
npm install --legacy-peer-deps
```

#### 4. `Cannot find module '@nuxt/...`
**Cause:** Dependencies not installed
**Solution:**
```bash
npm install
# Or clean reinstall
rm -rf node_modules package-lock.json
npm install
```

#### 5. Blank white page / `NuxtWelcome` shows
**Cause:** Old app.vue still in use
**Solution:**
Ensure `app/app.vue` is updated with:
```vue
<template>
  <div>
    <NuxtRouteAnnouncer />
    <NuxtPage />
  </div>
</template>
```

#### 6. `Cannot find pages` or routing not working
**Cause:** Pages not in correct directory
**Solution:**
- Ensure structure:
  ```
  frontend/student-port/pages/
  ├── index.vue
  ├── login.vue
  ├── register.vue
  ├── admin/index.vue
  └── viewer/index.vue
  ```
- Restart dev server: `Ctrl+C`, then `npm run dev`

#### 7. API calls failing with 404
**Cause:** Frontend using wrong API base URL
**Solution:**
1. Check `nuxt.config.ts`:
   ```typescript
   runtimeConfig: {
     public: {
       apiBase: 'http://localhost:8000'
     }
   }
   ```
2. Check `composables/useAuth.ts` uses `apiBase`
3. Verify backend is running on port 8000

#### 8. Login page loads but "Login" button doesn't work
**Cause:** API communication issue
**Solution:**
1. Open browser DevTools (F12)
2. Check Network tab for failed requests
3. Check console for error messages
4. Verify backend is responding: `http://localhost:8000/docs`

### Database Issues

#### 1. Users table empty after login
**Cause:** init_db.py not run
**Solution:**
```bash
cd backend
python init_db.py
```

#### 2. Can't delete users
**Cause:** Missing DELETE endpoint or permission
**Solution:**
1. Verify user is logged in as admin
2. Check backend has DELETE endpoint:
   ```python
   @app.delete("/api/users/{user_id}")
   def delete_user(user_id: int, db: Session = Depends(get_db)):
   ```

#### 3. Passwords showing in plaintext
**Cause:** Password hashing not implemented
**Solution:** Ensure `backend/main.py` uses:
```python
hashed_password = hash_password(user.password)
```

### Network/Connection Issues

#### 1. Frontend can't reach backend
**Diagnosis:**
```bash
# Test from terminal
curl http://localhost:8000/

# Expected response: {"message": "Student Portfolio API"}
```

**Solution:**
1. Backend running? Check terminal
2. Correct port? (default 8000)
3. Firewall blocking? Check settings
4. CORS enabled? Check `main.py`

#### 2. "net::ERR_CONNECTION_REFUSED"
**Cause:** Backend not running or wrong address
**Solution:**
1. Start backend: `uvicorn main:app --reload`
2. Verify it's running: Visit `http://localhost:8000/docs`
3. Check `nuxt.config.ts` has correct URL
4. Check browser console for exact error

#### 3. 401 Unauthorized after login
**Cause:** Token not being sent or expired
**Solution:**
1. Check token in localStorage (DevTools → Application)
2. Verify token in Authorization header (DevTools → Network)
3. Check token expiration in backend

### Authentication Issues

#### 1. Can't login with any credentials
**Cause:** Several possibilities
**Solution:**
```bash
# Verify users exist
# In MySQL client:
USE cit_curriculum;
SELECT * FROM users;

# If empty:
python init_db.py
```

#### 2. Wrong password works anyway
**Cause:** Password verification disabled
**Solution:**
Ensure `verify_password()` is used:
```python
if not verify_password(user.password, db_user.password):
    raise HTTPException(...)
```

#### 3. Logout doesn't work
**Cause:** Token still in localStorage
**Solution:**
1. Ensure logout() called in composable
2. Check localStorage cleared (DevTools → Application)
3. Check browser console for errors

#### 4. Can't create new users
**Cause:** Validation or database issue
**Solution:**
1. Check username/email unique in DB
2. Check password meets requirements (6+ chars)
3. Check role is 'admin' or 'viewer'
4. Check database has write permissions

### Performance Issues

#### 1. Slow login response
**Cause:** 
- Database query slow
- Bcrypt hashing slow (normal, by design)
- Network latency
**Solution:**
1. Check backend response time (DevTools → Network)
2. Monitor database connections
3. Verify no errors in backend terminal

#### 2. Page loading slowly
**Cause:** 
- Large dataset
- Inefficient queries
- Network issues
**Solution:**
- Add pagination (future enhancement)
- Monitor API response times
- Check browser DevTools Performance tab

## Debug Checklist

### When everything breaks:

- [ ] Is backend running? `uvicorn main:app --reload`
- [ ] Is frontend running? `npm run dev`
- [ ] Is database running? Check MariaDB service
- [ ] Can you access `http://localhost:8000/docs`?
- [ ] Can you see network requests in DevTools (F12)?
- [ ] Are there errors in browser console?
- [ ] Are there errors in backend terminal?
- [ ] Did you run `python init_db.py`?
- [ ] Are credentials correct (admin/password123)?
- [ ] Is localhost:3000 in CORS allowed origins?

### Recovery Steps:

1. **Stop everything:**
   ```bash
   # In each terminal
   Ctrl+C
   ```

2. **Restart background services:**
   ```bash
   # Database
   net start MySQL80  # Windows
   # Or use services app
   ```

3. **Reinitialize database:**
   ```bash
   cd backend
   python init_db.py
   ```

4. **Restart backend:**
   ```bash
   cd backend
   uvicorn main:app --reload
   ```

5. **Restart frontend:**
   ```bash
   cd frontend/student-port
   npm run dev
   ```

6. **Access and test:**
   ```
   http://localhost:3000
   ```

## Getting Help

1. **Check browser console** (F12 → Console tab)
2. **Check backend terminal** for error messages
3. **Use DevTools Network tab** to inspect API calls
4. **Check API docs**: `http://localhost:8000/docs`
5. **Review error messages** carefully
6. **Search this guide** for keywords

## Performance Tips

- Keep both dev servers running in separate terminals
- Use browser DevTools Network tab to monitor requests
- Check backend logs in terminal for slow queries
- Use `--reload` flag for auto-reload during development
- Clear localStorage if auth issues persist
- Restart servers after database changes

## Database Backup

Before making changes:
```bash
# Export database
mysqldump -u root -p cit_curriculum > backup.sql

# Restore from backup
mysql -u root -p cit_curriculum < backup.sql
```

---

**Still stuck?** Check the terminal output - it usually tells you exactly what's wrong!

**Last Updated:** April 2026
