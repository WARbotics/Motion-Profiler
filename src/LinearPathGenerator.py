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
                        
                        robot_theta = math.degrees(math.atan2(dy, dx))
                        turning_theta = -1*robot_theta
                    
                    else:
                        robot_theta = math.degrees(math.atan2(dy, dx)) - 90# Change this to be like bruces turning angle and theta graph 
                        turning_theta = robot_theta 
                else:
                    robot_theta = math.degrees(math.atan2(dy, dx))
                    turning_theta = robot_theta - self.path[i-1]['robot_theta']
            
                
                self.path.append({
                                    'x': self.waypoints[i].getX(), 
                                    'y': self.waypoints[i].getY(),
                                    'dx': dx, 
                                    'dy': dy, 
                                    'distance': distance, 
                                    'turning_theta': turning_theta,
                                    'robot_theta': robot_theta, 
                                    'time': self.waypoints[i].getTime()
                                })
                print(str({
                                    'x': self.waypoints[i].getX(), 
                                    'y': self.waypoints[i].getY(),
                                    'dx': dx, 
                                    'dy': dy, 
                                    'distance': distance, 
                                    'turning_theta': turning_theta,
                                    'robot_theta': robot_theta, 
                                    'time': self.waypoints[i].getTime()
                                }))
            
    def get_path(self):
        return self.path



    
