oprations = [
    lambda x: x - 2,
    lambda x: x - 5,
    lambda x: x // 3
]


def f(s: int, m: int) -> bool:
    if s <= 19 and (m == 3 or m == 5):
        return 1
    elif s <= 19 and m < 5:
        return 0
    elif s > 19 and m == 5:
        return 0
    if m & 1 == 0:
        return any([f(op(s), m + 1) for op in oprations])
    else:
        return all([f(op(s), m + 1) for op in oprations])


def g(s: int, m: int) -> bool:
    if s <= 19 and (m == 3):
        return 1
    elif s <= 19 and m < 3:
        return 0
    elif s > 19 and m == 3:
        return 0
    if m & 1 == 0:
        return any([g(op(s), m + 1) for op in oprations])
    else:
        return all([g(op(s), m + 1) for op in oprations])


ress = set()
unress = set()
for s in range(20, 100):
    if f(s, 1):
        ress.add(s)
for s in range(20, 100):
    if g(s, 1):
        unress.add(s)
print(ress, '-', unress)
print(ress - unress)
