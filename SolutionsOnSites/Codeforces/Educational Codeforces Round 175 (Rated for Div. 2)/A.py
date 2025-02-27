import sys

input = sys.stdin.readline

t = int(input())
results = []
for i in range(1, t + 1):
    n = int(input())
    cnt = 0
    for r in range(3):
        if n >= r:
            cnt += (n - r) // 15 + 1
    results.append(str(cnt))
print("\n".join(results))
