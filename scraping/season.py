from bs4 import BeautifulSoup
import requests

from pymongo import MongoClient


import os
from dotenv import load_dotenv

class Team:
    def __init__(self, id, name, wins, loses):
        self.id = id
        self.name = name
        self.wins = wins
        self.loses = loses


load_dotenv() 

currentYear = str(os.getenv("YEAR"))

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
        currentConference = conference.contents[0].strip() 

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
        currentConference = conference.contents[0].strip() 

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

#AFC in Json
afc_json_data = []
for team in afcArray:
    team_data = {
        'team': team[0],
        'wins': int(team[1]),
        'losses': int(team[2]),
        'ties': team[3],
        'division': team[4],
        'division_rank': team[6],
        'year': team[5],
    }
    afc_json_data.append(team_data)    

for n in range(len(nfcArray)):
    position = (n + 1) % 4
    if position == 0:
        nfcArray[n].append(4)
    else:   
        nfcArray[n].append(position)

print("\n")
for n in nfcArray:
    print(n)

#nfc in Json
nfc_json_data = []
for team in nfcArray:
    team_data = {
        'team': team[0],
        'wins': int(team[1]),
        'losses': int(team[2]),
        'ties': team[3],
        'division': team[4],
        'division_rank': team[6],
        'year': team[5],
    }
    nfc_json_data.append(team_data)    

total_standings = afc_json_data + nfc_json_data


data = {
    "year" : currentYear,
    "teams" : total_standings
}


print("\ndb:\n")
# Database Time
uri = str(os.getenv("MONGO_URI"))
client = MongoClient(uri)
db = client['NFL-Pickems']

table = db['Season Standings']
count = table.count_documents({'year': currentYear})


if count > 0:
    result = table.update_one(
        {'year': currentYear},
        {'$set': data}      
    )
    print("Updated data")
else:
    table.insert_one(data)
    print("Inserted new data")
