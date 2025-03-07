import csv
from math import sqrt


def read_data(file: str, mode="r", encoding="utf-8", func_format=lambda x: x) -> list:
    data = []
    with open(file, mode=mode, encoding=encoding) as f:
        reader = csv.DictReader(f, delimiter=",")
        for row in reader:
            row["X"] = float(row["X"].replace(",", "."))
            row["Y"] = float(row["Y"].replace(",", "."))
            data.append(row)
    return data


def dist(x1, y1, x2, y2):
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def find_clusters(cond, data):
    clusters = {}
    for row in data:
        x = row["X"]
        y = row["Y"]
        assigned_cluster = 0
        for c in cond:
            cid = c(x, y)
            if cid != 0:
                assigned_cluster = cid
                break
        if assigned_cluster not in clusters:
            clusters[assigned_cluster] = []
        clusters[assigned_cluster].append((x, y))
    return clusters


def calculating_dist(points, px, py):
    total = 0
    for xi, yi in points:
        total += dist(px, py, xi, yi)
    return total


def get_cluster_averages(clusters):
    results = {}
    for cid, points in clusters.items():
        best_point = None
        best_sum = None
        for point in points:
            d_sum = calculating_dist(points, point[0], point[1])
            if best_sum is None or d_sum < best_sum:
                best_sum = d_sum
                best_point = point
        results[cid] = best_point
    return results


def main(files, cluster_cond_A, cluster_cond_B):
    data_A = read_data(
        file=files[0],
        mode="r",
        encoding="utf-8",
        func_format=lambda x: x.replace(",", "."),
    )
    data_B = read_data(
        file=files[1],
        mode="r",
        encoding="utf-8",
        func_format=lambda x: x.replace(",", "."),
    )

    clusters_A = find_clusters(cond=cluster_cond_A, data=data_A)
    clusters_B = find_clusters(cond=cluster_cond_B, data=data_B)

    # clusters_A.pop(min(clusters_A, key=lambda cid: len(clusters_A[cid])))
    clusters_A.pop(max(clusters_A, key=lambda cid: len(clusters_A[cid])))

    # clusters_B.pop(min(clusters_B, key=lambda cid: len(clusters_B[cid])))
    clusters_B.pop(max(clusters_B, key=lambda cid: len(clusters_B[cid])))

    clusters_average_A = get_cluster_averages(clusters_A)
    clusters_average_B = get_cluster_averages(clusters_B)

    sum_x_A, sum_y_A = 0, 0
    count_A = len(clusters_average_A)
    for x, y in clusters_average_A.values():
        sum_x_A += x
        sum_y_A += y
    avg_x_A = sum_x_A / count_A
    avg_y_A = sum_y_A / count_A
    result_A_x = int(avg_x_A * 10000)
    result_A_y = int(avg_y_A * 10000)

    sum_x_B, sum_y_B = 0, 0
    count_B = len(clusters_average_B)
    for x, y in clusters_average_B.values():
        sum_x_B += x
        sum_y_B += y
    avg_x_B = sum_x_B / count_B
    avg_y_B = sum_y_B / count_B
    result_B_x = int(avg_x_B * 10000)
    result_B_y = int(avg_y_B * 10000)

    print(result_A_x, result_A_y)
    print(result_B_x, result_B_y)


if __name__ == "__main__":
    files = [
        "USE\\27\\Занятия в цдо\\data\\1_A.csv",
        "USE\\27\\Занятия в цдо\\data\\1_27B.csv",
    ]

    cluster_cond_A = [
        lambda x, y: 1 if y < 2 else 0,
        lambda x, y: 2 if 2 < y < 5.5 else 0,
        lambda x, y: 3 if y > 5.5 else 0,
    ]
    cluster_cond_B = [
        lambda x, y: 1 if (x < 1) and (y < 2) else 0,
        lambda x, y: 2 if (x < 3) and (y > 2) else 0,
        lambda x, y: 3 if (x > 3) and (y < 1) else 0,
        lambda x, y: 4 if (x > 3) and (1 < y < 5) else 0,
        lambda x, y: 5 if (x > 3) and (y > 5) else 0,
    ]

    main(files=files, cluster_cond_A=cluster_cond_A, cluster_cond_B=cluster_cond_B)
    """
    Формулировка задачи странная, очень даже, ответ А подходит, ответ Б чуть-чуть не подходит, хотя очень странно.
    """
