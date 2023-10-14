from fastapi import FastAPI, status, Depends, HTTPException, Body, Header, Request
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm 

from typing_extensions import Annotated

from models.pydantic_models import UserLogin, Users, SeasonPicks
from models.database_models import Database_Users, Database_regular_seasons, Database_Users_Regular_Season_Picks
import models.database_models

from db.database import engine, SessionLocal
from sqlalchemy.orm import Session

from auth.jwt_handler import generate_token, decode_token
from auth.password_hashing import hash_password, verify_password
from datetime import datetime, timedelta

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/login")
models.database_models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try: 
        yield db
    finally:
        db.close

@app.post('/api/auth/register')
async def root(newUser: Users, db: Session = Depends(get_db) ):

    existing_user = db.query(Database_Users).filter(
        Database_Users.username == newUser.username
    ).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="User with this username already exists")

    existing_user_email = db.query(Database_Users).filter(
        Database_Users.email == newUser.email
    ).first()
    if existing_user_email:
        raise HTTPException(status_code=400, detail="User with this email already exists")

    if newUser.password is None:
        raise HTTPException(status_code=400, detail="No Password?")       

    hashed_pwd = hash_password(newUser.password)

    new_database_entry = Database_Users(
        username = newUser.username,
        email = newUser.email,
        hashed_password = hashed_pwd
    )

    db.add(new_database_entry)
    db.commit()
    db.refresh(new_database_entry) 

    return {"message": "User registered successfully"}


@app.post('/api/auth/login')
async def root( form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db) ):
 
    existing_user = db.query(Database_Users).filter(
        Database_Users.username == form_data.username
    ).first()
    if existing_user is None:
        raise HTTPException(status_code=400, detail="User does not exist")
    
    if verify_password(form_data.password, existing_user.hashed_password) is False:
        raise HTTPException(status_code=400, detail="Password Issue")    

    access_token_exp = timedelta(minutes=1)
    access_token = generate_token(data={"Username": existing_user.username}, expires_delta=access_token_exp)

    return {"access_token": access_token, "token_type": "bearer"}


@app.get('/api/get_pickspicks/')
async def root( year: str, token: str = Depends(oauth2_scheme)):
    return year

@app.post('/api/lockin_picks/')
async def root( picks: [SeasonPicks], token: str = Depends(oauth2_scheme)):
    return year

@app.get('/api/seasons/')
async def root( year: str, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    try:
        results = db.query(Database_regular_seasons).filter(Database_regular_seasons.year == year).all()
        return results
    except Exception as e:
        return JSONResponse({"error": str(e)})

@app.get("/tokentest")
async def read_items(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db) ):
    
    decoded_data = decode_token(token)
    
    if decoded_data is None:
        raise HTTPException(status_code=401, detail="Token has expired")

    existing_user = db.query(Database_Users).filter(
        Database_Users.username == decoded_data["Username"]
    ).first()
    if existing_user is None:
        raise HTTPException(status_code=400, detail="User does not exist")

    return existing_user


@app.get("/")
async def root():
    return JSONResponse(content={"message": "Health check, service is running!"})
