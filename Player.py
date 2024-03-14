class Player:

    def __init__(self, team: str, name: str, runs: int, sr: float, fours: int, sixes: int, zeroDismisals: int, fifties: int, centuries: int, notOuts: int, isBowler: bool, ballsFaced: int, wickets: int, fourplus: int, fiveplus: int, sixplus: int, maidens: int, hattrick: int, economy: float, oversBowled: int) -> None:
        
        # Initial Variables
        self.team = team
        self.name = name

        self.runs = runs
        self.sr = sr
        self.fours = fours
        self.sixes = sixes
        self.zeroDismisals = zeroDismisals
        self.fifties = fifties
        self.centuries = centuries
        self.notOuts = notOuts
        self.isBowler = isBowler
        self.ballsFaced = ballsFaced
        self.total = 0

        self.wickets = wickets
        self.fourplus = fourplus
        self.fiveplus = fiveplus
        self.sixplus = sixplus
        self.maidens = maidens
        self.hattrick = hattrick
        self.economy = economy
        self.oversBowled = oversBowled

        
        
        # Calculate Points
        self.calculate_batting_points()
        self.calculate_bowling_points()

    def calculate_batting_points(self):
        
        # Yellow
        yellow = 0
        yellow += self.runs * 2 # 2 points per run
        yellow += self.fours * 4 # 4 point per 4
        yellow += self.sixes * 8 # 8 points per 6
        yellow -= self.zeroDismisals * 6 # -6 points per 0 dismissal
        yellow += self.fifties * 50 # 50 points per 50
        yellow += self.centuries * 100 # 100 points per 100

        if self.isBowler == True: # If the player is a bowler, double the points
            yellow *= 2
        
        # Green
        green = 0
        if self.ballsFaced > 15:
            if self.sr > 200.00:
                green += 1000
            elif 175.00 <= self.sr <= 200.00:
                green += 800
            elif 150.00 <= self.sr < 175.00:
                green += 600
            elif 125.00 <= self.sr < 150.00:
                green += 400
            elif 100.00 <= self.sr < 125.00:
                green += 200
            elif 75.00 <= self.sr < 100.00:
                green -= 100
            elif 50.00 <= self.sr < 75.00:
                green -= 200
            elif 25.00 <= self.sr < 50.00:
                green -= 300
            else:
                green -= 500
        if self.isBowler == True: # If the player is a bowler, double the points
            green *= 2


        # Cyan
        cyan = 0
        if self.ballsFaced > 15:
            if self.sr > 850:
                cyan += 5000
            elif self.sr > 800:
                cyan += 4500
            elif self.sr > 750:
                cyan += 4000
            elif self.sr > 700:
                cyan += 3500
            elif self.sr > 650:
                cyan += 3000
            elif self.sr > 600:
                cyan += 2500
            elif self.sr > 550:
                cyan += 2000
            elif self.sr > 500:
                cyan += 1500
            elif self.sr > 450:
                cyan += 1000
            elif self.sr > 400:
                cyan += 750
            elif self.sr > 350:
                cyan += 500
            elif self.sr > 300:
                cyan += 250
        if self.isBowler == True: # If the player is a bowler, double the points
            cyan *= 2
        
        # Total
        self.total = yellow + green + cyan

        """ Calculations for MAXES are done else where"""

    # Getter Methods for MAX calculations 
    def getAverage(self):
        return self.runs / self.ballsFaced

    def getStrikeRate(self):
        return (self.runs / self.ballsFaced) * 100

    def getScore(self):
        return self.runs
    
    def get4s(self):
        return self.fours

    def get6s(self):
        return self.sixes

    def get50s(self):
        return self.fifties

    def get100s(self):
        return self.centuries

    def get0s(self):
        return self.zeroDismisals

    def getNOs(self):
        return self.notOuts
    
    def getMaidens(self):
        return self.maidens

    def getWickets(self):
        return self.wickets
    
    def getEconomy(self):
        return self.economy
    
    def getfourplus(self):
        return self.fourplus

    def getfiveplus(self):
        return self.fiveplus
    
    def getsixplus(self):
        return self.sixplus
    
    #TODO: Complete List






    def calculate_bowling_points(self):
        pass




    def __str__(self) -> str:
        return f"Runs: {self.runs}, SR: {self.sr}, 4s: {self.fours}, 6s: {self.sixes}, 0s: {self.zeroDismisals}, 50s: {self.fifties}, 100s: {self.centuries}, NOs: {self.notOuts}, Bowler: {self.isBowler}, Balls Faced: {self.ballsFaced}"