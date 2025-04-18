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

# def f(code: str) -> int:
#     sz = 26
#     ttl = 0

#     for l in range(1, len(code)):
#         ttl += sz ** l

#     for i, ch in enumerate(code):
#         power = len(code) - i - 1
#         offset = ord(ch) - ord('A')
#         ttl += offset * (sz ** power)

#     return ttl + 1

# print(f("ASFY"))


# def get_code_by_number(n):
#     from string import ascii_uppercase

#     n -= 1
#     l = 1
#     ttl = 0

#     while True:
#         cnt = 26 ** l
#         if ttl + cnt > n:
#             break
#         ttl += cnt
#         l += 1

#     index = n - ttl
#     word = ""
#     for _ in range(l):
#         word = ascii_uppercase[index % 26] + word
#         index //= 26

#     return word


# print(get_code_by_number(3647))


# import string

# alph = "0123456789" + string.ascii_lowercase


# def dto15(n: int) -> list:
#     ns = []
#     while n > 0:
#         ns.append(n % 15)
#         n //= 15
#     return ns[::-1]


# ttl_cnt = 0
# f = True
# for n in range(10 ** 6):
#     ns = dto15(n)
#     if len(ns) > 5:
#         break
#     if len(ns) > 4:
#         if f:
#             print(n, 4)
#             f = False
#         if ns.count(8) == 1:
#             cnt = 0
#             for ln in ns:
#                 if ln > 9:
#                     cnt += 1
#             if cnt >= 2:
#                 ttl_cnt += 1
# print(ttl_cnt)


# import string

# alph = "КОСФ"


# def fr(n: int) -> str:
#     n -= 1
#     l = 1
#     ttl = 0

#     while True:
#         cnt = 4**l
#         if ttl + cnt > n:
#             break
#         ttl += cnt
#         l += 1

#     index = n - ttl
#     word = ""
#     for _ in range(l):
#         word = alph[index % 4] + word
#         index //= 4
#     return word


# for i in range(10**6):
#     ns = fr(i)
#     print(ns)
#     if len(ns) > 4:
#         break
#     if len(ns) > 3:
#         if ns == "ФОКС":
#             print(i)
#             break


# from itertools import product

# alph = "ФОКС"


# cnt = 0
# for p in product("ФОКС", repeat=5):
#     n = p.count('Ф')
#     print(p, n)
#     if 0 < n < 3:
#         cnt += 1
# print(cnt)


# from itertools import permutations

# matrix = "247 157 47 137 27 7 123456".split()
# graph = "ЕА ЕД АБ АЕ АД БА БВ БД ВГ ВД ВБ ДА ДБ ДЕ ДВ ДГ МД".split()

# print(*range(1, 8))

# for perm in permutations("АБВГДЕМ"):
#     if all(str(perm.index(y) + 1) in matrix[perm.index(x)] for x, y in graph):
#         print(*perm) # 37


# from itertools import permutations

# matrix = "37 46 145678 23 3 23 13 3".split()
# graph = "БВ БА ВГ ВБ АГ АБ ГД ГВ ГА ГЖ ГЕ ГД ГК ЖГ ЖЕ КГ ДГ ЕГ ЕЖ".split()

# print(*range(1, 8))

# for perm in permutations("АБВГДЖЕК"):
#     if all(str(perm.index(y) + 1) in matrix[perm.index(x)] for x, y in graph):
#         print(*perm)
