import sys


input = sys.stdin.readline

results = []
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    N = n - 1
    row = []
    for j in range(n):
        row.append(str(k) if (j & N) == j else "0")
    results.append(" ".join(row))
print("\n".join(results))
