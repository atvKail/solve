from sys import setrecursionlimit


setrecursionlimit(60000)

operations = [
    lambda x: x + 1,
    lambda x: x + 2,
    lambda x: x * 2
]


def f(x: int, x7: bool, xn11: bool) -> int:
    if x > 17:
        return 0
    if x == 17:
        if x7 and xn11:
            return 1
        return 0
    if x == 7:
        x7 = x7 or 1
    if x == 11:
        xn11 = xn11 & 0

    ss = 0
    for op in operations:
        ss += f(op(x), x7, xn11)
    return ss
    

print(f(1, 0, 1))
