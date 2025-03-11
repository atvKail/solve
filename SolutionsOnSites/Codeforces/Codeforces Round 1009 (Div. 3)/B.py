import sys

input = sys.stdin.readline

t = int(input().strip())
results = []
for _ in range(t):
    n = int(input().strip())
    a = list(map(int, input().split()))
    results.append(str(sum(a) - (n - 1)))
print("\n".join(results))
