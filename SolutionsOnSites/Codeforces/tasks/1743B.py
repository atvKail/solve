import sys


input = sys.stdin.readline

t = int(input().strip())
results = []
for _ in range(t):
    n = int(input().strip())
    perm = [1] + list(range(n, 1, -1))
    results.append(" ".join(map(str, perm)))
print("\n".join(results))
