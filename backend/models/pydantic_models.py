from pydantic import BaseModel

class UserLogin(BaseModel):
    email: str
    password: str

class Users(BaseModel):
    username: str
    email: str
    password: str   