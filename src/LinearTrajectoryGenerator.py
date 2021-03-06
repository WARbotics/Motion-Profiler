import math
import cmath

class LinearTrajectoryGenerator():

    # The big isseu with a linear trajectory generator is that it is 1D you 
    # cannot have theta in it 
    # this likely used for just simple demostration

    def __init__(self, path, MAX_V, MAX_A, MAX_TURNING_V, MAX_TURNING_A):
        self.path = path
        self.trajectory = []
        self.MAX_V = MAX_V
        self.MAX_A = MAX_A
        self.MAX_TURNING_V = MAX_TURNING_V
        self.MAX_TURNING_A = MAX_TURNING_A
        
    def build_trajectory(self):
        for i in range(len(self.path)):
            
            if abs(self.path[i]['turning_theta']) > 0 and (i+1 < len(self.path)): 
                travel_time = self.path[i+1]['time'] - self.path[i]['time']
                turning = self.make_trapzoidal_profile_turning(float(travel_time)*(.25), self.path[i]['turning_theta'])
                forward = self.make_trapzoidal_profile(float(travel_time)*(.75), self.path[i]['distance'])

                self.trajectory.append({
                    "turning": {    
                        "v_cruise": turning['v_cruise'],
                        "cruise_time": turning['cruise_time'],
                        "acceleration_time": turning['acceleration_time'],
                        "decceleration_time": turning['decceleration_time'],
                        "theta": self.path[i]['turning_theta']
                    },
                    "forward": {
                        "v_cruise": forward['v_cruise'],
                        "cruise_time": forward['cruise_time'], 
                        "acceleration_time": forward['acceleration_time'],
                        "decceleration_time": forward['decceleration_time'], 
                        "distance": self.path[i]['distance']
                    }
                }) 
                print(self.trajectory[i-1])
            elif (i+1 < len(self.path)):
                travel_time = self.path[i+1]['time'] - self.path[i]['time']
                if i > 0:
                    travel_time = travel_time - self.trajectory[i]['travel_time']
                forward = self.make_trapzoidal_profile(travel_time, self.path[i]['distance'])
                
                self.trajectory.append({
                    "turning": {    
                        "v_cruise": 0,
                        "cruise_time": 0,
                        "acceleration_time": 0,
                        "decceleration_time": 0,
                        "theta": 0
                    },
                    "forward": {
                        "v_cruise": forward['v_cruise'],
                        "cruise_time": forward['cruise_time'], 
                        "acceleration_time": forward['acceleration_time'],
                        "decceleration_time": forward['decceleration_time'], 
                        "distance": self.path[i]['distance']
                    }
                }) 
                print(self.trajectory[i-1])

    def make_trapzoidal_profile(self, time, distance):
        v_cruise = min(self.MAX_V, (.5*self.MAX_A*(time/2)*(time/2))) 
        #  Figure out how much distance you will cover to accelerate from v_start to v_cruise dx = 1/2at^2
        
        acceleration_time = v_cruise/self.MAX_A
        acceleration_distance = ((1/2)*self.MAX_A *
                                (acceleration_time) *
                                (acceleration_time))  # Because this trapzoidal both acceleration have the same distance
        cruise_time = time - (2*acceleration_time)
        cruise_distance = v_cruise * cruise_time
        print("Acceleration_time: " + str(acceleration_time))
        print("cruise_time: "+ str(cruise_time))
        print("cruise_distance: "+str(cruise_distance))
        return {"v_cruise": v_cruise, "acceleration_time": acceleration_time, "decceleration_time": acceleration_time,"cruise_time": cruise_time, "travel_time": ((acceleration_time*2) + cruise_time)}

    def make_trapzoidal_profile_turning(self, time, theta):
        v_cruise = min([self.MAX_TURNING_V, (self.MAX_TURNING_A*(time/2))]) 
        #  Figure out how much distance you will cover to accelerate from v_start to v_cruise dx = 1/2at^2
        acceleration_time = v_cruise/self.MAX_TURNING_A
        acceleration_distance = ((1/2)*self.MAX_TURNING_A *
                                (acceleration_time) *
                                (acceleration_time))  # Because this trapzoidal both acceleration have the same distance
        cruise_time = time - (2*acceleration_time)

        return {"v_cruise": v_cruise, "acceleration_time": acceleration_time, "decceleration_time": acceleration_time,"cruise_time": cruise_time, "travel_time": ((acceleration_time*2) + cruise_time)}
    
    def getTrajectory(self):
        return self.trajectory
