# import sys

# sys.setrecursionlimit(int(1e7))
# input = sys.stdin.readline


# n = int(input())
# adj = [[] for _ in range(n + 1)]
# for _ in range(n - 1):
#     u, v = map(int, input().split())
#     adj[u].append(v)
#     adj[v].append(u)

# parent = [0] * (n + 1)
# depth = [0] * (n + 1)
# order = [1]
# parent[1] = 1
# depth[1] = 0
# for u in order:
#     for w in adj[u]:
#         if w == parent[u]:
#             continue
#         parent[w] = u
#         depth[w] = depth[u] + 1
#         order.append(w)

# sz = [0] * (n + 1)
# for u in reversed(order):
#     sz[u] = 1
#     for w in adj[u]:
#         if w == parent[u]:
#             continue
#         sz[u] += sz[w]

# s0 = sum(depth[1:])

# f1 = [0] * (n + 1)
# f2 = [0] * (n + 1)
# for u in range(1, n + 1):
#     f1[u] = sz[u] * depth[u]
#     f2[u] = sz[u] * depth[parent[u]]

# log = (n + 1).bit_length()
# up = [[0] * (n + 1) for _ in range(log)]
# g1 = [[0] * (n + 1) for _ in range(log)]
# g2 = [[0] * (n + 1) for _ in range(log)]

# for u in range(1, n + 1):
#     up[0][u] = parent[u]
#     g1[0][u] = f1[u]
#     g2[0][u] = f2[u]

# for k in range(1, log):
#     pu = up[k - 1]
#     upu = up[k]
#     g1p = g1[k - 1]
#     g2p = g2[k - 1]
#     g1c = g1[k]
#     g2c = g2[k]
#     for u in range(1, n + 1):
#         mid = pu[u]
#         upu[u] = pu[mid]
#         g1c[u] = g1p[u] + g1p[mid]
#         g2c[u] = g2p[u] + g2p[mid]

# q = int(input())
# out = []
# for _ in range(q):
#     v, u = map(int, input().split())

#     rem = depth[u] - depth[v]
#     s1 = 0
#     s2 = 0
#     x = u
#     for k in range(log - 1, -1, -1):
#         if rem >= (1 << k):
#             s1 += g1[k][x]
#             s2 += g2[k][x]
#             x = up[k][x]
#             rem -= 1 << k

#     s1 += f1[v]
#     s2 += f2[v]

#     dlt = sz[v] * (depth[u] + depth[v]) - 2 * (s1 - s2 + f2[v])
#     out.append(str(s0 + dlt))
# print("\n".join(out))


import sys

sys.setrecursionlimit(10**7)
input = sys.stdin.readline


n = int(input())
adj = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

parent = [0] * (n + 1)
depth = [0] * (n + 1)
order = [1]
parent[1] = 1
depth[1] = 0
for u in order:
    for w in adj[u]:
        if w == parent[u]:
            continue
        parent[w] = u
        depth[w] = depth[u] + 1
        order.append(w)

sz = [0] * (n + 1)
for u in reversed(order):
    sz[u] = 1
    for w in adj[u]:
        if w == parent[u]:
            continue
        sz[u] += sz[w]

s0 = sum(depth[1:])

sum1 = [0] * (n + 1)
sum2 = [0] * (n + 1)

for u in order:
    f1 = sz[u] * depth[u]
    f2 = sz[u] * depth[parent[u]]
    if u == 1:
        sum1[u] = f1
        sum2[u] = f2
    else:
        p = parent[u]
        sum1[u] = sum1[p] + f1
        sum2[u] = sum2[p] + f2

q = int(input())
out = []
for _ in range(q):
    v, u = map(int, input().split())
    p = parent[v]

    s1 = sum1[u] - sum1[p]
    s2 = sum2[u] - sum2[p]
    f2v = sz[v] * depth[p]

    dlt = sz[v] * (depth[u] + depth[v]) - 2 * (s1 - s2 + f2v)
    out.append(str(s0 + dlt))
print("\n".join(out))
