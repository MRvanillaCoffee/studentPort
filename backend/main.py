# Create table and initialize session in main.py
from fastapi import FastAPI, Depends
from . import database, models
from sqlalchemy.orm import Session

app = FastAPI()
models.Base.metadata.create_all(bind=database.engine)

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/items/")
def read_items(db: Session = Depends(get_db)):
    return db.query(models.Item).all()
