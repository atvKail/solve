file_a = "USE\\Решения\\27\\21932\\27_A_21932.txt"
file_b = "USE\\Решения\\27\\21932\\27_B_21932.txt"


import math


def dist(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def readData(path: str) -> list:
    with open(path, "r") as f:
        data = [tuple(map(float, line.strip().split(";"))) for line in f.readlines()]
    return data


def find_cluster(points, point, alpha):
    cluster = [point]
    to_check = [point]
    points.remove(point)

    while to_check:
        p = to_check.pop()
        for other_point in points:
            if dist(*p, *other_point) <= alpha:
                to_check.append(other_point)
                cluster.append(other_point)
                points.remove(other_point)
    return cluster


def get_all_clusters(points, alpha):
    clusters = []
    while points:
        point = points[0]
        clusters.append(find_cluster(points, point, alpha))
    return clusters


def get_cluster_center(cluster):
    return min(cluster, key=lambda x: sum(dist(*x, *p) for p in cluster))


def get_cluster_centers(clusters):
    return [get_cluster_center(cluster) for cluster in clusters]


def main() -> int:
    points_A = readData(file_a)
    points_B = readData(file_b)

    alpha_A = 1
    alpha_B = 1

    clusters_A = get_all_clusters(points_A, alpha_A)
    clusters_B = get_all_clusters(points_B, alpha_B)

    print("clusters A: {}".format(len(clusters_A)))
    print("clusters B: {}".format(len(clusters_B)))

    centers_A = get_cluster_centers(clusters_A)
    centers_B = get_cluster_centers(clusters_B)

    clusters_A = [[centers_A[i], clusters_A[i]] for i in range(len(centers_A))]
    clusters_B = [[centers_B[i], clusters_B[i]] for i in range(len(centers_B))]

    print(
        int(min(clusters_A, key=lambda x: len(x[1]))[0][0] * 10000),
        int(max(clusters_A, key=lambda x: len(x[1]))[0][1] * 10000),
    )
    print(
        int(min(clusters_B, key=lambda x: len(x[1]))[0][0] * 10000),
        int(max(clusters_B, key=lambda x: len(x[1]))[0][1] * 10000),
    )


1


if __name__ == "__main__":
    main()
