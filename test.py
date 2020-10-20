from min_disk import *


def test_min_disk_0_points(filename="data1.txt"):
    points = read_data(filename)
    min_disk_1 = MinDisk(points)
    circle = min_disk_1.find_min_disk()
    print_data(circle, "output1.txt")


def test_min_disk_1_point():
    points = np.array([
        [1, 2]
    ])
    min_disk_1 = MinDisk(points)
    circle = min_disk_1.find_min_disk()
    print_data(circle, "output2.txt")


def test_min_disk_2_points():
    points = np.array([
        [1, 2],
        [3, 4]
    ])
    min_disk_1 = MinDisk(points)
    circle = min_disk_1.find_min_disk()
    print_data(circle, "output3.txt")


def test_min_disk_3_points_diam():
    points = np.array([
        [1, 2],
        [3, 4],
        [5, 6]
    ])
    min_disk_1 = MinDisk(points)
    circle = min_disk_1.find_min_disk()
    print_data(circle, "output4.txt")


def test_min_disk_3_points():
    points = np.array([
        [-2, 0],
        [2, 0],
        [0, 3]
    ])
    min_disk_1 = MinDisk(points)
    circle = min_disk_1.find_min_disk()
    print_data(circle, "output5.txt")


def test_min_disk_6_points():
    points = np.array([
        [2, 4],
        [-2, 4],
        [1, 3],
        [-1, 3],
        [0, 2],
        [0, 0]
    ])
    min_disk_1 = MinDisk(points)
    circle = min_disk_1.find_min_disk()
    print_data(circle, "output6.txt")


def test_min_disk_5_points():
    points = np.array([
        [6, 3],
        [1, -2],
        [2, 4],
        [-3, 6],
        [0, 0]
    ])
    min_disk_1 = MinDisk(points)
    circle = min_disk_1.find_min_disk()
    print_data(circle, "output7.txt")


def test_min_disk_points_on_line():
    points = np.array([
        [0, 0],
        [1, 1],
        [2, 2],
        [3, 3],
        [4, 4],
        [5, 5]
    ])
    min_disk_1 = MinDisk(points)
    circle = min_disk_1.find_min_disk()
    print_data(circle, "output8.txt")


def test_min_disk_points():
    points = np.array([
        [0, 0],
        [1, 1],
        [-1, 1],
        [1, -1],
        [-1, -1],
        [0, 2],
        [2, 0],
        [0, -2],
        [-2, 0],
    ])
    min_disk_1 = MinDisk(points)
    circle = min_disk_1.find_min_disk()
    print_data(circle, "output9.txt")

