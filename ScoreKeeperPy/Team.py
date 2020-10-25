class Team:
    def __init__(self, Name, StartingEleven, TeamId):
        self.Name = Name
        self.StartingEleven = StartingEleven
        self.TeamId = TeamId
    
    def printTeamName(self):
        print(self.Name)
    
    def printStartingEleven(self):
        print(self.StartingEleven)