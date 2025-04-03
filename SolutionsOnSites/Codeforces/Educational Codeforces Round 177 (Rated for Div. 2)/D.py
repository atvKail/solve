import sys

input = sys.stdin.readline
MOD = 998244353

max_n = 5 * 10**5
fact = [1] * (max_n + 1)
invfact = [1] * (max_n + 1)
for i in range(2, max_n + 1):
    fact[i] = fact[i - 1] * i % MOD
invfact[max_n] = pow(fact[max_n], MOD - 2, MOD)
for i in range(max_n, 0, -1):
    invfact[i - 1] = invfact[i] * i % MOD


t = int(input())
index = 1
results = []
for _ in range(t):
    c = list(map(int, input().split()))
    N = sum(c)

    if N == 0:
        results.append("0")
        continue

    O = (N + 1) // 2
    E = N // 2

    f = True
    for cnt in c:
        if cnt > O:
            f = False
            break
    if not f:
        results.append("0")
        continue

    fsum = 0
    free = []
    for cnt in c:
        if cnt == 0:
            continue
        if cnt > E:
            fsum += cnt
        else:
            free.append(cnt)

    trgt = O - fsum
    if trgt < 0:
        results.append("0")
        continue

    dp = [0] * (trgt + 1)
    dp[0] = 1
    for w in free:
        for j in range(trgt, w - 1, -1):
            dp[j] = (dp[j] + dp[j - w]) % MOD
    f = dp[trgt]

    dm = 1
    for cnt in c:
        if cnt:
            dm = dm * fact[cnt] % MOD
    sposob_arrage = fact[O] * fact[E] % MOD * pow(dm, MOD - 2, MOD) % MOD

    res = f * sposob_arrage % MOD
    results.append(str(res))
sys.stdout.write("\n".join(results))

# solved, решено на претестах, решение было успешно взломано, tl
