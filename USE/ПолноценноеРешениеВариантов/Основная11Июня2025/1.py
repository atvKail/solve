from itertools import permutations


s = "346 348 12 127 678 15 458 257".split()
v = "DB DC DA AH AD AE BC BD BH HB HG HA CD CB CF FC FG GH GF GE EA EG".split()

print(*range(1, 9))
for p in permutations("ABCDEFGH"):
    if all(str(p.index(b) + 1) in s[p.index(a)] for a, b in v):
        print(*p)
