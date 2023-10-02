from bs4 import BeautifulSoup
import requests

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
    team = row.find("a")
    if (team != None):
        teamName = team.contents[0]
    wins = row.find("td", {'data-stat': 'wins'}) 
    if (wins != None):
        totalWins = wins.contents[0]
    losses = row.find("td", {'data-stat': 'losses'}) 
    if (losses != None):
        totalLs = losses.contents[0]
    
    if team and wins and losses is not None:
        total = [teamName, totalWins, totalLs]
        afcArray.append(total)

nfcTable = NFC.find('tbody')
nfcArray = []

for row in nfcTable.find_all('tr'):
    team = row.find("a")
    if (team != None):
        teamName = team.contents[0]
    wins = row.find("td", {'data-stat': 'wins'}) 
    if (wins != None):
        totalWins = wins.contents[0]
    losses = row.find("td", {'data-stat': 'losses'}) 
    if (losses != None):
        totalLs = losses.contents[0]
    
    if team and wins and losses is not None:
        total = [teamName, totalWins, totalLs]
        nfcArray.append(total)

for n in afcArray:
    print(n)


print("\n")


for n in nfcArray:
    print(n)



#Formatting AFC Teams




