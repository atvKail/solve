"""
Учёный решил провести кластеризацию некоторого множества звёзд по их расположению на карте звёздного неба.
Кластер звёзд - это набор звёзд (точек) на графике. Каждая звезда обязательно принадлежит только одному из кластеров.
Центр кластера, или центроид, - это одна из звёзд на графике,
сумма расстояний от которой до всех остальных звёзд кластера минимальна.
Расстояние между двумя точками А(x1, у1) и В(х2, у2) вычисляется по формуле:
d(A,b) = V(x1 - x2)2 + (31 - 32)2
Даны два входных файла (файл А и файл Б).
В файле А хранятся данные о звёздах двух кластеров.
В каждой строке записана информация о расположении на карте одной звезды: сначала координата x,
затем координата у (в условных единицах). Известно, что количество звёзд не превышает 1000.
В файле Б хранятся данные о звёздах трёх кластеров. Известно, что количество звёзд не превышает 10000.
Структура хранения информации о звездах в файле Б аналогична файлу А. Возможные данные одного из файлов иллюстрированы графиком.
Кластеры имеют форму «рогалика». Аномалиями назовём точки, находящиеся на расстоянии более одной условной единицы от точек кластеров.
При расчётах аномалии учитывать не нужно. Для каждого файла определите координаты центра каждого кластера,
затем вычислите два числа: Р, - среднее арифметическое абсцисс центров кластеров, и Рy - среднее арифметическое ординат центров кластеров. В ответе запишите четыре числа: в первой строке сначала целую часть произведения Р • 100000, затем целую часть произведения • 100000 для файла А, во второй строке - аналогичные данные для файла Б.
Внимание! График приведён в иллюстративных целях для произвольных значений, не имеющих отношения к заданию.
Для выполнения задания используйте данные из прилагаемого файла.
"""

import math
import random


def read_data(file_name):
    """Считывает данные из файла."""
    with open(file_name, "r") as file:
        lines = file.readlines()
    data = [tuple(map(float, line.replace(",", ".").split())) for line in lines]
    return data


def k_means(points, k, max_iterations=1000):
    """Clusters points into k clusters using the k-means algorithm."""
    # Initialize centroids randomly
    centroids = random.sample(points, k)

    for _ in range(max_iterations):
        # Assign points to the nearest centroid
        clusters = {i: [] for i in range(k)}
        for point in points:
            closest_centroid = min(
                range(k), key=lambda c: euclidean_distance(point, centroids[c])
            )
            clusters[closest_centroid].append(point)

        # Update centroids to be the mean of their cluster
        new_centroids = []
        for i in range(k):
            cluster_points = clusters[i]
            if cluster_points:  # Avoid division by zero
                mean_x = sum(p[0] for p in cluster_points) / len(cluster_points)
                mean_y = sum(p[1] for p in cluster_points) / len(cluster_points)
                new_centroids.append((mean_x, mean_y))
            else:
                new_centroids.append(
                    centroids[i]
                )  # Keep the old centroid if the cluster is empty

        # Check for convergence
        if new_centroids == centroids:
            break
        centroids = new_centroids

    return clusters, centroids


def euclidean_distance(p1, p2):
    """Вычисляет евклидово расстояние между двумя точками."""
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def main():
    data_A = read_data("USE/27/EGE_27A_2025.txt")
    data_B = read_data("USE/27/EGE_27B_2025.txt")

    cluster_A, centroids_A = k_means(data_A, 2)
    cluster_B, centroids_B = k_means(data_B, 3)

    average_arifm_cord = lambda x, d: sum([x[i][d] for i in range(len(x))]) / len(x)

    print(
        "A: ",
        average_arifm_cord(centroids_A, 0) * 100000,
        average_arifm_cord(centroids_A, 1) * 100000,
    )
    print(
        "B: ",
        average_arifm_cord(centroids_B, 0) * 100000,
        average_arifm_cord(centroids_B, 1) * 100000,
    )


if __name__ == "__main__":
    main()


# Неверное решение, вот правильное по мнению составителей:
# Для A:
K = 2  # количество кластеров


def findClusterNo(x, y):
    return (
        0 if y > 2 and (x < 3 or (x < 7 and y < 5)) else 1 if x < 10.5 and y > 1 else -1
    )


clusters = [[] for i in range(K)]

for s in open("27b.txt"):
    x, y = s.replace(",", ".").split()
    x, y = float(x), float(y)
    clusterNo = findClusterNo(x, y)
    if clusterNo >= 0:
        clusters[clusterNo].append((x, y))

import math


def dist(p1, p2):
    return math.hypot(p1[0] - p2[0], p1[1] - p2[1])


centers = []
for k in range(K):
    minSumDist = float("inf")
    for pCenter in clusters[k]:
        sumDist = sum(dist(pCenter, p) for p in clusters[k])
        if sumDist < minSumDist:
            minSumDist = sumDist
            center = pCenter
    centers.append(center)

print("Центроиды:\n", centers)

sumX, sumY = 0, 0
for k in range(K):
    sumX += centers[k][0]
    sumY += centers[k][1]

print(int(sumX / K * 100_000), int(sumY / K * 100_000))

# Для B:

K = 3  # количество кластеров


def findClusterNo(x, y):
    return (
        0
        if (x < 7 and y < 2) or (x < 2 and y < 5)
        else 1
        if y > 0 and y < 5.2 and x < 10
        else 2
        if 1 < x < 11 and 5.2 < y < 10
        else -1
    )


clusters = [[] for i in range(K)]

for s in open("27b.txt"):
    x, y = s.replace(",", ".").split()
    x, y = float(x), float(y)
    clusterNo = findClusterNo(x, y)
    if clusterNo >= 0:
        clusters[clusterNo].append((x, y))

import math


def dist(p1, p2):
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5


centers = []
for k in range(K):
    minSumDist = float("inf")
    for pCenter in clusters[k]:
        sumDist = sum(dist(pCenter, p) for p in clusters[k])
        if sumDist < minSumDist:
            minSumDist = sumDist
            center = pCenter
    centers.append(center)

print("Центроиды:\n", centers)

sumX, sumY = 0, 0
for k in range(K):
    sumX += centers[k][0]
    sumY += centers[k][1]

print(int(sumX / K * 100_000), int(sumY / K * 100_000))
