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
    divisional_position = Column(Integer)


# Playoff model for nfl

class Database_Users(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    hashed_password = Column(String)


class Database_Users_Regular_Season_Picks(Base):
    __tablename__ = 'users-regular-season-picks'
    
    pick_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    year = Column(Integer)
    team_name = Column(String)
    team_division = Column(String)
    division_position = Column(Integer)

class Database_Users_Scores(Base):
    __tablename__ = 'users-scores'
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    year = Column(Integer, unique=True)
    regular_season_score = Column(Integer)
    playoff_score = Column(Integer)