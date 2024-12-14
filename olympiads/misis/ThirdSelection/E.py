MOD = 998244353

def mod_exp(base, exp, mod):
    res = 1
    while exp > 0:
        if exp % 2 == 1:
            res = (res * base) % mod
        base = (base * base) % mod
        exp //= 2
    return res

def sieve(maxv):
    mu = [1] * (maxv + 1)
    is_prime = [True] * (maxv + 1)
    for i in range(2, maxv + 1):
        if is_prime[i]:
            for j in range(i, maxv + 1, i):
                is_prime[j] = False
                mu[j] *= -1
            for j in range(i * i, maxv + 1, i * i):
                mu[j] = 0
    return mu

def count(n, m, mu):
    ttl = 0
    for d in range(1, m + 1):
        if mu[d] != 0:
            count = mod_exp(m // d, n, MOD)
            ttl = (ttl + mu[d] * count) % MOD
    return ttl


quers = []
max_m = 0
for _ in range(int(input())):
    n, m = map(int, input().split())
    quers.append((n, m))
    max_m = max(max_m, m)

mu = sieve(max_m)

for n, m in quers:
    print(count(n, m, mu))