from itertools import permutations, product


def F(x, y, z, w):
    return (x and not y) or (x == z) or (not w)


row1 = [0, 1, 1, 0]
row2 = [0, None, None, None]
row3 = [None, 1, 0, 1]

for perm in permutations(["w", "x", "y", "z"]):
    vals1 = {var: bool(row1[i]) for i, var in enumerate(perm)}
    if F(vals1["x"], vals1["y"], vals1["z"], vals1["w"]) is not False:
        continue

    ok3 = False
    for b in (0, 1):
        r3 = [b, row3[1], row3[2], row3[3]]
        vals3 = {var: bool(r3[i]) for i, var in enumerate(perm)}
        if F(vals3["x"], vals3["y"], vals3["z"], vals3["w"]) is False:
            ok3 = True
            break
    if not ok3:
        continue

    ok2 = False
    for bits in product((0, 1), repeat=3):
        r2 = [row2[0], *bits]
        vals2 = {var: bool(r2[i]) for i, var in enumerate(perm)}
        if F(vals2["x"], vals2["y"], vals2["z"], vals2["w"]) is False:
            ok2 = True
            break
    if not ok2:
        continue
    print(perm)
    break
