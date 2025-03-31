def f(n: int) -> int:
    if n <= 2:
        return n
    if n & 1 == 0:
        return (2 * n + f(n - 3)) // 6
    return (3 * n + f(n - 1) + f(n - 2)) // 5


print(f(42))
