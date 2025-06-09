import bisect


with open("USE\\Решения\\26\\21424\\26_21424.txt") as f:
    data = f.read().split()
n = int(data[0])
a = list(map(int, data[1:]))

a.sort()

next_idx = [n] * n
for i in range(n):
    j = bisect.bisect_left(a, a[i] + 9, lo=i + 1)
    next_idx[i] = j

dp = [0] * n
for i in range(n - 1, -1, -1):
    j = next_idx[i]
    if j < n:
        dp[i] = dp[j] + 1
    else:
        dp[i] = 1

k = max(dp)
bstart = 0
for i in range(n):
    if dp[i] == k and a[i] > bstart:
        bstart = a[i]
print(f"{k} {bstart}")
