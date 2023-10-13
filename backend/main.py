from fastapi import FastAPI, status, Depends, HTTPException, Body
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm 

from typing_extensions import Annotated

from models.pydantic_models import UserLogin, Users
from models.database_models import Database_Users, Database_regular_seasons
import models.database_models

from db.database import engine, SessionLocal
from sqlalchemy.orm import Session

from auth.jwt_handler import signJWT, decodeJWT
from auth.password_hashing import hash_password, verify_password

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
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
async def root( newUser: Users, db: Session = Depends(get_db) ):


    return {"message": "User Login successfully"}

@app.get('/api/seasons/')
async def root( year: str, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    try:
        results = db.query(Database_regular_seasons).filter(Database_regular_seasons.year == year).all()
        return results
    except Exception as e:
        return JSONResponse({"error": str(e)})

@app.get("/")
async def root():
    return JSONResponse(content={"message": "Health check, service is running!"})
