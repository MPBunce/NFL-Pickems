from db.database import Base
from sqlalchemy import Column, Integer, String

class Database_regular_seasons(Base):
    __tablename__ = 'nfl-seasons'

    id = Column(Integer, primary_key=True, index=True)
    team_name = Column(String)
    wins = Column(Integer)
    losses = Column(Integer)
    ties = Column(Integer)
    team_division = Column(String)
    year = Column(Integer)

class Database_Users(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    hashed_password = Column(String)