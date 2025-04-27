import sys

input = sys.stdin.readline

INF = 10**30


n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

pok = sorted(zip(a, b), key=lambda x: x[0])
s = [p[0] for p in pok]
c = [p[1] for p in pok]

if n == 1:
    print(c[0])
else:
    a1 = [s[j] - j for j in range(n)]
    a2 = [s[j] - (j - 1) for j in range(n)]

    pl = [0] * n
    pl[0] = a1[0]
    for j in range(1, n):
        pl[j] = max(pl[j - 1], a1[j])

    S = [0] * n
    S[n - 1] = a2[n - 1]
    for j in range(n - 2, -1, -1):
        S[j] = max(S[j + 1], a2[j])

    ans = INF
    for p in range(n):
        lmax = pl[p - 1] if p > 0 else -INF

        rmax = S[p + 1] if p < n - 1 else -INF
        need = max(lmax, rmax)

        if s[p] > need:
            ans = min(ans, c[p])

    print(ans if ans < INF else -1)
