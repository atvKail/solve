operations = [
    lambda x: x + 1,
    lambda x: x + 4,
    lambda x: x * 3
]


def f(x: int, m: int) -> bool:
    if x >= 67 and m == 4:
        return 1
    elif x < 67 and m == 4:
        return 0
    elif x >= 67 and m >= 4:
        return 0
    elif x >= 67 and m < 4:
        return 0
    if m & 1 == 0:
        return all([f(op(x), m + 1) for op in operations])
    return any([f(op(x), m + 1) for op in operations])


cnt = 0
for s in range(1, 66):
    if f(s, 1):
        print(s)
        cnt += 1
    if cnt > 1:
        break
