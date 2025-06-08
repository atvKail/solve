from itertools import product, permutations


def f(x: bool, y: bool, w: bool, z: bool) -> bool:
    return not ((not x or w) and not y) or not (z and not (w and y))


for a1, a2, a3, a4, a5, a6, a7 in product([0, 1], repeat=7):
    matrix = [[0, a1, a2, 1], [a3, 1, a4, a5], [1, 0, a6, a7]]
    for p in permutations("xywz"):
        ress = [f(**dict(zip(p, r))) for r in matrix]
        if ress == [0, 0, 0]:
            print(*p, sep="")
