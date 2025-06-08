operations = [
    lambda x: x + 2,
    lambda x: x + 4,
    lambda x: x * 2
]


def f(x: int, n22: bool, n24: bool) -> int:
    if x == 38 and n22 != n24 and (n22 or n24):
        return 1
    if x > 38:
        return 0
    if x == 22:
        n22 = n22 or 1
    if x == 24:
        n24 = n24 or 1
    return sum(f(op(x), n22, n24) for op in operations)


print(f(12, 0, 0))
