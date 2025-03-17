import sys

input = sys.stdin.readline


MAXS = 60
MAXK = 60
INF = 10**20

dp = [[INF] * (MAXS + 1) for _ in range(MAXS + 1)]
dp[0][0] = 0

for k in range(1, MAXK + 1):
    kk = 1 << k
    ndp = [row[:] for row in dp]
    for a in range(MAXS + 1):
        for b in range(MAXS + 1):
            if dp[a][b] < INF:
                if a + k <= MAXS:
                    nv = dp[a][b] + kk
                    if nv < ndp[a + k][b]:
                        ndp[a + k][b] = nv
                if b + k <= MAXS:
                    nv = dp[a][b] + kk
                    if nv < ndp[a][b + k]:
                        ndp[a][b + k] = nv
    dp = ndp
# dp можно вывести и присвоить выведенное dp, чтобы всё подсчитанное записать просто, без на 1 секунду больше

cand = []
for a in range(MAXS + 1):
    for b in range(MAXS + 1):
        if dp[a][b] < INF:
            cand.append((dp[a][b], a, b))
cand.sort(key=lambda x: x[0])


t = int(input().strip())
results = [0] * t
for i in range(t):
    x, y = map(int, input().strip().split())
    for cost, shx, shy in cand:
        if (x >> shx) == (y >> shy):
            results[i] = cost
            break

print("\n".join(map(str, results)))
# Отправка python3.8 - превышено ограничение по времени, pypy3.10 полное решение. Лучше написать на C++
