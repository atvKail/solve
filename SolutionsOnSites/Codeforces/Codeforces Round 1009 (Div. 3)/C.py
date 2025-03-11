import sys

input = sys.stdin.readline

results = []
t = int(input())
for _ in range(t):
    x = int(input())
    if (x & (x - 1)) == 0:
        results.append("-1")
        continue
    if (x & (x + 1)) == 0:
        results.append("-1")
        continue

    mask = 1
    k = 0
    while x & mask:
        mask <<= 1
        k += 1

    m = x & -x
    y = (1 << k) | m
    results.append(str(y))
print("\n".join(results))
