# import heapq


# def dijkstra(graph, start, n):
#     distances = {i: float("infinity") for i in range(1, n + 1)}
#     distances[start] = 0
#     priority_queue = [(0, start)]

#     while priority_queue:
#         current_distance, current_vertex = heapq.heappop(priority_queue)

#         if current_distance > distances[current_vertex]:
#             continue

#         for neighbor, weight in graph[current_vertex].items():
#             distance = current_distance + weight
#             if distance < distances[neighbor]:
#                 distances[neighbor] = distance
#                 heapq.heappush(priority_queue, (distance, neighbor))

#     return distances


# n, m = map(int, input().split())
# graph = {i: {} for i in range(1, n + 1)}

# for _ in range(m):
#     u, v, c = map(int, input().split())
#     graph[u][v] = min(graph[u].get(v, float("infinity")), c)
#     graph[v][u] = min(graph[v].get(u, float("infinity")), c)

# a, b = map(int, input().split())

# distances = dijkstra(graph, a, n)

# print(distances[b] if distances[b] != float("infinity") else -1)


# n, m, k = map(int, input().split())

# if k == 0:
#     print(-1)
#     exit()

# roads = []
# for _ in range(m):
#     u, v, l = map(int, input().split())
#     roads.append((u, v, l))

# storages = set(map(int, input().split()))

# min_cost = float("infinity")
# for u, v, l in roads:
#     if (u in storages and v not in storages) or (v in storages and u not in storages):
#         min_cost = min(min_cost, l)

# print(min_cost if min_cost != float("infinity") else -1)

#############Задачи олимпиады "Олимпиада регион 2022-23"
######################Задача A. Разделение прямоугольника
# from math import sqrt, ceil


# for _ in range(int(input())):
#     a, b, k, m = map(int, input().split())

#     D = k**2 - 4 * m + 4 * k + 4
#     if D < 0:
#         print(-1)
#     else:
#         v = [(k + sqrt(D)) / 2, (k - sqrt(D)) / 2]
#         h = [float("inf"), float("inf")]

#         if ceil(v[0]) != int(v[0]):
#             v[0] = b
#         if ceil(v[1]) != int(v[1]):
#             v[1] = b

#         if 0 <= v[0] < b and 0 <= k - v[0] < a:
#             v[0] = int(v[0])
#             h[0] = k - v[0]
#         if 0 <= v[1] < b and 0 <= k - v[1] < a:
#             v[1] = int(v[1])
#             h[1] = k - v[1]

#         ans = min((v[0], h[0]), (v[1], h[1]), key=lambda x: x[1])
#         if ans[1] == float("inf"):
#             print(-1)
#         else:
#             print(*ans[::-1])

##################### Задача B. Произведение Фибоначчи
# def fibonacci_up_to(n):
#     fib = [1, 1]
#     while fib[-1] <= n:
#         fib.append(fib[-1] + fib[-2])
#     return [x for x in fib if x > 1]


# def count_fib_products(n, fib, index):
#     if n == 1:
#         return 1
#     if n < 1 or index < 0:
#         return 0

#     count = 0
#     if n % fib[index] == 0:
#         count += count_fib_products(n // fib[index], fib, index)
#     count += count_fib_products(n, fib, index - 1)
#     return count


# def count_fibonacci_products(n):
#     fib = fibonacci_up_to(n)
#     return count_fib_products(n, fib, len(fib) - 1)


# for _ in range(int(input())):
#     n = int(input())
#     print(count_fibonacci_products(n))

# ############################Задача C. Робот-пылесос
# directions = {"E": (1, 0), "N": (0, 1), "W": (-1, 0), "S": (0, -1)}

# k, n = map(int, input().split())

# cleaned = set()

# curr_x, curr_y = 0, 0

# for _ in range(n):
#     dir, d = input().split()
#     d = int(d)
#     dx, dy = directions[dir]

#     for step in range(d):
#         for x in range(curr_x, curr_x + k):
#             for y in range(curr_y, curr_y + k):
#                 cleaned.add((x, y))

#         curr_x += dx
#         curr_y += dy

# for x in range(curr_x, curr_x + k):
#     for y in range(curr_y, curr_y + k):
#         cleaned.add((x, y))

# print(len(cleaned))

#####################Задача D. Разноцветные точки


# ##################Задача E. Метрострой
# def total_power(x):
#     power = 0
#     for z, a, b in engines:
#         if x <= z:
#             power += a * x
#         else:
#             power += a * z + b * (x - z)
#     return power

# n, p = map(int, input().split())
# engines = [tuple(map(int, input().split())) for _ in range(n)]

# left, right = 1, 10**12
# ans = -1
# while left <= right:
#     mid = left + (right - left) // 2
#     if total_power(mid) >= p:
#         ans = mid
#         right = mid - 1
#     else:
#         left = mid + 1

# print(ans)

######################Задача G. Камни
# from collections import deque

# n, q = map(int, input().split())
# a = list(map(int, input().split()))
# queries = [tuple(map(int, input().split())) for _ in range(q)]

# ans = [[0] * (n + 1) for _ in range(n + 1)]

# for start in range(1, n + 1):
#     painted = [False] * (n + 1)
#     painted[start] = True
#     order = deque([start])
#     ans[start][1] = 1

#     for step in range(2, n + 1):
#         neighbors = []
#         for stone in order:
#             if stone > 1 and not painted[stone - 1]:
#                 neighbors.append(stone - 1)
#             if stone < n and not painted[stone + 1]:
#                 neighbors.append(stone + 1)

#         next_stone = min(neighbors, key=lambda x: a[x - 1])
#         painted[next_stone] = True
#         order.append(next_stone)

#         ans[next_stone][step] += 1

# for p, k in queries:
#     print(ans[p][k])
##################Задача A. Разноцветный квадрат
# n = int(input())

# alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# square = []
# for i in range(n):
#     row = []
#     for j in range(n):
#         distance = min(abs(i - j), abs(i + j - (n - 1)))
#         row.append(alphabet[distance % 26])
#     square.append("".join(row))

# print("\n".join(square))
