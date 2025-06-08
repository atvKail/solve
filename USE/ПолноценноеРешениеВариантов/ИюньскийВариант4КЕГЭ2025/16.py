import sys

sys.setrecursionlimit(30000)


def f(n: int) -> int:
    if n < 180:
        return 24
    return f(n - 12) + 6


print(sum(map(int, list(str(f(80000))))))
