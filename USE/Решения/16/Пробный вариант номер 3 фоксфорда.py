import sys

sys.setrecursionlimit(30000)


def F(n):
    if n == 1:
        return 5
    return 2 * n + F(n - 1)


# def F(n):
#     return n * (n + 1) + 5        # По факту сумма арифметической прогрессии 2 * (1 + 2 + 3 + ... + n) + 5


result = F(2048) - F(1024)

print(result)
