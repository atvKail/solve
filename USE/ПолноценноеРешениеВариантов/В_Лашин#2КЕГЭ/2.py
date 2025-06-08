from itertools import *


def f(x: bool, y: bool, w: bool, z: bool) -> bool:
    return (w == (not (not y or z))) and x


for a1, a2, a3, a4, a5, a6 in product([1, 0], repeat=6):
    matrix = [(0, a1, a2, a3), (0, 0, a4, a5), (0, 0, 0, a6)]
    if len(matrix) == len(set(matrix)):
        for p in permutations("xyzw"):
            ress = [f(**dict(zip(p, r))) for r in matrix]
            if ress == [1, 1, 1]:
                print(*p)
