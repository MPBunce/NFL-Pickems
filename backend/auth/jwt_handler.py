import time 
import jwt

import os
from dotenv import load_dotenv

load_dotenv()

JWT_SECRET : str = os.getenv("SECRET")
ALGO : str = os.getenv("ALGORITHM")


def token_response(token: str):
    return {
        "access token": token
    }

def signJWT(userId: str):
    payload = {
        "userId": userId,
        "expiry": time.time() + 600
    }
    token = jwt.encode(payload, JWT_SECRET, algorith=ALGO)
    return token_response(token)

def decodeJWT(token: str):
    try:
        decode_token = jwt.decode(token, JWT_SECRET, algorith=ALGO)
        return decode_token if decode_token['expires'] >= time.time() else None    
    except:
        return {}