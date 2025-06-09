oprations = [
    lambda x: x - 2,
    lambda x: x - 5,
    lambda x: x // 3
]


def f(s: int, m: int) -> bool:
    if s <= 19 and m == 3:
        return 1
    elif s <= 19 and m >= 3:
        return 0
    elif s <= 19 and m < 3:
        return 0
    if m & 1 == 0:
        return any([f(op(s), m + 1) for op in oprations])
    else:
        return all([f(op(s), m + 1) for op in oprations])


for s in range(20, 10000):
    if f(s, 1):
        print(s)
        break
