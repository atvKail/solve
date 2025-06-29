import sys

sys.setrecursionlimit(30000)

operations = [
    lambda x: x - 1,
    lambda x: x - 2,
    lambda x: x // 3
]


def f(x: int, e6: bool, n13: bool) -> int:
    if x < 4:
        return 0
    if x == 4 and e6 and n13:
        return 1
    if x == 6:
        e6 = 1
    if x == n13:
        n13 &= 0
    return sum([f(op(x), e6, n13) for op in operations])


print(f(19, 0, 1))
