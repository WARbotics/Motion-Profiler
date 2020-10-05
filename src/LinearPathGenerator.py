import math

class LinearPathGenerator():
    
    # Use graphs to makesure that everything is being correctly setup
     
    def __init__(self, *args, **kwargs):
        self.waypoints = waypoints
        self.path = [] 


    def build_path(self):
        for i in range(len(waypoints)):
            if i > 0:
                dx = waypoints[i].getX() - waypoints[i-1].getX() 
                dy = waypoints[i].getY() - waypoints[i-1].getY()
                distance = math.sqrt((dx*dx) + (dy*dy)) 
                dtheta = math.degrees(math.atan2(dy,dx)) # This is relative. we need a global angle of the robot that is the unit circle 
                if dx > 0:
                    global_theta = self.path[i-1] - theta
                    dtheta = math.degrees(math.atan2(dy,dx))
                else:
                    global_theta = self.path[i-1] + theta
                    dtheta = -1*math.degrees(math.atan2(dy,dx))
                self.path.append({"x": waypoints[i].getX(), 
                                "y": waypoints[i].getY(),
                                "dx": dx, 
                                "dy" dy, 
                                "distnace": distance, 
                                "dtheta": dtheta,
                                "global_theta":global_theta, 
                                "time": waypoints[i].getTime()})
            else: 
                self.path.append({"x": 0, 
                    "y": 0,
                    "dx":0,
                    "dy":0, 
                    "distance": 0, 
                    "dtheta": 0,
                    "global_theta": 90, 
                    "time": 0})
            

    def get_path(self):
        return path



    
