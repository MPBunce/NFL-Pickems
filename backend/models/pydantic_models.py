from pydantic import BaseModel

class Token(BaseModel):
    access_token: str
    token_type: str

class UserLogin(BaseModel):
    email: str
    password: str

class Users(BaseModel):
    username: str
    email: str
    password: str   

class SeasonPicks(BaseModel):
    year : int
    team_name : str
    team_division : str
    division_position : int

class PlayoffPicks(BaseModel):
    wins: str