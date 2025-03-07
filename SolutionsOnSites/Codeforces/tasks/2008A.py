import sys


input = sys.stdin.readline

t = int(input().strip())
results = []
for _ in range(t):
    a, b = map(int, input().strip().split())
    if a % 2 != 0:
        results.append("NO")
    else:
        if a == 0:
            results.append("YES" if b % 2 == 0 else "NO")
        else:
            results.append("YES")
print("\n".join(results))
