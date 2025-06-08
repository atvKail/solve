from itertools import product


n = 1
pv = 0
alph = list("ЖИВОДЕРНЯ")
for p in sorted(product(alph, repeat=5)):
    w = "".join(p)
    if n & 1 == 0 and w[0] == w[-1] and w.count("Р") >= 2:
        pv = n
    n += 1
print(pv)
