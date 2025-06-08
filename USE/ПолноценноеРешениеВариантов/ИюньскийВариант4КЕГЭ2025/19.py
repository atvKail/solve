operations = [
    lambda a, b: [a - 2, b],
    lambda a, b: [a // 2, b],
    lambda a, b: [a, b - 2],
    lambda a, b: [a, b // 2],
]


def f(heaps: list[int], h: int) -> bool:
    if sum(heaps) <= 212 and h == 3:
        return True
    elif sum(heaps) <= 212 and h < 3:
        return False
    elif sum(heaps) > 212 and h == 3:
        return False
    else:
        return any([f(op(*heaps), h + 1) for op in operations])


for s in range(1000, 102, -1):
    if f([s, 110], 1):
        print(s)
        break
