from bs4 import BeautifulSoup
import requests


import psycopg2
from psycopg2.extras import RealDictCursor
from psycopg2.extras import execute_values


import os
from dotenv import load_dotenv


class Team:
    def __init__(self, id, name, wins, loses):
        self.id = id
        self.name = name
        self.wins = wins
        self.loses = loses

currentYear = '2023'

url = 'https://www.pro-football-reference.com/years/' + currentYear + '/index.htm'
requestPage = requests.get(url)
soup = BeautifulSoup(requestPage.text, "html.parser")
AFC = soup.find("div", {"id": "all_AFC"})
NFC = soup.find("div", {"id": "all_NFC"})

afcTable = AFC.find('tbody')
afcArray = []

for row in afcTable.find_all('tr'):

    conference = row.find("td", {'data-stat': 'onecell'}) 
    if conference is not None:
        currentConference = conference.contents[0]

    team = row.find("a")
    if (team != None):
        teamName = team.contents[0]
    wins = row.find("td", {'data-stat': 'wins'}) 
    if (wins != None):
        totalWins = wins.contents[0]
    losses = row.find("td", {'data-stat': 'losses'}) 
    if (losses != None):
        totalLs = losses.contents[0]

    ties = row.find("td", {'data-stat': 'ties'}) 


    if team and wins and losses is not None:
        total = [teamName, totalWins, totalLs]
        if ties is None:
            total.append(0)
        else:
            total.append(ties.contents[0])
        total.append(currentConference)
        total.append(currentYear)
        afcArray.append(total)

nfcTable = NFC.find('tbody')
nfcArray = []

for row in nfcTable.find_all('tr'):

    conference = row.find("td", {'data-stat': 'onecell'}) 
    if conference is not None:
        currentConference = conference.contents[0]

    team = row.find("a")
    if (team != None):
        teamName = team.contents[0]
    wins = row.find("td", {'data-stat': 'wins'}) 
    if (wins != None):
        totalWins = wins.contents[0]
    losses = row.find("td", {'data-stat': 'losses'}) 
    if (losses != None):
        totalLs = losses.contents[0]
    
    ties = row.find("td", {'data-stat': 'ties'}) 

    if team and wins and losses is not None:
        total = [teamName, totalWins, totalLs]
        if ties is None:
            total.append(0)
        else:
            total.append(ties.contents[0])
        total.append(currentConference)
        total.append(currentYear)
        nfcArray.append(total)

for n in range(len(afcArray)):
    position = (n + 1) % 4
    if position == 0:
        afcArray[n].append(4)
    else:   
        afcArray[n].append(position)

print("\n")
for n in afcArray:
    print(n)

for n in range(len(nfcArray)):
    position = (n + 1) % 4
    if position == 0:
        nfcArray[n].append(4)
    else:   
        nfcArray[n].append(position)

print("\n")
for n in nfcArray:
    print(n)


load_dotenv()

POSTGRES_USER : str = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_SERVER : str = os.getenv("POSTGRES_SERVER","localhost")
POSTGRES_PORT : str = os.getenv("POSTGRES_PORT",5432) # default postgres port is 5432
POSTGRES_DB : str = os.getenv("POSTGRES_DB")
DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"

# Define the SQL INSERT statement template with ON CONFLICT
insert_sql = f"""
    INSERT INTO "nfl-seasons" (team_name, wins, losses, ties, team_division, year, divisional_position)
    VALUES %s
    ON CONFLICT (team_name, year) DO UPDATE
    SET wins = excluded.wins, losses = excluded.losses, ties = excluded.ties, team_division = excluded.team_division, divisional_position = excluded.divisional_position;
"""

#Update DB
try:
    conn = psycopg2.connect(DATABASE_URL)
    cursor = conn.cursor()    
    
    # Assuming afcArray and nfcArray are lists of tuples containing data
    execute_values(cursor, insert_sql, afcArray)
    execute_values(cursor, insert_sql, nfcArray)

    conn.commit()
    cursor.close()
    conn.close()

except psycopg2.Error as e:
    print("Error connecting to the database:", e)



#Invoke SP to update scores
try:
    conn = psycopg2.connect(DATABASE_URL)
    cursor = conn.cursor()    
    
    exeYear = int(currentYear)
    cursor.execute('CALL public.update_regular_season_scores(%s);', (exeYear,))

    print("sproc")
    
    cursor.close()
    conn.close()

except psycopg2.Error as e:
    print("Error connecting to the database:", e)