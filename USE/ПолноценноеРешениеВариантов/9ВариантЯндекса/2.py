from itertools import product, permutations


def F(x: bool, y: bool, z: bool, w: bool) -> bool:
    return (not z or x) and (not y and (not w == y))


for x1, x2, x3, x4, x5 in product(range(2), repeat=5):
    matrix = [
        [4, 0, 1, x1, 0, 0],
        [4, 1, x2, 0, x3, 0],
        [4, 0, 1, 1, x4, 1],
        [4, x5, 1, 1, 1, 1],
    ]

    for perm in permutations(range(4)):
