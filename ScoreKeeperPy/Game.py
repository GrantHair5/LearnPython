from Score import Score
class Game():
    totalTimeInMinutes = 90
    def __init__(self, Score):
        self.Score = Score
    def printScore(self):
        scoreText = "{} - {}"
        print(scoreText.format(self.Score.TeamOneGoals, self.Score.TeamTwoGoals))
