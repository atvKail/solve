from math import sqrt


def dist(x1: float, y1: float, x2: float, y2: float) -> float:
    return sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2))


def readData(path: str) -> list[tuple[float, float]]:
    with open(path, "r") as f:
        f.readline()
        data = [tuple(map(float, line.strip().replace(',', '.').split())) for line in f.readlines()]
    return data


def find_cluster(point: tuple[float, float], points: list[float], alpha: float) -> list[tuple[float, float]]:
    to_check = [point]
    cluster = [point]
    points.remove(point)

    while to_check:
        pc = to_check.pop()
        for p in points:
            if dist(*pc, *p) <= alpha:
                to_check.append(p)
                cluster.append(p)
                points.remove(p)
    return cluster


def find_all_clusters(points: list[tuple[float, float]], alpha: float) -> list[list[tuple[float, float]]]:
    clusters = []
    while points:
        p = points[0]
        clusters.append(find_cluster(p, points, alpha))
    return clusters


def get_cluster_center(cluster: list[tuple[float, float]]) -> tuple[float, float]:
    return min(cluster, key=lambda x: sum(dist(*x, *p) for p in cluster))


def get_cluster_centers(clusters: list[list[tuple[float, float]]]) -> list[tuple[float, float]]:
    return [get_cluster_center(cluster) for cluster in clusters]


def main() -> int:
    path_A = "USE\\ПолноценноеРешениеВариантов\\Основная10Июня2025\\27_A_23209.txt"
    path_B = "USE\\ПолноценноеРешениеВариантов\\Основная10Июня2025\\27_B_23209.txt"

    data_A = readData(path=path_A)
    data_B = readData(path=path_B)

    alpha_A = 5
    alpha_B = 2

    clusters_A = find_all_clusters(points=data_A, alpha=alpha_A)
    clusters_B = find_all_clusters(points=data_B, alpha=alpha_B)

    clusters_B = [cluster for cluster in clusters_B if len(cluster) > 1 ]

    print(f"cluster A -> ", len(clusters_A))
    print(f"cluster B -> ", len(clusters_B))

    centers_A = get_cluster_centers(clusters_A)

    print(
        int(max([x for x, _ in centers_A]) * 10000),
        int(max([x for _, x in centers_A]) * 10000),
    )

    min_cl_B = min(clusters_B, key=lambda x: len(x))
    max_cl_B = max(clusters_B, key=lambda x: len(x))

    print(
        int(abs(get_cluster_center(min_cl_B)[0] - get_cluster_center(max_cl_B)[0]) * 10000),
        int(abs(get_cluster_center(min_cl_B)[1] - get_cluster_center(max_cl_B)[1]) * 10000)
    )
    return 0


if __name__ == "__main__":
    main()
