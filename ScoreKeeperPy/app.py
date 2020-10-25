from Team import Team
from Game import Game
from Score import Score
from time import time

manUStartingEleven = ["De Gea", "Wan Bisaka", "Maguire", "Lindelof", "Shaw", "Van De Beek", "Pogba", "Fernandes", "Martial", "Greenwood", "Rashford"]        
chelseaStartingEleven = ["Mendy", "James", "Zouma", "Silva", "Chillwell", "Jorginho", "Kante", "Mount", "Pulisic", "Werner", "Havertz"]

homeTeam = Team("Man United", manUStartingEleven, 1)
awayTeam = Team("Chelsea", chelseaStartingEleven, 2)

gameOne = Game()

gameOne.addTeamGoal("Greenwood", homeTeam.Name, homeTeam.TeamId)
gameOne.addTeamGoal("Havertz", awayTeam.Name, awayTeam.TeamId)
gameOne.addTeamGoal("Rashford", homeTeam.Name, homeTeam.TeamId)

 








