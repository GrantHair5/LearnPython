from Team import Team
from Game import Game
from Score import Score
from time import time

print("Welcome To Grant's Football Game")
print("Enter home team name:")
homeTeamName = input()
print("Enter away team name:")
awayTeamName = input()

manUStartingEleven = ["De Gea", "Wan Bisaka", "Maguire", "Lindelof", "Shaw", "Van De Beek", "Pogba", "Fernandes", "Martial", "Greenwood", "Rashford"]        
chelseaStartingEleven = ["Mendy", "James", "Zouma", "Silva", "Chillwell", "Jorginho", "Kante", "Mount", "Pulisic", "Werner", "Havertz"]

homeTeam = Team(homeTeamName, manUStartingEleven, 1)
awayTeam = Team(awayTeamName, chelseaStartingEleven, 2)

gameOne = Game()

print("Game Has Begun {} vs {}".format(homeTeamName, awayTeamName))
print(" ")

gameOne.addTeamGoal("Greenwood", homeTeam.Name, homeTeam.TeamId)
gameOne.addTeamGoal("Havertz", awayTeam.Name, awayTeam.TeamId)
gameOne.addTeamGoal("Rashford", homeTeam.Name, homeTeam.TeamId)

 








