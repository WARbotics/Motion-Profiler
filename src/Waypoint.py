class Waypoint:
    x = None
    y = None 
    theta = None
    seq = None
    isOrigin = False

    def __init__(self, *args, **kwargs):
        self.x = x  # Meters from the origin 
        self.y = y 
        self.theta = theta
        self.seq = seq

    def getX(self,):
        return self.x

    def getY(self):
        return self.y;

    def getTheta(self):
        return self.theta
    
    def getSeq(self):
        return self.seq

    def setAsOrigin(self):
        self.isOrigin = True


