import numpy as np


class MinDisk(object):
    def __init__(self, points):
        self.points = points

    def _welzl(self):
        n = len(self.points)
        if n == 1:
            return np.array([self.points[0]])
        if n == 2:
            return np.array([self.points[0], self.points[1]])
        # np.random.seed(15)
        points = np.random.permutation(self.points)
        # build a circle D2 around points p1, p2
        D2 = np.array([points[0], points[1]])
        for i in range(2, n):
            if not is_in_circle(D2, points[i]):
                # point[i] lies on the boundary of new minimal circle
                D2 = self._welzl1(points[0:i], points[i])
        return D2

    def _welzl1(self, points, q):
        points = np.random.permutation(points)
        # build a circle D1 around points p1, q
        D1 = np.array([points[0], q])
        for i in range(1, len(points)):
            if not is_in_circle(D1, points[i]):
                D1 = self._welzl2(points[0:i], points[i], q)
        return D1

    def _welzl2(self, points, q1, q2):
        # build a circle D0 around points q1, q2
        D0 = np.array([q1, q2])
        for i in range(0, len(points)):
            if not is_in_circle(D0, points[i]):
                D0 = np.array([points[i], q1, q2])
        return D0

    def find_min_disk(self):
        return self._welzl()


def is_in_circle(D, p):
    if len(D) == 2:
        return int(int(int((p[0] - D[0, 0])) * int((p[0] - D[1, 0]))) + int(int((p[1] - D[0, 1])) * int((p[1] - D[1, 1])))) <= 0

    matrix2 = np.array([
        [D[0, 0], D[0, 1], 1],
        [D[1, 0], D[1, 1], 1],
        [D[2, 0], D[2, 1], 1]
    ])
    if determinant(matrix2) > 0:  # counterclockwise
        matrix = np.array([
            [p[0] ** 2 + p[1] ** 2, p[0], p[1], 1],
            [D[0, 0] ** 2 + D[0, 1] ** 2, D[0, 0], D[0, 1], 1],
            [D[2, 0] ** 2 + D[2, 1] ** 2, D[2, 0], D[2, 1], 1],
            [D[1, 0] ** 2 + D[1, 1] ** 2, D[1, 0], D[1, 1], 1]
        ], dtype=int)
    else:
        matrix = np.array([
            [p[0] ** 2 + p[1] ** 2, p[0], p[1], 1],
            [D[0, 0] ** 2 + D[0, 1] ** 2, D[0, 0], D[0, 1], 1],
            [D[1, 0] ** 2 + D[1, 1] ** 2, D[1, 0], D[1, 1], 1],
            [D[2, 0] ** 2 + D[2, 1] ** 2, D[2, 0], D[2, 1], 1]
        ], dtype=int)

    return determinant(matrix) >= 0


def determinant(M):
    n, _ = np.shape(M)
    if n == 1:
        return int(M[0, 0])
    else:
        summa = 0
        for i in range(n):
            summa += (-1) ** i * int(M[0, i]) * determinant(M[1:, [j for j in range(n) if j != i]])
        return summa


def read_data(file_name: str):
    # print("Data file:", file_name)
    file = open(file_name)
    points = []
    flag = False
    for line in file:
        point = [int(x) for x in line.split()]
        if len(point) != 2:
            print_error(
                "ERROR: Point must have 2 coordinates (x, y), but you have " + str(len(point)) + " coordinates.")
            exit()
        points.append(point)
        flag = True
    file.close()
    if not flag:
        print_error("ERROR: file " + file_name + " is empty.")
        exit()
    return np.array(points)


def print_data(data, filename):
    # print("Circle:", data)
    file = open(filename, 'w')
    for item in data:
        file.write(str(item[0]) + " " + str(item[1]) + "\n")
    file.close()


def print_error(error):
    file = open('output.txt', 'w')
    file.write(error + "\n")
    file.close()
