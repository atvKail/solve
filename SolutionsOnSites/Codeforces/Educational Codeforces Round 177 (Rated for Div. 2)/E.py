import sys


def getZebras(limit=10**18):
    res = []
    n = 1
    while True:
        a = (4**n - 1) // 3
        if a > limit:
            break
        res.append(a)
        n += 1
    return res


def conv(x, coins_desc):
    digits = []
    for coin in coins_desc:
        if coin > x:
            d = 0
        else:
            d = x // coin
            if d > 4:
                d = 4
        digits.append(d)
        x -= d * coin
    return digits


def cntLeq(X, target, coins_desc):
    rep = conv(X, coins_desc)
    n = len(rep)

    dp = [[[0] * (target + 1) for _ in range(2)] for _ in range(n + 1)]

    dp[0][1][0] = 1
    for i in range(n):
        for tight in range(2):
            for s in range(target + 1):
                ways = dp[i][tight][s]
                if ways == 0:
                    continue

                max_digit = rep[i] if tight == 1 else 4
                for d in range(max_digit + 1):
                    ns = s + d
                    if ns > target:
                        continue
                    ntight = 1 if (tight == 1 and d == rep[i]) else 0
                    dp[i + 1][ntight][ns] += ways
    return dp[n][0][target] + dp[n][1][target]


results = []
t = int(input())

coins = getZebras(10**18)
coins_desc = coins[::-1]
n = len(coins_desc)

for _ in range(t):
    L, R, k = map(int, input().split())

    if k > 4 * n:
        results.append("0")
        continue

    cnt_R = cntLeq(R, k, coins_desc)
    cnt_Lm1 = cntLeq(L - 1, k, coins_desc) if L > 0 else 0
    results.append(str(cnt_R - cnt_Lm1))
sys.stdout.write("\n".join(results))

# Неверно 4764716061, а правильно 4246658701
