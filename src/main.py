from LinearPathGenerator import LinearPathGenerator
from Waypoint import Waypoint
from LinearTrajectoryGenerator import LinearTrajectoryGenerator 


def main():
    origin_w = Waypoint(0, 0, 0, 0)
    # w1 = Waypoint(-2, 3, 1, 3)
    w2 = Waypoint(.2, .3, 2, 6)
    w3 = Waypoint(.7, .6, 3, 12)
    w4 = Waypoint(1, 1.2, 4, 18)
    path = LinearPathGenerator([origin_w, w2, w3, w4])
    path.build_path()
    trajectory = LinearTrajectoryGenerator(path.get_path(), .5, .05, .2, .025)
    trajectory.build_trajectory()
    #print(str(trajectory.getTrajectory()))



if __name__ == "__main__":
    main()