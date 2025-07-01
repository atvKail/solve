operations = [
    lambda x: x - 1,
    lambda x: x - 4,
    lambda x: x // 3
]


def f(x: int, ni8: bool = 1, i14: bool = 0) -> int:
    if x == 2 and ni8 and i14:
        return 1
    if x < 2:
        return 0
    if x == 8:
        ni8 &= 0
    if x == 14:
        i14 = 1
    return sum(f(x=op(x), ni8=ni8, i14=i14) for op in operations)


print(f(19))