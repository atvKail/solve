import sys

input = sys.stdin.readline


t = int(input())
res = []
for i in range(1, t + 1):
    n = int(input())
    res.append(str(2 * n))
sys.stdout.write("\n".join(res))

# Solved
