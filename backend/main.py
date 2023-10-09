from fastapi import FastAPI, status, Depends, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import List, Annotated
from models import Users, standings_2023
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

db_dependency = Annotated[Session, Depends(get_db)]

@app.get('/api/season_2023/')
async def root( db: db_dependency):
    try:
        # Assuming you have a model called YourModel
        results = db.query(standings_2023).all()
        return results
    except Exception as e:
        return JSONResponse({"error": str(e)})


@app.get("/api")
async def root():
    return JSONResponse(content={"message": "Hello World Health Check"})

@app.get("/")
async def root():
    return JSONResponse(content={"message": "Healthy"})