from itertools import permutations

matrix = "2678 168 58 5678 34 1247 146 1234".split()
graph = "АГ АЗ АЕ АБ БА БЖ БЕ ЕБ ЕЗ ЕЖ ЗГ ЗА ЗЕ ЖГ ЖБ ЖЕ ЖД ГВ ГЗ ГА ГЖ ВГ ВД ДВ ДЖ".split()

print(*range(1, 9))

for perm in permutations("АБВГДЕЗЖ"):
    if all(str(perm.index(y) + 1) in matrix[perm.index(x)] for x, y in graph):
        print(*perm)