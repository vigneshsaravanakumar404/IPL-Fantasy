class Team:

    def __init__(self, name, players) -> None:

        self.name = name
        self.players = players
        self.total = 0

        self.calculate_points()
        self.generateTeamReport()

    # Getter Methods
    def getTeamName(self):
        return self.name
    
    def getPlayers(self):
        return self.players
    
    def getMaxes(self):
        return None

    # Calculations
    def calculate_points(self): # Without MAXES
        pass

    def generateTeamReport(self): # Without MAXES
        pass
