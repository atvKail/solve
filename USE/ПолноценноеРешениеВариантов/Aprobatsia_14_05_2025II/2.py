from itertools import *


def f(x: int, y: int, z: int, w: int) -> bool:
    return (not x and not y) or (y == z) or w


for a1, a2, a3, a4 in product([0, 1], repeat=4):
    matrix = [
        (0, 1, a1, a2),
        (1, a3, 1, 0),
        (a4, 1, 1, 0)
    ]
    if len(matrix) == len(set(matrix)):
        for p in permutations("xyzw"):
            ress = [f(**dict(zip(p, r))) for r in matrix]
            if ress == [0, 0, 0]:
                print(*p, sep="")
