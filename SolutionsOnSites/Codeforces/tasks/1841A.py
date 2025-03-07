import sys


input = sys.stdin.readline

gamers = ["Alice", "Bob"]

results = []
t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    results.append(gamers[1] if n in (2, 3, 4) else gamers[0])
print("\n".join(results))
