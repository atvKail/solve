import sys

input = sys.stdin.readline


t = int(input().strip())
res = []
for _ in range(t):
    n, k = map(int, input().strip().split())
    if n % 2 == 0:
        moves = (n + (k - 1) - 1) // (k - 1)
    else:
        moves = 1 + ((n - k) + (k - 1) - 1) // (k - 1)
    res.append(str(moves))
print("\n".join(res))
