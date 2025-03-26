import sys

input = sys.stdin.readline


t = int(input().strip())
for _ in range(t):
    n = int(input().strip())

    if n % 2 == 0:
        print(-1)
        continue

    p = []
    for i in range(1, n + 1):
        val = (2 * i) % n
        if val == 0:
            val = n
        p.append(val)
    print(" ".join(map(str, p)))
