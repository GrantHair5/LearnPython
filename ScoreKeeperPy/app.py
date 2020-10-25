from Team import Team
from Game import Game
from Score import Score
from time import time

manUStartingEleven = ["De Gea", "Wan Bisaka", "Maguire", "Lindelof", "Shaw", "Van De Beek", "Pogba", "Fernandes", "Martial", "Greenwood", "Rashford"]        
chelseaStartingEleven = ["Mendy", "James", "Zouma", "Silva", "Chillwell", "Jorginho", "Kante", "Mount", "Pulisic", "Werner", "Havertz"]

manUnited = Team("Man United", manUStartingEleven)
chelsea = Team("Chelsea", chelseaStartingEleven)

gameOne = Game()

gameOne.addTeamOneGoal("Greenwood", manUnited.Name)
gameOne.addTeamTwoGoal("Havertz", chelsea.Name)

 








