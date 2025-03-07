"""
cat "USE\\ПолноценноеРешениеВариантов\\ВариантЕГЭФокфорд\\data\\26.txt" | python "USE\\ПолноценноеРешениеВариантов\\ВариантЕГЭФокфорд\\26.py"
"""

import sys
import bisect


data = sys.stdin.read().split()
if not data:
    sys.exit()

N = int(data[0])
heights = [int(x) for x in data[1 : 1 + N]]

heights.sort()

n = len(heights)

dp = [0] * n

size = 2**13
seg = [0] * (2 * size)


def seg_update(i, value):
    i += size
    seg[i] = value
    while i > 1:
        i //= 2
        seg[i] = max(seg[2 * i], seg[2 * i + 1])


def seg_query(l, r):
    l += size
    r += size
    res = 0
    while l <= r:
        if l % 2 == 1:
            res = max(res, seg[l])
            l += 1
        if r % 2 == 0:
            res = max(res, seg[r])
            r -= 1
        l //= 2
        r //= 2
    return res


for i in range(n - 1, -1, -1):
    j = bisect.bisect_left(heights, heights[i] + 5, i + 1, n)
    best = seg_query(j, n - 1) if j < n else 0
    dp[i] = 1 + best
    seg_update(i, dp[i])


m = max(dp)


max_first = 0
for i in range(n):
    if dp[i] == m:
        max_first = max(max_first, heights[i])


print(m, max_first)
