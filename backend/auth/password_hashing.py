from passlib.context import CryptContext
import os
from dotenv import load_dotenv

load_dotenv()

JWT_SECRET : str = os.getenv("SECRET")
ALGO : str = os.getenv("ALGORITHM")

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def hash_password(password):
    return pwd_context.hash(password)