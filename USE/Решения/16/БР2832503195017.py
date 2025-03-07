# import sys

# sys.setrecursionlimit(30000)
# sys.set_int_max_str_digits(100000)


# def f(n):
#     if n < 5:
#         return n

#     return 2 * n * f(n - 4)


# print((f(13766) - 9 * f(13762)) // f(13758))


def F_non_recursive(n):
    dp = {}
    for i in range(5):
        dp[i] = i
    for i in range(5, n + 1):
        dp[i] = 2 * i * dp[i - 4]
    return dp[n]


F_13766 = F_non_recursive(13766)
F_13762 = F_non_recursive(13762)
F_13758 = F_non_recursive(13758)

result = (F_13766 - 9 * F_13762) // F_13758

print(result)
