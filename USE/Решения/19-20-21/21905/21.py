operations = [
    lambda x: x + 1,
    lambda x: x + 4,
    lambda x: x * 3
]


def f(x: int, m: int) -> bool:
    if x >= 67 and (m == 3 or m == 5):
        return 1
    elif x >= 67 and m < 5:
        return 0
    elif x < 67 and m == 5:
        return 0
    if m & 1 == 0:
        return any([f(op(x), m + 1) for op in operations])
    return all([f(op(x), m + 1) for op in operations])


def g(x: int, m: int) -> bool:
    if x >= 67 and m == 3:
        return 1
    elif x < 67 and m == 3:
        return 0
    elif x >= 67 and m < 3:
        return 0
    if m & 1 == 0:
        return any([g(op(x), m + 1) for op in operations])
    return all([g(op(x), m + 1) for op in operations])


ress = set()
unress = set()
for s in range(1, 67):
    if f(s, 1):
        ress.add(s)
    if g(s, 1):
        unress.add(s)
print(min(ress - unress))
