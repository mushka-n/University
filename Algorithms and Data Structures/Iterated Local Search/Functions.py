from scipy.spatial import distance
from Dot import Dot
from math import sqrt


def Read_File():
    fileLines = open('data.txt', 'r').readlines()
    dots_num = int(fileLines[0])
    dots, distances = [], [[]] * dots_num

    for i in range(1, dots_num + 1):
        new_dot = list(map(int, (fileLines[i]).split()))
        dots.append(Dot(new_dot[0], new_dot[1], new_dot[2]))

    for i in range(dots_num):
        dot_distances = []
        for j in range(dots_num):
            dot_distances.append(round(distance.euclidean(dots[i].Coords(), dots[j].Coords()), 3))
        distances[i] = dot_distances
    return dots_num, dots, distances
