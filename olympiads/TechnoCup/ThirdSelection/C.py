# MOD = 10**9 + 7


# def fast_exp(base, exp, mod):
#     res = 1
#     while exp > 0:
#         if exp % 2 == 1:
#             res = (res * base) % mod
#         base = (base * base) % mod
#         exp //= 2
#     return res


# def sum_of_powers(start, cnt, mod):
#     if cnt == 0:
#         return 0
#     return (
#         fast_exp(2, start, mod)
#         * (fast_exp(2, cnt, mod) - 1)
#         % mod
#         * fast_exp(1, mod - 2, mod)
#     ) % mod


# n, t, k = map(int, input().split())
# if t == 0:
#     st = (k - 1) * n
#     print(sum_of_powers(st, n, MOD))
# elif t == 1:
#     st = k - 1
#     step = n
#     ttl = (
#         fast_exp(2, st, MOD)
#         * (fast_exp(2, step * n, MOD) - 1)
#         % MOD
#         * fast_exp(fast_exp(2, step, MOD) - 1, MOD - 2, MOD)
#     ) % MOD
#     print(ttl)
# elif t == 2:
#     if k == 1:
#         ttl = 0
#         for i in range(n):
#             ttl = (ttl + fast_exp(2, i * (n + 1), MOD)) % MOD
#         print(ttl)
#     elif k == 2:
#         ttl = 0
#         for i in range(n):
#             ttl = (ttl + fast_exp(2, i * (n - 1) + (n - 1), MOD)) % MOD
#         print(ttl)


MOD = 10**9 + 7


def fast_exp(base, exp, mod):
    res = 1
    while exp > 0:
        if exp % 2 == 1:
            res = (res * base) % mod
        base = (base * base) % mod
        exp //= 2
    return res


def sum_of_powers(start, step, cnt, mod):
    if cnt == 0:
        return 0
    if step == 1:
        # сумма первых cnt степеней
        return (fast_exp(2, start, mod) * (fast_exp(2, cnt, mod) - 1) % mod) % mod
    # геом прогрессия
    factor = fast_exp(2, step, mod)
    return (
        fast_exp(2, start, mod)
        * (fast_exp(factor, cnt, mod) - 1)
        % mod
        * fast_exp(factor - 1, mod - 2, mod)
    ) % mod


def sum_diagonal_1(n, mod):
    return sum_of_powers(0, n + 1, n, mod)


def sum_diagonal_2(n, mod):
    return sum_of_powers(n - 1, n - 1, n, mod)


n, t, k = map(int, input().split())

if t == 0:
    st = (k - 1) * n
    print(sum_of_powers(st, 1, n, MOD))
elif t == 1:
    st = k - 1
    print(sum_of_powers(st, n, n, MOD))
elif t == 2:
    if k == 1:
        print(sum_diagonal_1(n, MOD))
    elif k == 2:
        print(sum_diagonal_2(n, MOD))
