operations = [
    lambda a, b: [a - 2, b],
    lambda a, b: [a // 2, b],
    lambda a, b: [a, b - 2],
    lambda a, b: [a, b // 2],
]


def f(heaps, h):
    if sum(heaps) <= 212 and (h == 3 or h == 5):
        return True
    elif sum(heaps) <= 212 and h < 5:
        return False
    elif sum(heaps) > 212 and h == 5:
        return False
    else:
        if h % 2 != 0:
            return all(f(op(*heaps), h + 1) for op in operations)
        else:
            return any(f(op(*heaps), h + 1) for op in operations)


def g(heaps: list[int], h: int):
    if sum(heaps) <= 212 and h == 3:
        return True
    elif sum(heaps) <= 212 and h < 3:
        return False
    elif sum(heaps) > 212 and h == 3:
        return False
    else:
        if h % 2 != 0:
            return all(g(op(*heaps), h + 1) for op in operations)
        else:
            return any(g(op(*heaps), h + 1) for op in operations)


ress = set()
for s in range(102, 1000):
    if f([s, 110], 1):
        ress.add(s)
for s in range(102, 1000):
    if g([s, 110], 1):
        ress -= {s}
print(max(ress))
