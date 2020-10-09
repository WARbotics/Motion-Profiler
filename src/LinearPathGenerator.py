import math


class LinearPathGenerator:
    
    # Use graphs to makesure that everything is being correctly setup
     
    def __init__(self, waypoints):
        self.waypoints = waypoints
        self.path = []

    def build_path(self):
        for i in range(len(self.waypoints)):
            if i < len(self.waypoints)-1:
                dx = self.waypoints[i+1].getX() - self.waypoints[i].getX()
                dy = self.waypoints[i+1].getY() - self.waypoints[i].getY()  
                distance = math.sqrt((dx*dx) + (dy*dy)) 
        
                if i == 0:
                    if dx > 0:
                        
                        dtheta = math.degrees(math.atan2(dy, dx))
                        global_theta = 90 - dtheta
                    else:
                        dtheta = -1*math.degrees(math.atan2(dy, dx)) # Change this to be like bruces turning angle and theta graph 
                        global_theta = 90 + dtheta
                else:
                    if dx > 0:
                        dtheta = math.degrees(math.atan2(dy, dx)) - self.path[i-1]['dtheta']
                        global_theta = self.path[i-1]['global_theta'] - dtheta
                    else:
                        dtheta = math.degrees(math.atan2(dy, dx)) - self.path[i-1]['dtheta']
                        dtheta = -1*dtheta
                        global_theta = self.path[i-1]['global_theta'] + dtheta # <------this is a mess and I dont know wtf is going on!
                self.path.append({
                                    'x': self.waypoints[i].getX(), 
                                    'y': self.waypoints[i].getY(),
                                    'dx': dx, 
                                    'dy': dy, 
                                    'distnace': distance, 
                                    'dtheta': dtheta,
                                    'global_theta': global_theta, 
                                    'time': self.waypoints[i].getTime()
                                })
                print(str({
                                    'x': self.waypoints[i].getX(), 
                                    'y': self.waypoints[i].getY(),
                                    'dx': dx, 
                                    'dy': dy, 
                                    'distnace': distance, 
                                    'dtheta': dtheta,
                                    'global_theta': global_theta, 
                                    'time': self.waypoints[i].getTime()
                                }))
            
    def get_path(self):
        return self.path



    
