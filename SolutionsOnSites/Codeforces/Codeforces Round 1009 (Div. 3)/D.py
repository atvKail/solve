import math
import sys

input = sys.stdin.readline

results = []
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    x = list(map(int, input().split()))
    r = list(map(int, input().split()))

    max_y = {}
    for xi, ri in zip(x, r):
        ri_sq = ri * ri
        for dx in range(-ri, ri + 1):
            x_cur = xi + dx
            dx_sq = dx * dx
            y_sqr = ri_sq - dx_sq
            y_max = math.isqrt(y_sqr)
            if x_cur in max_y:
                if y_max > max_y[x_cur]:
                    max_y[x_cur] = y_max
            else:
                max_y[x_cur] = y_max

    ttl = 0
    for y in max_y.values():
        ttl += 2 * y + 1
    results.append(str(ttl))
print("\n".join(results))
