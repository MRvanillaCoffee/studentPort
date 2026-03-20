import hashlib
import os
from typing import Optional

from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from pymongo import MongoClient


MONGO_URI = os.getenv("MONGO_URI", "mongodb://127.0.0.1:27017")
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME", "student_port")


client = MongoClient(MONGO_URI)
db = client[MONGO_DB_NAME]
users_collection = db["users"]
scores_collection = db["scores"]


app = FastAPI(title="StudentPort API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_methods=["*"],
    allow_headers=["*"],
)


class LoginRequest(BaseModel):
    student_id: str = Field(min_length=1)
    password: str = Field(min_length=1)


def _hash_password(password: str) -> str:
    return hashlib.sha256(password.encode("utf-8")).hexdigest()


def _verify_password(raw_password: str, user_doc: dict) -> bool:
    password_hash = user_doc.get("password_hash")
    plain_password = user_doc.get("password")

    if password_hash:
        return _hash_password(raw_password) == password_hash
    if plain_password:
        return raw_password == plain_password
    return False


@app.get("/")
async def root(student_id: Optional[str] = Query(default=None)):
    if not student_id:
        return {"message": "StudentPort API is running", "usage": "?student_id=<id>"}

    user = users_collection.find_one({"student_id": student_id}, {"_id": 0, "password": 0, "password_hash": 0})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    scores = list(scores_collection.find({"student_id": student_id}, {"_id": 0}))

    return {
        "user": user,
        "scores": scores,
        "score_count": len(scores)
    }


@app.post("/auth/login")
async def login(payload: LoginRequest):
    user = users_collection.find_one({"student_id": payload.student_id})
    if not user or not _verify_password(payload.password, user):
        raise HTTPException(status_code=401, detail="Username or password is incorrect")

    return {
        "name": user.get("name", payload.student_id),
        "username": user.get("username", ""),
        "student_id": user.get("student_id", ""),
    }


@app.get("/scores/{student_id}")
async def get_scores(
    student_id: str,
    year: Optional[str] = Query(default=None),
    semester: Optional[str] = Query(default=None),
):
    student_query = {"student_id": student_id}
    query = {"student_id": student_id}
    if year:
        year_values = [year]
        if year.isdigit():
            year_values.append(int(year))
        query["year"] = {"$in": year_values}
    if semester:
        semester_values = [semester]
        if semester.isdigit():
            semester_values.append(int(semester))
        query["semester"] = {"$in": semester_values}

    scores = list(scores_collection.find(query, {"_id": 0}))
    all_scores = list(scores_collection.find(student_query, {"_id": 0, "year": 1, "semester": 1}))
    years = sorted({str(item.get("year")) for item in all_scores if item.get("year") is not None})
    semesters = sorted({str(item.get("semester")) for item in all_scores if item.get("semester") is not None})

    return {
        "items": scores,
        "years": years,
        "semesters": semesters,
    }


@app.post("/seed-demo")
async def seed_demo_data():
    demo_student_id = "6803052411022"
    demo_user = users_collection.find_one({"username": "Thanakorn"})
    if not demo_user:
        users_collection.insert_one(
            {
                "username": "Thanakorn",
                "password_hash": _hash_password("1234"),
                "name": "Thanakorn",
                "student_id": demo_student_id,
            }
        )
    else:
        old_student_id = demo_user.get("student_id")
        if old_student_id != demo_student_id:
            users_collection.update_one(
                {"_id": demo_user["_id"]},
                {"$set": {"student_id": demo_student_id}},
            )
            if old_student_id:
                scores_collection.update_many(
                    {"student_id": old_student_id},
                    {"$set": {"student_id": demo_student_id}},
                )

    if scores_collection.count_documents({"student_id": demo_student_id}) == 0:
        scores_collection.insert_many(
            [
                {
                    "student_id": demo_student_id,
                    "subject": "Programming",
                    "score": 85,
                    "grade": "A",
                    "year": "2567",
                    "semester": "1",
                },
                {
                    "student_id": demo_student_id,
                    "subject": "Database",
                    "score": 78,
                    "grade": "B+",
                    "year": "2567",
                    "semester": "1",
                },
                {
                    "student_id": demo_student_id,
                    "subject": "Web Dev",
                    "score": 92,
                    "grade": "A",
                    "year": "2567",
                    "semester": "2",
                },
                {
                    "student_id": demo_student_id,
                    "subject": "Math",
                    "score": 65,
                    "grade": "C+",
                    "year": "2566",
                    "semester": "2",
                },
            ]
        )

    return {"status": "ok", "message": "Demo data is ready"}