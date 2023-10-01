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

for row in afcTable.find_all('tr'):
    print( row.find("a") )
    print( row.find("td", {'data-stat': 'wins'}) )
    print( row.find("td", {'data-stat': 'losses'}) )
    print('\n')

#Formatting AFC Teams




