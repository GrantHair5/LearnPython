from Score import Score
class Game():
    totalTimeInMinutes = 90
    GameScore = Score()
    
    def printScore(self):
        scoreText = "{} - {}"
        print(scoreText.format(self.GameScore.TeamOneGoals, self.GameScore.TeamTwoGoals))
    
    def addTeamGoal(self, scorer, teamName, teamId):
        if teamId == 1:
            self.addTeamOneGoal(scorer, teamName)
        elif teamId == 2: 
            self.addTeamTwoGoal(scorer, teamName)


    def addTeamOneGoal(self, scorer, teamName):
        self.GameScore.TeamOneGoals = self.GameScore.TeamOneGoals + 1
        print("Goal by {} for {}".format(scorer, teamName))
        self.printScore()

    def addTeamTwoGoal(self, scorer, teamName):
        self.GameScore.TeamTwoGoals = self.GameScore.TeamTwoGoals + 1
        print("Goal by {} for {}".format(scorer, teamName))
        self.printScore()
    
