from fastapi import FastAPI, status, Depends, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import List
from models import Users, regular_seasons
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try: 
        yield db
    finally:
        db.close

@app.get('/api/seasons/')
async def root( year: str, db: Session = Depends(get_db) ):
    try:
        # Assuming you have a model called YourModel
        results = db.query(regular_seasons).filter(regular_seasons.year == year).all()
        return results
    except Exception as e:
        return JSONResponse({"error": str(e)})


@app.get("/api")
async def root():
    return JSONResponse(content={"message": "Hello World Health Check"})

@app.get("/")
async def root():
    return JSONResponse(content={"message": "Healthy"})