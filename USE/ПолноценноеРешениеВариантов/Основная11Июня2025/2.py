from itertools import permutations, product


def f(x: bool, y: bool, w: bool, z: bool) -> bool:
    return not(not w or (x == y)) and (not z or x)


for a1, a2, a3, a4, a5 in product([1, 0], repeat=5):
    matrix = [
        (a1, 0, 1, 0),
        (0, a2, a3, 0),
        (a4, 1, 1, a5)
    ]

    if len(matrix) == len(set(matrix)):
        for p in permutations("xywz"):
            res = [f(**dict(zip(p, r))) for r in matrix]
            if res == [1, 1, 1]:
                print(*p, sep="")
                