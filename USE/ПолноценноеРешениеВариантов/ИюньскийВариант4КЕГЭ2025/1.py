from itertools import permutations


s = "26 147 456 237 37 13 245".split()
v = "BD BG GB GF GC FC FE FG EA ED AE AC DE DB".split()

print(*range(1, 8))
for p in permutations("ABCDE    FG"):
    if all(str(p.index(b) + 1) in s[p.index(a)] for a, b in v):
        print(*p)
