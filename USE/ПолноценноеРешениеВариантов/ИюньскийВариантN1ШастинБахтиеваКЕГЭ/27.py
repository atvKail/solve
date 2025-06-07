import math


def dist(x1, y1, x2, y2):
    return math.hypot(x1 - x2, y1 - y2)


def readData(path: str) -> list:
    with open(path, "r", encoding="utf-8") as f:
        f.readline()
        return [tuple(map(float, line.strip().split(";"))) for line in f]


def get_all_clusters(points, alpha):
    n = len(points)

    adj = [[] for _ in range(n)]
    for i in range(n):
        xi, yi = points[i]
        for j in range(i + 1, n):
            xj, yj = points[j]
            if dist(xi, yi, xj, yj) <= alpha:
                adj[i].append(j)
                adj[j].append(i)

    visited = [False] * n
    clusters = []
    for i in range(n):
        if not visited[i]:
            stack = [i]
            visited[i] = True
            comp = []
            while stack:
                u = stack.pop()
                comp.append(points[u])
                for v in adj[u]:
                    if not visited[v]:
                        visited[v] = True
                        stack.append(v)
            clusters.append(comp)
    return clusters


def get_cluster_center(cluster):
    return min(cluster, key=lambda x: sum(dist(*x, *p) for p in cluster))


def main():
    path_A = "USE\\ПолноценноеРешениеВариантов\\ИюньскийВариантN1ШастинБахтиеваКЕГЭ\\27A_22623.txt"
    path_B = "USE\\ПолноценноеРешениеВариантов\\ИюньскийВариантN1ШастинБахтиеваКЕГЭ\\27B_22623.txt"

    points_A = readData(path_A)
    points_B = readData(path_B)

    alpha = 2
    H, W = 4, 4

    clusters_A = get_all_clusters(points_A, alpha)
    clusters_B = get_all_clusters(points_B, alpha)

    print("clusters A:", len(clusters_A))
    print("clusters B:", len(clusters_B))

    sizes_A = [len(c) for c in clusters_A]
    sizes_B = [len(c) for c in clusters_B]
    print("A cluster sizes:", sizes_A, "sum:", sum(sizes_A))
    print("B cluster sizes:", sizes_B, "sum:", sum(sizes_B))

    PsA = sum(sizes_A) / (len(sizes_A) * H * W)
    PsB = sum(sizes_B) / (len(sizes_B) * H * W)

    centers_A = [get_cluster_center(c) for c in clusters_A]
    centers_B = [get_cluster_center(c) for c in clusters_B]

    idx_max_A = max(range(len(sizes_A)), key=lambda i: sizes_A[i])
    idx_min_A = min(range(len(sizes_A)), key=lambda i: sizes_A[i])
    idx_max_B = max(range(len(sizes_B)), key=lambda i: sizes_B[i])
    idx_min_B = min(range(len(sizes_B)), key=lambda i: sizes_B[i])

    SpA = dist(*(centers_A[idx_max_A] + centers_A[idx_min_A]))
    SpB = dist(*(centers_B[idx_max_B] + centers_B[idx_min_B]))

    print(int(PsA * 1000), int(SpA * 1000))
    print(int(PsB * 1000), int(SpB * 1000))


if __name__ == "__main__":
    main()

# WA
# Теряет точку 678
