from LinearPathGenerator import LinearPathGenerator
from Waypoint import Waypoint
from LinearTrajectoryGenerator import LinearTrajectoryGenerator 


def main():
    origin_w = Waypoint(0, 0, 0, 0)
    # w1 = Waypoint(-2, 3, 1, 3)
    w2 = Waypoint(2, 3, 2, 20)
    w3 = Waypoint(2, 5, 3, 40)
    w4 = Waypoint(3, 5, 4, 60)
    path = LinearPathGenerator([origin_w, w2, w3, w4])
    path.build_path()
    trajectory = LinearTrajectoryGenerator(path.get_path(), 4, 2, 2, 1)
    trajectory.build_trajectory()
    #print(str(trajectory.getTrajectory()))



if __name__ == "__main__":
    main()