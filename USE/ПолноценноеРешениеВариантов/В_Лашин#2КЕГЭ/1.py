from itertools import *


s = "346 56 14 13 26 125".split()
v = "DE DF EF ED FD FE FA AF AC AB BA BC CB CA".split()
print(*range(1, 7))
for p in permutations("ABCDEF"):
    if all(str(p.index(b) + 1) in s[p.index(a)] for a, b in v):
        print(*p)
