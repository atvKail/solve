operations = [
    lambda a, b: [a - 2, b],
    lambda a, b: [a // 2, b],
    lambda a, b: [a, b - 2],
    lambda a, b: [a, b // 2],
]


def f(heaps: list[int], h: int):
    if sum(heaps) <= 212 and h == 4:
        return True
    elif sum(heaps) <= 212 and h < 4:
        return False
    elif sum(heaps) > 212 and h == 4:
        return False
    else:
        if h % 2 != 0:
            return any([f(op(*heaps), h + 1) for op in operations])
        else:
            return all([f(op(*heaps), h + 1) for op in operations])


ress = []
for s in range(102, 1000, 1):
    if f([s, 110], 1):
        ress.append(s)
print(min(ress), max(ress))
