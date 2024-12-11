# import sys


# sys.set_int_max_str_digits(30000)

# n = int(input())
# if n % 2 != 0:
#     print(0)
# elif n == 2:
#     print(2)
# else:
#     f = [0] * (n + 1)
#     f[2] = 2

#     for i in range(4, n + 1, 2):
#         f[i] = 2 * f[i - 2]

#     print(f[n])
# task D 100


# def dist(x1, y1, x2, y2, n, m):
#     dx = min(abs(x1 - x2), n - abs(x1 - x2))
#     dy = min(abs(y1 - y2), m - abs(y1 - y2))
#     return dx + dy


# n, m, b = map(int, input().split())
# seeds = [tuple(map(int, input().split())) for _ in range(b)]

# labels = [chr(ord("a") + i) for i in range(b)]

# influence_grid = [[0 for _ in range(n)] for _ in range(m)]
# map_grid = [["#" for _ in range(n)] for _ in range(m)]

# for y in range(m):
#     for x in range(n):
#         influences = []
#         for idx in range(b):
#             bx, by, bi = seeds[idx]
#             d = dist(x, y, bx, by, n, m)
#             influence = max(0, bi - d)
#             influences.append((influence, idx))
#         mi = max(influences, key=lambda t: t[0])[0]
#         if mi == 0:
#             map_grid[y][x] = "#"
#             influence_grid[y][x] = 0
#         else:
#             count = sum(1 for inf, _ in influences if inf == mi)
#             if count > 1:
#                 map_grid[y][x] = "#"
#                 influence_grid[y][x] = 0
#             else:
#                 for inf, idx in influences:
#                     if inf == mi:
#                         map_grid[y][x] = labels[idx]
#                         influence_grid[y][x] = inf
#                         break

# for row in map_grid:
#     print("".join(row))

# for row in influence_grid:
#     print(" ".join(map(str, row)))     # C 85
