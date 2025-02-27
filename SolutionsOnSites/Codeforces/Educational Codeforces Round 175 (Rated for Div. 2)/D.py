import sys


input = sys.stdin.readline
MOD = 998244353

results = []
t = int(input())
for _ in range(t):
    n = int(input())
    ps = list(map(int, input().split()))

    parent = [0] * (n + 1)
    parent[1] = 0
    for i in range(2, n + 1):
        parent[i] = ps[i - 2]

    dpth = [0] * (n + 1)
    dpth[1] = 0
    for i in range(2, n + 1):
        dpth[i] = dpth[parent[i]] + 1
    mdpth = max(dpth)

    grps = [[] for _ in range(mdpth + 1)]
    for i in range(1, n + 1):
        grps[dpth[i]].append(i)

    dp = [0] * (n + 1)
    S = [0] * (mdpth + 1)
    dp[1] = 1
    S[0] = 1

    if mdpth >= 1:
        for v in grps[1]:
            dp[v] = 1
        S[1] = len(grps[1]) % MOD

    for d in range(2, mdpth + 1):
        ttl = 0
        for v in grps[d]:
            ways = (S[d - 1] - dp[parent[v]]) % MOD
            dp[v] = ways
            ttl = (ttl + ways) % MOD
        S[d] = ttl
    results.append(str(sum(dp[1:]) % MOD))
print("\n".join(results))
