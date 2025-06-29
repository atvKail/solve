operations = [
    lambda x: x - 3,
    lambda x: x - 7,
    lambda x: x // 3
]


def f(x: int, m: int) -> bool:
    if x <= 11:
        return not m & 1
    if m == 0:
        return 0
    vars = [f(op(x), m - 1) for op in operations]
    return all(vars) if not m & 1 else any(vars)


print(19, [x for x in range(12, 150) if f(x, 2)])
print(20, [x for x in range(12, 150) if not f(x, 1) and f(x, 3)])
print(21, [x for x in range(12, 150) if not f(x, 2) and f(x, 4)])
