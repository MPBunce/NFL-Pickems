from datetime import datetime, timedelta
import jwt

import os
from dotenv import load_dotenv

load_dotenv()

JWT_SECRET : str = os.getenv("SECRET")
ALGO : str = os.getenv("ALGORITHM")


def generate_token(data: dict, expires_delta: timedelta or None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire= datetime.utcnow() + timedelta(minutes=15)

    formatted_datetime = expire.strftime("%Y-%m-%d %H:%M:%S")
    to_encode.update({ "expires": formatted_datetime })
    
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET, algorithm=ALGO)
    return encoded_jwt

def validate_token():
    return

def decode_token():
    return