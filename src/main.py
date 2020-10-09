from LinearPathGenerator import LinearPathGenerator
from Waypoint import Waypoint


def main():
    origin_w = Waypoint(0, 0, 0, 0)
    w2 = Waypoint(2, 3, 1, 3)
    w3 = Waypoint(2, 5, 2, 5)
    w4 = Waypoint(3, 5, 3, 8)
    path = LinearPathGenerator([origin_w, w2, w3, w4])
    path.build_path()
    print(path.get_path())


if __name__ == "__main__":
    main()