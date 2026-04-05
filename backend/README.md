# FastAPI + MongoDB

## 1) ติดตั้งแพ็กเกจ

```powershell
pip install -r backend/requirements.txt
```

## 2) ตั้งค่า environment

```powershell
copy backend/.env.example .env
```

แก้ค่าในไฟล์ `.env` ให้ตรงกับ MongoDB ของคุณ

## 3) รันเซิร์ฟเวอร์

```powershell
uvicorn backend.main:app --reload
```

## 4) ทดสอบ

- http://127.0.0.1:8000/
- http://127.0.0.1:8000/docs

## 5) Login API

`POST /auth/login`

ตัวอย่าง body:

```json
{
	"student_id": "6803052411022",
	"password": "1234"
}
```

ตัวอย่าง response:

```json
{
	"name": "Thanakorn",
	"username": "Thanakorn",
	"student_id": "6803052411022",
	"access_token": "<token>",
	"token_type": "bearer",
	"expires_in": 3600
}
```
