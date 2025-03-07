from sys import setrecursionlimit


setrecursionlimit(6000)


def f(n: int) -> int:
    if n == 1:
        return 4
    return 3 * n + f(n - 1)


print(f(2049) - f(2023))
