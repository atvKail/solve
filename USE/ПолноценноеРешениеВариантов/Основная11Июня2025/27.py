from math import *
from itertools import permutations


def dist(x1: float, y1: float, x2: float, y2: float) -> float:
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def get_cluster(
    point: tuple[float, float], points: list[tuple[float, float]], alpha: float
) -> list[tuple[float, float]]:
    to_check = [point]
    cluster = [point]
    points.remove(point)

    while to_check:
        cp = to_check.pop()
        for p in points:
            if dist(*cp, *p) <= alpha:
                to_check.append(p)
                cluster.append(p)
                points.remove(p)
    return cluster


def get_all_clusters(
    points: list[tuple[float, float]], alpha: float
) -> list[list[tuple[float, float]]]:
    return [get_cluster(p, points, alpha) for p in points]


def get_cluster_centroid(cluster):
    return min(cluster, key=lambda x: sum(dist(*x, *p) for p in cluster))


def get_clusters_centroid(
    clusters: list[list[tuple[float, float]]],
) -> list[tuple[float, float]]:
    return [get_cluster_centroid(cluster) for cluster in clusters]


def read_data(path: str) -> list[tuple[float, float]]:
    data = []
    with open(path, "r") as f:
        f.readline()
        while line := f.readline().strip():
            data.append(tuple(map(float, line.replace(",", ".").split())))
    return data


if __name__ == "__main__":
    path_A = "USE\\ПолноценноеРешениеВариантов\\Основная11Июня2025\\27_A_23284.txt"
    path_B = "USE\\ПолноценноеРешениеВариантов\Основная11Июня2025\\27_B_23284.txt"

    data_A = read_data(path_A)
    data_B = read_data(path_B)

    alpha_A = 3
    # alpha_B = 0.6

    clusters_A = get_all_clusters(points=data_A, alpha=alpha_A)
    # clusters_B = get_all_clusters(points=data_B, alpha=alpha_B)

    # clusters_B = [cluster for cluster in clusters_B if len(cluster) > 1]

    centroids_A = get_clusters_centroid(clusters_A)
    # centroids_B = get_clusters_centroid(clusters_B)

    print(
        int(sum(x for x, _ in centroids_A) * 10000),
        int(sum(x for _, x in centroids_A) * 10000)
    )

    # print(
    #     int(min([dist(*x, *y) for x, y in permutations(centroids_B, 2)]) * 10000),
    #     int(max([dist(*x, *y) for x, y in permutations(centroids_B, 2)]) * 10000)
    # )

    # print(len(data_B))
    clusters_B = [[], [], []]
    while data_B:
        p = data_B.pop()
        # print(p)
        if p[1] > 20 and p[1] < 40:
            
            if p[0] < 10:
                clusters_B[0].append(p)
            elif p[0] < 20:
                clusters_B[1].append(p)
            else:
                clusters_B[2].append(p)
    # print([len(i) for i in clusters_B])
    centroids_B = get_clusters_centroid(clusters_B)

    print(
        int(min([dist(*x, *y) for x, y in permutations(centroids_B, 2)]) * 10000),
        int(max([dist(*x, *y) for x, y in permutations(centroids_B, 2)]) * 10000)
    )
