class Team:
    def __init__(self, Name, StartingEleven):
        self.Name = Name
        self.StartingEleven = StartingEleven
    
    def printTeamName(self):
        print(self.Name)
    
    def printStartingEleven(self):
        print(self.StartingEleven)

manUStartingEleven = ["De Gea", "Wan Bisaka", "Maguire", "Lindelof", "Shaw", "Van De Beek", "Pogba", "Fernandes", "Martial", "Greenwood", "Rashford"]        
chelseaStartingEleven = ["Mendy", "James", "Zouma", "Silva", "Chillwell", "Jorginho", "Kante", "Mount", "Pulisic", "Werner", "Havertz"]

manUnited = Team("Man United", manUStartingEleven)
manUnited.printTeamName()
manUnited.printStartingEleven()
print(len(manUnited.StartingEleven))


chelsea = Team("Chelsea", chelseaStartingEleven)
chelsea.printTeamName()
chelsea.printStartingEleven()
print(len(chelsea.StartingEleven))