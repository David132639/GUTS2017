##VERSION 1.1 CHANGED NAME SOHVA
class Monster:
    def __init__(self, loc, route):
        ## loc is a tuple that is the location
        ## Route is the list of the locations in which the monster moves
        self.loc = loc
        self.route = route
        self.index = 0

    def __str__(self):
        return str(self.loc)

    def getLoc(self):
        return loc

    def setLoc(self, loc):
        self.loc = loc

    def move(self):
        self.index = ((self.index + 1)%len(self.route))
        self.loc = self.route[self.index]

