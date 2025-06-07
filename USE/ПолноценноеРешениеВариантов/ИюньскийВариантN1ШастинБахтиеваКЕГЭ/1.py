from itertools import *


a = "45 4567 56 12 123 237 26".split()
s = "ДВ ДЖ ВЕ ВД ЕЖ ЕВ ЕГ ГБ ГЕ БЖ БА БГ ЖА ЖБ ЖЕ ЖД АБ АЖ".split()
print("1 2 3 4 5 6 7")
for p in permutations("ДЖВЕАБГ"):
    if all([str(p.index(x) + 1) in a[p.index(y)] for x, y in s]):
        print(*p)
