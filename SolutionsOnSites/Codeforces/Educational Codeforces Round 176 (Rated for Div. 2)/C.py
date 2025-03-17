import sys
import bisect

input = sys.stdin.readline


results = []
t = int(input().strip())
for _ in range(t):
    n, m = map(int, input().strip().split())
    a = list(map(int, input().strip().split()))

    a.sort()

    ttl = 0
    for L in range(1, n):
        R = n - L
        cl = m - bisect.bisect_left(a, L)
        cr = m - bisect.bisect_left(a, R)
        cb = m - bisect.bisect_left(a, max(L, R))
        wfs = cl * cr - cb
        ttl += wfs
    results.append(str(ttl))

print("\n".join(results))
