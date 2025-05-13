from itertools import permutations, product


cnt = 0
for x in product("ГОД", repeat=6):
    if x[0] in "ГД" and x[1] in "ГД":
        cnt += 1
print(cnt)
