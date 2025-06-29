from itertools import product


i = 1
prev = None
for p in sorted(product("ТЕОРИЯ", repeat=6)):
    if p.count('И') >= 2 and p[0] not in {'Р', 'Т', 'Я'} and not i & 1 == 0:
        prev = i
    i += 1
print(prev)
