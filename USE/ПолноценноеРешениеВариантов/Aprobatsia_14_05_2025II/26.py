from bisect import bisect_left


boxes = []
with open("USE\\ПолноценноеРешениеВариантов\\Aprobatsia_14_05_2025II\\26.txt") as f:
    n = int(f.readline().strip())
    while (x := f.readline()) != "":
        boxes.append(int(x.strip()))

boxes.sort()

dp = [0] * n
for i in range(n - 1, -1, -1):
    target = boxes[i] + 8
    j = bisect_left(boxes, target, lo=i + 1)
    if j < n:
        dp[i] = 1 + dp[j]
    else:
        dp[i] = 1

mlen = max(dp)

bsmallest = 0
for i in range(n):
    if dp[i] == mlen and boxes[i] > bsmallest:
        bsmallest = boxes[i]
print(mlen, bsmallest)
