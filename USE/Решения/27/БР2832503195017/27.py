import math
from turtle import *


def read_data(filename):
    with open(filename, "r") as file:
        data = [tuple(map(float, line.split())) for line in file]
    return data


def visualize(clusters):
    tracer(0)
    screensize(2500, 2500)
    up()

    k = 1
    colors = ("red", "green", "blue")
    for cl, c in zip(clusters, colors):
        for p in cl:
            x, y = p
            goto(x * k, y * k)
            dot(3, c)
    ht()
    update()


def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)


def solutions(data_cluster):
    clusters = []
    while data_cluster:
        clusters.append([data_cluster.pop()])
        for pt in clusters[-1]:
            neigh = [p for p in data_cluster if euclidean_distance(p, pt) < 20]
            clusters[-1] += neigh
            for p in neigh:
                data_cluster.remove(p)
    # print(len(clusters))
    # visualize(clusters)
    centers = []
    for cl in clusters:
        dmin = 10**1000
        for p in cl:
            d = sum(euclidean_distance(p, pt) for pt in cl)
            if d < dmin:
                dmin = d
                c = p
        centers.append(c)
    px = int(sum(p[0] for p in centers) / len(centers))
    py = int(sum(p[1] for p in centers) / len(centers))
    print(px, py)


if __name__ == "__main__":
    dataA = read_data("USE/27/БР2832503195017/27_A_18884.txt")
    dataB = read_data("USE/27/БР2832503195017/27_B_18884.txt")

    solutions(dataA)

    solutions(dataB)

# 40 -30
# -19 -176
