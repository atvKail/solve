from itertools import *


def f(x: bool, y: bool, z: bool, w: bool) -> bool:
    return (not z or x) and (not x or y) or (w == (z or x))


for a1, a2, a3, a4, a5, a6, a7 in product([1, 0], repeat=7):
    matrix = [(a1, 1, a2, a3), (a4, a5, 1, 1), (a6, 1, a7, 1)]
    if len(matrix) == len(set(matrix)):
        for p in permutations("xyzw"):
            ress = [f(**dict(zip(p, r))) for r in matrix]
            if ress == [0, 0, 0]:
                print(p, sep=" ")
