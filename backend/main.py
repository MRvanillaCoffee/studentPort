from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# อนุญาตให้ Vue.js เข้าถึงข้อมูลได้
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/student-stats/{student_id}")
async def get_stats(student_id: str):
    # ส่งข้อมูลปลอมไปให้ Vue.js ก่อน
    return {
        "Engineering": 3.5,
        "Problem Analysis": 4.0,
        "Modern Tools": 2.8,
        "Ethics": 4.0,
        "Teamwork": 3.0
    }