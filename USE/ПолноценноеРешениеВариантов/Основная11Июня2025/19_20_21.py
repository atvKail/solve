operations = [
    lambda x: x - 3,
    lambda x: x - 8,
    lambda x: x // 3
]


def f(x: int, m: int) ->  bool:
    if x <= 16:
        return not m & 1
    if m == 0:
        return 0
    vars = [f(op(x), m - 1) for op in operations]
    return all(vars) if not m & 1 else any(vars)


print(19, [i for i in range(17, 150) if not f(i, 1) and f(i, 2)]) # Ответ 51
print(20, [i for i in range(17, 150) if not f(i, 1) and not f(i, 2) and f(i, 3)]) # Ответ 54 55
print(21, [i for i in range(17, 150) if not f(i, 2) and f(i, 4)]) # Ответ 57
