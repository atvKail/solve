def f(n: int) -> int:
    ns = str(n)
    ns = ns.replace("3", "4")
    ns = ns.replace("7", "8")
    dp = [1] * (len(ns) + 1)
    for i in range(1, len(ns) + 1):
        dp[i] = dp[i - 1] * int(ns[i - 1])
    R = dp[len(ns)]
    return R


for n in range(1000, 9999):
    if n == 3333:
        print(f(n))
    if f(n) == 256:
        print(n)
        break
