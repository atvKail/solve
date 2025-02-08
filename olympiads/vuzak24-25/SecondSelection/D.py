MOD = 10**9 + 7

n = int(input())
a = list(map(int, input().split()))

m = n // 2
maxN = m

f = [1] * (maxN + 1)
g = [1] * (maxN + 1)

for i in range(1, maxN + 1):
    f[i] = f[i - 1] * i % MOD
g[maxN] = pow(f[maxN], MOD - 2, MOD)
for i in range(maxN, 0, -1):
    g[i - 1] = g[i] * i % MOD

r0 = 0
r1 = 0
for r in range(m):
    b = f[m - 1] * g[r] % MOD * g[m - 1 - r] % MOD
    r0 = (r0 + b * a[2 * r]) % MOD
    r1 = (r1 + b * a[2 * r + 1]) % MOD

print(r0, r1)
