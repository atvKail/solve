import sys

input = sys.stdin.readline

t = int(input().strip())
results = []
for _ in range(t):
    l, r, d, u = map(int, input().split())
    results.append("Yes" if l == r == d == u else "No")
print("\n".join(results))

