from bs4 import BeautifulSoup, Comment
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

currentYear = '2022'

url = 'https://www.pro-football-reference.com/years/' + currentYear + '/index.htm'
requestPage = requests.get(url)
soup = BeautifulSoup(requestPage.text, "html.parser")

AFC = soup.find("div", {"id": "all_afc_playoff_standings"})
NFC = soup.find("div", {"id": "all_nfc_playoff_standings"})
PLAYOFFS = soup.find("div", {"id": "all_playoff_results"})

afcArray = []
commentsAFC = AFC.find_all(string=lambda text: isinstance(text, Comment))
for comment in commentsAFC:
    commented_html = comment.extract()

    commented_soup = BeautifulSoup(commented_html, 'html.parser')

    tbody = commented_soup.find('tbody')
    for row in tbody.find_all('tr'):
        team_name = row.find('th').a.text
        afcArray.append(team_name)

for n in afcArray:
    print(n)  

nfcArray = []
commentsNFC = NFC.find_all(string=lambda text: isinstance(text, Comment))
for comment in commentsNFC:
    commented_html = comment.extract()

    commented_soup = BeautifulSoup(commented_html, 'html.parser')

    tbody = commented_soup.find('tbody')
    for row in tbody.find_all('tr'):
        team_name = row.find('th').a.text
        nfcArray.append(team_name)

for n in nfcArray:
    print(n)  

playoffsArray = []
commentsPLAYOFFS = PLAYOFFS.find_all(string=lambda text: isinstance(text, Comment))
for comment in commentsPLAYOFFS:
    commented_html = comment.extract()

    commented_soup = BeautifulSoup(commented_html, 'html.parser')


    tbody = commented_soup.find('tbody')
    for row in tbody.find_all('tr'):
        data = []
        #print(row.find('th').text, row.find("td", {'data-stat': 'winner'}).text, row.find("td", {'data-stat': 'loser'}).text, row.find("td", {'data-stat': 'pts_win'}).text, row.find("td", {'data-stat': 'pts_lose'}).text )
        data.append(row.find('th').text)
        data.append(row.find("td", {'data-stat': 'winner'}).text)
        data.append(row.find("td", {'data-stat': 'loser'}).text)
        data.append(row.find("td", {'data-stat': 'pts_win'}).text)
        data.append(row.find("td", {'data-stat': 'pts_lose'}).text)
        if data is not None:
            playoffsArray.append(data)

for n in playoffsArray:
    print(n)  


load_dotenv()

# POSTGRES_USER : str = os.getenv("POSTGRES_USER")
# POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
# POSTGRES_SERVER : str = os.getenv("POSTGRES_SERVER","localhost")
# POSTGRES_PORT : str = os.getenv("POSTGRES_PORT",5432) # default postgres port is 5432
# POSTGRES_DB : str = os.getenv("POSTGRES_DB")
# DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"

# # Define the SQL INSERT statement template with ON CONFLICT
# insert_sql = f"""
#     INSERT INTO "nfl-seasons" (team_name, wins, losses, ties, team_division, year, divisional_position)
#     VALUES %s
#     ON CONFLICT (team_name, year) DO UPDATE
#     SET wins = excluded.wins, losses = excluded.losses, ties = excluded.ties, team_division = excluded.team_division, divisional_position = excluded.divisional_position;
# """

# #Update DB
# try:
#     conn = psycopg2.connect(DATABASE_URL)
#     cursor = conn.cursor()    
    
#     # Assuming afcArray and nfcArray are lists of tuples containing data
#     execute_values(cursor, insert_sql, afcArray)
#     execute_values(cursor, insert_sql, nfcArray)

#     conn.commit()
#     cursor.close()
#     conn.close()

# except psycopg2.Error as e:
#     print("Error connecting to the database:", e)



# #Invoke SP to update scores
# try:
#     conn = psycopg2.connect(DATABASE_URL)
#     cursor = conn.cursor()    
    
#     exeYear = int(currentYear)
#     cursor.execute('CALL public.update_regular_season_scores(%s);', (exeYear,))

#     print("sproc")
    
#     cursor.close()
#     conn.close()

# except psycopg2.Error as e:
#     print("Error connecting to the database:", e)