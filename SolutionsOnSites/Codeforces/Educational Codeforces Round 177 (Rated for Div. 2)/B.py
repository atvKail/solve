import sys, bisect

input = sys.stdin.readline


results = []
t = int(int(input()))
for _ in range(t):
    n, k, x = map(int, input().split())
    a = list(map(int, input().split()))

    total = sum(a)
    if k * total < x:
        results.append("0")
        continue

    prefix = [0] * n
    s = 0

    prefix[0] = 0
    for j in range(1, n):
        s += a[j - 1]
        prefix[j] = s

    ans = 0
    for m in range(k):
        R = (k - m) * total - x
        cnt = bisect.bisect_right(prefix, R, 0, n)
        ans += cnt
    results.append(str(ans))
sys.stdout.write("\n".join(results))

# Solved
