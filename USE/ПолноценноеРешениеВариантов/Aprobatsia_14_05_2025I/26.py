from bisect import bisect_left


with open("USE\\ПолноценноеРешениеВариантов\\Aprobatsia_14_05_2025I\\26.txt", "r") as f:
    N = int(f.readline().strip())
    a = [int(f.readline().strip()) for _ in range(N)]

dp = []
for x in a:
    pos = bisect_left(dp, x)
    if pos == len(dp):
        dp.append(x)
    else:
        dp[pos] = x
print(len(dp))
