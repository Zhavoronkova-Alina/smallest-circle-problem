import sys

from min_disk import *
from test import *


def main():
    if len(sys.argv) != 2:
        print_error("ERROR: There are must be one data file.")
        exit()
    points = read_data(sys.argv[1])
    min_disk_1 = MinDisk(points)
    circle = min_disk_1.find_min_disk()
    print_data(circle, "output.txt")
    # test_min_disk_0_points()
    # test_min_disk_1_point()
    # test_min_disk_2_points()
    # test_min_disk_3_points_diam()
    # test_min_disk_3_points()
    # test_min_disk_6_points()
    # test_min_disk_5_points()
    # test_min_disk_points_on_line()
    # test_min_disk_points()
    # matrix2 = np.array([
    #     [43705, 179, 108, 1],
    #     [1496500, 804, 922, 1],
    #     [911837, 949, 106, 1],
    #     [319729, 345, 448, 1]
    # ])
    # print(determinant(matrix2))


if __name__ == '__main__':
    main()
