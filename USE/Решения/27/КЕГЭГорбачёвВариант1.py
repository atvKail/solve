import math

def processfiles(file_path):
    points = []
    with open(file=file_path, mode="r", encoding="utf-8") as file:
        for line in file:
            parts = line.strip().split()
            if not parts:
                continue
            try:
                x, y = map(float, parts)
                points.append((x, y))
            except ValueError:
                continue
    return points

def cluster_points(points, W, H):
    n = len(points)
    assigned = [False] * n
    clusters = []
    
    for i in range(n):
        if not assigned[i]:
            cluster = [points[i]]
            assigned[i] = True
            changed = True
            while changed:
                changed = False
                for j in range(n):
                    if not assigned[j]:
                        new_cluster = cluster + [points[j]]
                        xs = [p[0] for p in new_cluster]
                        ys = [p[1] for p in new_cluster]
                        if (max(xs) - min(xs) <= W) and (max(ys) - min(ys) <= H):
                            cluster.append(points[j])
                            assigned[j] = True
                            changed = True
            clusters.append(cluster)
    return clusters

def find_medoid(cluster):
    best_point = None
    best_sum = float('inf')
    for p in cluster:
        s = 0.0
        for q in cluster:
            dx = p[0] - q[0]
            dy = p[1] - q[1]
            s += math.hypot(dx, dy)
        if s < best_sum:
            best_sum = s
            best_point = p
    return best_point

def solve(files_pathes):
    W = 3
    H = 6
    
    results = []
    for file_path in files_pathes:
        points = processfiles(file_path)
        clusters = cluster_points(points, W, H)
        
        medoids = []
        for cluster in clusters:
            medoid = find_medoid(cluster)
            medoids.append(medoid)

        if medoids:
            sum_x = sum(p[0] for p in medoids)
            sum_y = sum(p[1] for p in medoids)
            Px = sum_x / len(medoids)
            Py = sum_y / len(medoids)
        else:
            Px, Py = 0, 0
        
        res_x = abs(int(Px * 100000))
        res_y = abs(int(Py * 100000))
        results.append((res_x, res_y))

    for res in results:
        print(res[0], res[1])

if __name__ == "__main__":
    files_pathes = [
        "USE\\27\\data\\27A_18157.txt", 
        "USE\\27\\data\\27B_18157.txt"
    ]
    solve(files_pathes)
