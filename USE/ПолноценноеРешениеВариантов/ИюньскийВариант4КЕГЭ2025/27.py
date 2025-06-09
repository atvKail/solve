import math


def dist(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def readData(path: str) -> list:
    with open(path, "r") as f:
        f.readline()
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
    path_A = "USE\\ПолноценноеРешениеВариантов\\ИюньскийВариант4КЕГЭ2025\\27A_22624.txt"
    path_B = "USE\\ПолноценноеРешениеВариантов\\ИюньскийВариант4КЕГЭ2025\\27B_22624.txt"

    points_A = readData(path_A)
    points_B = readData(path_B)

    alpha_A = 1
    alpha_B = 1

    clusters_A = get_all_clusters(points_A, alpha_A)
    clusters_B = get_all_clusters(points_B, alpha_B)

    clusters_A = [clusters_A[i] for i in range(len(clusters_A)) if len(clusters_A[i]) > 5]
    clusters_B = [clusters_B[i] for i in range(len(clusters_B)) if len(clusters_B[i]) > 5]

    print("clusters A: {}".format(len(clusters_A)))
    print("clusters B: {}".format(len(clusters_B)))

    centers_A = get_cluster_centers(clusters_A)
    centers_B = get_cluster_centers(clusters_B)

    print(
        int(sum([x for x, _ in centers_A]) / len(centers_A) * 10000),
        int(sum([x for _, x in centers_A]) / len(centers_A) * 10000),
    )
    print(
        int(sum([x for x, _ in centers_B]) / len(centers_B) * 10000),
        int(sum([x for _, x in centers_B]) / len(centers_B) * 10000),
    )


if __name__ == "__main__":
    main()
