operations = [
    lambda x: x + 3,
    lambda x: x + 5,
    lambda x: x * x
]


def f(x: int, x16: bool, nx27: bool) -> int:
    if x > 51:
        return 0
    if x == 51 and x16 and nx27:
        return 1
    if x == 16:
        x16 = x16 or 1
    if x == 27:
        nx27 = nx27 & 0
    return sum([f(op(x), x16, nx27) for op in operations])


print(f(3, 0, 1))