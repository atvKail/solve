from itertools import *

a = "457 46 567 12 138 235 13".split()
s = "FE EC CA AB BD DF GF GC GD".split()
print("1 2 3 4 5 6 7")
for p in permutations("FECABDG"):
    if all([str(p.index(x) + 1) in a[p.index(y)] for x, y in s]):
        print(*p)
