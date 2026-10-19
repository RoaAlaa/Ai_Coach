from fastapi import FastAPI
from sqlalchemy import text
from sqlalchemy.orm import Session
from fastapi import Depends
from app.core.database import get_db
app = FastAPI(title = "AI Interview Coach API")


@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.get("/health/db")
def health_check_db(db: Session = Depends(get_db)):
    try:
        db.execute(text("SELECT 1"))
        return {"status": "healthy"}
    except Exception as e:
        return {"status": "unhealthy", "error": str(e)}