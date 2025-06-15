# import sys
# import bisect


# input = sys.stdin.readline

# t = int(input())
# horizontals = []
# verticals = []
# for i in range(1, t + 1):
#     x1, y1, x2, y2 = map(int, input().split())
#     if y1 == y2:
#         xmin, xmax = min(x1, x2), max(x1, x2)
#         horizontals.append((xmin, xmax, y1, i))
#     else:
#         ymin, ymax = min(y1, y2), max(y1, y2)
#         verticals.append((x1, ymin, ymax, i))

# events = []
# for xmin, xmax, y, idH in horizontals:
#     events.append((xmin, 0, y, idH))
#     events.append((xmax, 2, y, idH))
# for x, ymin, ymax, idV in verticals:
#     events.append((x, 1, ymin, ymax, idV))

# events.sort(key=lambda x: (x[0], x[1]))

# active = []
# id_to_y = {}
# flagH = [False] * (t + 1)
# flagV = [False] * (t + 1)

# for ev in events:
#     if ev[1] == 0:
#         _, _, y, idH = ev
#         bisect.insort(active, (y, idH))
#         id_to_y[idH] = y
#     elif ev[1] == 2:
#         _, _, y, idH = ev
#         pos = bisect.bisect_left(active, (y, idH))
#         if pos < len(active) and active[pos] == (y, idH):
#             active.pop(pos)
#     else:
#         _, _, ymin, ymax, idV = ev
#         l = bisect.bisect_right(active, (ymin, 10**18))
#         r = bisect.bisect_left(active, (ymax, -(10**18)))
#         if l < r:
#             flagV[idV] = True
#             for y, idH in active[l:r]:
#                 flagH[idH] = True

# ans = 0
# for i in range(1, t + 1):
#     if flagH[i] or flagV[i]:
#         ans += 1
# print(ans)


# def ntod(x: str, n: int) -> int:
#     import string

#     alph = "0123456789" + string.ascii_uppercase
#     num = list(x)
#     dnum = sum(alph.index(num[i]) * n ** (len(num) - i - 1) for i in range(len(num)))
#     return dnum


# print(ntod("2N04", 36))

# print(2 & 1 == 0)


# def dbscan(points, eps, min_pts):
#     labels = [None] * len(points)
#     cluster_id = 0
#     for i in range(len(points)):
#         if labels[i] is not None:
#             continue

#         neighbors = []
#         for j in range(len(points)):
#             dx = points[i][0] - points[j][0]
#             dy = points[i][1] - points[j][1]
#             if dx * dx + dy * dy <= eps * eps:
#                 neighbors.append(j)

#         if len(neighbors) < min_pts:
#             labels[i] = -1
#         else:
#             cluster_id += 1
#             labels[i] = cluster_id
#             k = 0

#             while k < len(neighbors):
#                 j = neighbors[k]
#                 if labels[j] == -1:
#                     labels[j] = cluster_id
#                 if labels[j] is None:
#                     labels[j] = cluster_id

#                     new_neighbors = []
#                     for m in range(len(points)):
#                         dx = points[j][0] - points[m][0]
#                         dy = points[j][1] - points[m][1]
#                         if dx * dx + dy * dy <= eps * eps:
#                             new_neighbors.append(m)

#                     if len(new_neighbors) >= min_pts:
#                         neighbors += new_neighbors
#                 k += 1
#     return labels

