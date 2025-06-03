from itertools import *

a = "356 67 145 37 13 127 246".split()
s = "EF ED FG FC FE CF CG GF GC GB BD BA BG AB AD DE DA DB".split()
print("1 2 3 4 5 6 7")
for p in permutations("ADBGEFC"):
    if all([str(p.index(x) + 1) in a[p.index(y)] for x, y in s]):
        print(*p)
