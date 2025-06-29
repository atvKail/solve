from itertools import product, permutations


def f(x, y, w, z) -> bool:
    return (not x or y) and z and not w


for a1, a2, a3, a4, a5, a6 in product([0, 1], repeat=6):
    matrix = [
        (0, 1, a1, a2),
        (1, 1, a3, a4),
        (1, a5, 1, a6)
    ]
    if len(matrix) == len(set(matrix)):
        for p in permutations("xyzw"):
            ress = [f(**dict(zip(p, r))) for r in matrix]
            if ress == [1, 1, 1]:
                print(*p, sep='')
