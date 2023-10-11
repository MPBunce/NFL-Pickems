from fastapi import FastAPI, status, Depends, HTTPException
from fastapi.responses import JSONResponse
from models.database_models import Users, UserLogin, regular_seasons

import models.database_models

from db.database import engine, SessionLocal
from sqlalchemy.orm import Session

from auth.jwt_handler import signJWT, decodeJWT

app = FastAPI()

models.database_models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try: 
        yield db
    finally:
        db.close

@app.get('/api/auth/register')
async def root( newUser: Users, db: Session = Depends(get_db) ):
    existing_user = db.query(Users).filter(
        Users.username == newUser.username
    ).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="User with this username already exists")

    existing_user_email = db.query(Users).filter(
        Users.email == newUser.email
    ).first()
    if existing_user_email:
        raise HTTPException(status_code=400, detail="User with this email already exists")

    # If the user doesn't already exist, create and add the new user
    db_user = Users(**newUser.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return {"message": "User registered successfully"}

@app.get('/api/seasons/')
async def root( year: str, db: Session = Depends(get_db) ):
    try:
        # Assuming you have a model called YourModel
        results = db.query(regular_seasons).filter(regular_seasons.year == year).all()
        return results
    except Exception as e:
        return JSONResponse({"error": str(e)})

@app.get("/")
async def root():
    return JSONResponse(content={"message": "Health check, service is running!"})

