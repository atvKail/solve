import sys
from bisect import bisect_left


a = []
with open(
    "USE\\ПолноценноеРешениеВариантов\\Открытый майский вариант 2025\\26_21910.txt", "r"
) as f:
    N = int(f.readline().strip())
    for line in f.readlines():
        a.append(int(line.strip()))
a.sort()
D = 9

dp = [1] * N
sufmax = [0] * (N + 1)
sufmax[N] = 0

for i in range(N - 1, -1, -1):
    j = bisect_left(a, a[i] + D, i + 1)
    if j < N:
        dp[i] = 1 + sufmax[j]
    sufmax[i] = max(dp[i], sufmax[i + 1])

k = sufmax[0]
bmin = max(a[i] for i in range(N) if dp[i] == k)
print(f"{k} {bmin}")
