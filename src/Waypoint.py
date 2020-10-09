class Waypoint:

    def __init__(self, x, y, seq, time):
        self.x = x  # Meters from the origin 
        self.y = y 
        self.seq = seq
        self.time = time

    def getX(self,):
        return self.x

    def getY(self):
        return self.y
 
    def getSeq(self):
        return self.seq

    def setAsOrigin(self):
        self.isOrigin = True
        self.time = 0

    def getTime(self):
        return self.time
