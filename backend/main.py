from fastapi import FastAPI
import psycopg2
from psycopg2.extras import RealDictCursor
from dotenv import dotenv_values

app = FastAPI()



@app.get("/api")
async def root():
    return {"message": "Hello World Health Check"}

@app.get("/")
async def root():
    return {"message": "Healthy"}