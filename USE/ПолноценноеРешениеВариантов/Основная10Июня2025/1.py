from itertools import permutations


s = "478 38 256 15 34 37 168 127".split()
v = "HF HB HA BC BF BH CG CB GC GA GD DE DG EF ED FE FB FH AH AG".split()

print(*range(1, 9))
for p in permutations("ABCDEFGH"):
    if all([str(p.index(a) + 1) in s[p.index(b)] for a, b in v]):
        print(*p)
