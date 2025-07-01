import sys

sys.setrecursionlimit(30000)


def f(x: int) -> int:
    return 2 * (g(x - 3) + 8)


def g(x: int) -> int:
    if x < 10:
        return 2 * x
    return g(x - 2) + 1


print(f(15548))
