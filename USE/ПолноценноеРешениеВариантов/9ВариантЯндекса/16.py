from sys import setrecursionlimit

setrecursionlimit(6000)


def f(n: int) -> int:
    if n < 3:
        return 1
    if n & 1 == 0:
        return f(n - 1) * (n - 1)
    return f(n - 2) * (2 * n - 2)


print((f(10048) - f(10045)) / f(10043))