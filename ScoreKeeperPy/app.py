from Team import Team
from Game import Game
from Score import Score

scoreOne = Score()
scoreOne.TeamOneGoals = 3
scoreOne.TeamTwoGoals = 2
gameOne = Game(scoreOne)
scoreText = "{} - {}"
print(scoreText.format(gameOne.Score.TeamOneGoals, gameOne.Score.TeamTwoGoals))




#manUStartingEleven = ["De Gea", "Wan Bisaka", "Maguire", "Lindelof", "Shaw", "Van De Beek", "Pogba", "Fernandes", "Martial", "Greenwood", "Rashford"]        
#chelseaStartingEleven = ["Mendy", "James", "Zouma", "Silva", "Chillwell", "Jorginho", "Kante", "Mount", "Pulisic", "Werner", "Havertz"]

#manUnited = Team("Man United", manUStartingEleven)
#manUnited.printTeamName()
#manUnited.printStartingEleven()
#print(len(manUnited.StartingEleven))


#chelsea = Team("Chelsea", chelseaStartingEleven)
#chelsea.printTeamName()
#chelsea.printStartingEleven()
#print(len(chelsea.StartingEleven))