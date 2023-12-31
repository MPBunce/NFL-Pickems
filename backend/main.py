from fastapi import FastAPI, status, Depends, HTTPException, Body, Header, Request
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm 
from fastapi.middleware.cors import CORSMiddleware

from typing_extensions import Annotated, List

from models.pydantic_models import UserLogin, Users, SeasonPicks
from models.database_models import Database_Users, Database_regular_seasons, Database_Users_Scores, Database_Users_Regular_Season_Picks
import models.database_models

from db.database import engine, SessionLocal
from sqlalchemy.orm import Session
from sqlalchemy import text
from auth.jwt_handler import generate_token, decode_token
from auth.password_hashing import hash_password, verify_password
from datetime import datetime, timedelta



app = FastAPI()

origins = [
    "https://d3nsp1xpq5b06f.cloudfront.net",
    "http://192.168.2.18:5173",
    "http://192.168.56.1:5173",
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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

    newUser.email = newUser.email.lower()

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

    access_token_exp = timedelta(hours=12)
    access_token = generate_token(data={"Username": existing_user.username}, expires_delta=access_token_exp)

    return {"access_token": access_token, "token_type": "bearer"}


@app.post('/api/lockin_picks')
async def root( picks: List[SeasonPicks], db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    if len(picks) != 32:
        raise HTTPException(status_code=400, detail="Issue with picks data")
    
    decoded_data = decode_token(token)

    if decoded_data is None:
        raise HTTPException(status_code=401, detail="Token has expired")

    existing_user = db.query(Database_Users).filter(
        Database_Users.username == decoded_data["Username"]
    ).first()
    
    if existing_user is None:
        raise HTTPException(status_code=400, detail="Issues finding user details")

    user_picks = db.query(Database_Users_Regular_Season_Picks).filter(
        (Database_Users_Regular_Season_Picks.user_id == existing_user.id) &
        (Database_Users_Regular_Season_Picks.year == picks[0].year)
    ).all()

    if len(user_picks) == 32:
        raise HTTPException(status_code=400, detail="You have already locked in your picks for this year")

    for pick in picks:

        new_database_pick = Database_Users_Regular_Season_Picks(
            user_id = existing_user.id,
            year = pick.year,
            team_name = pick.team_name,
            team_division = pick.team_division,
            division_position = pick.division_position,
        )

        db.add(new_database_pick)
        db.commit()
        db.refresh(new_database_pick) 

    existing_user = db.query(Database_Users_Regular_Season_Picks).filter(
        Database_Users_Regular_Season_Picks.user_id == existing_user.id
    ).all()

        #Trigger Stored Proc
    stored_proc_call = text("CALL public.update_regular_season_scores(2023)")
    db.execute(stored_proc_call)
    db.commit()

    
    return len(picks)


@app.get('/api/get_picks')
async def root( year: str, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    
    decoded_data = decode_token(token)

    if decoded_data is None:
        raise HTTPException(status_code=401, detail="Token has expired")

    existing_user = db.query(Database_Users).filter(
        Database_Users.username == decoded_data["Username"]
    ).first()
    if existing_user is None:
        raise HTTPException(status_code=400, detail="Issues finding user details")
    
    user_picks = db.query(Database_Users_Regular_Season_Picks).filter(
        (Database_Users_Regular_Season_Picks.user_id == existing_user.id) &
        (Database_Users_Regular_Season_Picks.year == year)
    ).all()

    return user_picks


@app.get('/api/seasons/')
async def root( year: str, db: Session = Depends(get_db)):

    try:
        results = db.query(Database_regular_seasons).filter(Database_regular_seasons.year == year).all()
        return results
    except Exception as e:
        return JSONResponse({"error": str(e)})

@app.get('/api/leaderboard/')
async def root( year: str, db: Session = Depends(get_db)):

    try:
        results = db.query(Database_Users_Scores).filter(Database_Users_Scores.year == year).all()
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

