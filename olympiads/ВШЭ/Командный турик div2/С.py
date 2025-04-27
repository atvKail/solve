def f(segs, k):
    n = len(segs)
    if n <= 1:
        return n

    segs.sort(key=lambda x: x[0])

    gaps = []
    for i in range(1, n):
        prev_r = segs[i - 1][1]
        curr_l = segs[i][0]
        gaps.append(curr_l - prev_r)

    gaps.sort()

    used = 0
    mrgs = 0
    for g in gaps:
        if used + g > k:
            break
        used += g
        mrgs += 1

    return n - mrgs


import sys

input = sys.stdin.readline


n, k = map(int, input().split())
segs = []
for _ in range(n):
    l, r = map(int, input().split())
    segs.append((l, r))

print(f(segs, k))
