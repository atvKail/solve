# def solve(N, K, A, M, T):
#     if T < M:
#         return "No"

#     L = T // M
#     ttlp = N * K

#     if (T - M) // A >= N:
#         return "Yes"

#     l, r = 0, min(L, ttlp)
#     while l <= r:
#         mid = (l + r) // 2
#         badcnt = 0
#         for i in range(1, N + 1):
#             if T - i * A <= 0:
#                 bpos = mid
#             else:
#                 fbk = (T - i * A) // M + 1
#                 bpos = max(0, mid - fbk + 1)
#             badcnt += min(K, bpos)
#             if badcnt > mid:
#                 break

#         if badcnt >= mid:
#             l = mid + 1
#         else:
#             r = mid - 1

#     mid = r
#     if mid < min(L, ttlp):
#         return "Yes"
#     else:
#         return "No"


# N = int(input())
# K = int(input())
# A = int(input())
# M = int(input())
# T = int(input())

# print(solve(N, K, A, M, T))

######################################### 1 48
# import itertools

# def is_isomorphic(mapping, g1, g2):
#     return all(mapping[u] in g2.get(mapping[v], []) for u in g1 for v in g1[u])

# g1 = {
#     1: [5, 8],
#     2: [3, 5],
#     3: [2, 5, 6],
#     4: [5, 7],
#     5: [1, 2, 3, 4, 6, 7, 8],
#     6: [3, 5],
#     7: [4, 5, 8],
#     8: [1, 5, 7]
# }

# g2 = {
#     'A': ['B', 'C', 'D', 'E', 'F', 'G', 'H'],
#     'B': ['C', 'A'],
#     'C': ['B', 'D', 'A'],
#     'D': ['A', 'C'],
#     'E': ['F', 'A'],
#     'F': ['E', 'G', 'A'],
#     'G': ['F', 'H', 'A'],
#     'H': ['G', 'A']
# }

# for perm in itertools.permutations(g2.keys()):
#     m = dict(zip(g1.keys(), perm))
#     if is_isomorphic(m, g1, g2):
#         print(m)
#         break
# else:
#     print(-1)

######################################### 2 56
# from itertools import permutations

# matrix = "2678 134 26 258 4 137 168 147".split()
# graph = "АБ БГ БД АГ АВ ВЕ ЕК КЛ ДК ГД ЕГ".split()

# print(*range(1, 9))

# for perm in permutations("АБВГДЕКЛ"):
#     if all(str(perm.index(y) + 1) in matrix[perm.index(x)] for x, y in graph):
#         print(*perm)

########################################## 4 ywzx
# print("x y z w")
# for x in range(0, 2):
#     for y in range(0, 2):
#         for z in range(0, 2):
#             for w in range(0, 2):
#                 if (not(x) or y or z) == (not(y) and z and w):
#                     print(x, y, z, w)
########################################## 5 162
# def tb3(n):
#     if n == 0:
#         return "0"
#     d = ""
#     while n > 0:
#         d = str(n % 3) + d
#         n //= 3
#     return d


# def fb3(s):
#     return int(s, 3)


# max_r = -1
# best_n = -1

# for n in range(1, 1000):
#     nb3 = tb3(n)
#     if n % 3 == 0:
#         tail = nb3[-2:] if len(nb3) >= 2 else nb3.zfill(2)
#         r_base3 = nb3 + tail
#     else:
#         rem = n % 3
#         extra = tb3(rem * 5)
#         r_base3 = nb3 + extra
#     r = fb3(r_base3)
#     if r <= 173 and r > max_r:
#         max_r = r
#         best_n = n

# print(max_r)
# print(best_n)
###################################### 6
# def get_triplets(s):
#     return [int(s[i : i + 3]) for i in range(len(s) - 2)]


# for n in range(100, 10**6):
#     s = str(n).zfill(3)
#     trpls = get_triplets(s)
#     if not trpls:
#         continue
#     max_t = max(trpls)
#     min_t = min(trpls)
#     if max_t - min_t == 415:
#         print(n)
#         break
