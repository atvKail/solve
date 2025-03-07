import sys


input = sys.stdin.readline

results = []
t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    a = []
    for i in range(n):
        row = list(map(int, input().strip().split()))
        a.append(row)

    mvs = 0
    for d in range(-n + 1, n):
        mxneeded = 0
        start = max(0, d)
        end = min(n - 1, n - 1 + d)
        for i in range(start, end + 1):
            j = i - d
            deficit = 0
            if a[i][j] < 0:
                deficit = -a[i][j]
            if deficit > mxneeded:
                mxneeded = deficit
        mvs += mxneeded
    results.append(str(mvs))
print("\n".join(results))
