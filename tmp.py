# import sys

# input = sys.stdin.readline


# def find(x, parent):
#     if parent[x] != x:
#         parent[x] = find(parent[x], parent)
#     return parent[x]


# def union(x, y, parent):
#     rx = find(x, parent)
#     ry = find(y, parent)
#     if rx != ry:
#         parent[ry] = rx


# n, m = map(int, input().split())
# parent = list(range(n + 1))

# for _ in range(m):
#     u, v = map(int, input().split())
#     union(u, v, parent)

# k, a = map(int, input().split())

# if find(k, parent) == find(a, parent):
#     print(0)
# else:
#     print(1)


# import math
# import sys

# input = sys.stdin.readline


# n = int(input().strip())


# def solve(n: int) -> int:
#     s = math.isqrt(2 * n)
#     if s * s == 2 * n and s % 2 == 0:
#         return n

#     s = math.isqrt(2 * n - 1)
#     if s * s == 2 * n - 1 and s % 2 == 1:
#         return (s * s - 1) // 2

#     s = math.isqrt(2 * n + 1)
#     if s * s == 2 * n + 1 and s % 2 == 1:
#         return (s * s + 1) // 2
#     return -1


# print(solve(n))


# import sys

# input = sys.stdin.readline
# mod = 10**9 + 7

# # n = int(input().strip())
# # steps = list(map(int, input().split()))

# # dp = [0] * (n + 1)
# # dp[0] = 1

# # for i in range(1, n + 1):
# #     if steps[i - 1] == 0:
# #         dp[i] = dp[i - 1]
# #         if i - 2 >= 0:
# #             dp[i] = (dp[i] + dp[i - 2]) % mod
# #         else:
# #             dp[i] %= mod
# #     else:
# #         dp[i] = 0

# # print(dp[n])

# n = int(input().strip())
# a = list(map(int, input().strip().split()))
# dp = [0] * (n + 1)
# dp[0] = 1
# dp[1] = 1 if a[0] != 1 else 0
# for i in range(1,n):
#     if a[i]==1:
#         continue
#     dp[i+1]=(dp[i]+dp[i-1]) % mod
# print(dp[n])


# import sys

# input = sys.stdin.readline

# v = int(input().strip())
# res = []
# r1 = 2 * v + 2
# res.append(r1)

# if (v + 2) % 3 == 0:
#     r2 = 2 * (v - 1) // 3
#     res.append(r2)

# res = sorted(set(res))
# print(" ".join(map(str, res)))


# import sys, math

# input = sys.stdin.readline


# t = int(input().strip())
# for _ in range(t):
#     n = int(input().strip())
#     ds = list(map(int, input().split()))
#     happy = 0
#     s = 0
#     for a in ds:
#         s += a
#         r = int(math.isqrt(s))
#         if r * r == s and r % 2 == 1:
#             happy += 1
#     print(happy)


import sys
import math

input = sys.stdin.readline


n = int(input().strip())
hps = list(map(int, input().split()))
m = int(input().strip())

if n > m:
    print(-1)
else:
    l, r = 1, max(hps)
    res = -1
    while l <= r:
        mid = (l + r) // 2
        total_hits = sum((h + mid - 1) // mid for h in hps)
        if total_hits <= m:
            res = mid
            r = mid - 1
        else:
            l = mid + 1
    print(res)
