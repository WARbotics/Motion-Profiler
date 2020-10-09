
class LinearTrajectoryGenerator():

    # The big isseu with a linear trajectory generator is that it is 1D you 
    # cannot have theta in it 
    # this likely used for just simple demostration

    def __init__(self):
        self.path = []
        self.trajectory = []
        self.MAX_V = None
        self.MAX_A = None

    def build_trajectory(self):
        for i in range(len(self.path)):
            # We assume in this case that we are acting at starting at 0 m/s because we are starting and stopping
            # if turn turn first then move linear move 
            if 

    
            # what is the maxium we possibly could go if we had no contraints
            # Note that would be area of the acceleration and the deceration equal the distance travel
            v_cruise = min(self.MAX_V, (self.MAX_A*(self.path[i]['time']*self.path[i]['time'])/2)) # WIP looking at Cheesy poofs(254) presentation on trapzoidal motion profiles
            # Figure out how much distance you will cover to accelerate from v_start to v_cruise dx = 1/2at^2
            acceleration_time = v_cruise/self.MAX_A
            acceleration_distance = (1/2*self.MAX_A *
                                    (acceleration_time) *
                                    (acceleration_time))  # Because this trapzoidal both acceleration have the same distance
            cruise_time = (acceleration_distance * 2) - self.path[i]['distance']
                # Possibly make a motion profile object that you can pass time it would return a a,x,t,v 
                            
    def getTrajectory(self):
        return self.trajectory
