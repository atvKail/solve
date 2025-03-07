from itertools import product

c = 0
for x in product("0123456789abcdef", repeat=5):
    s = "".join(x)
    if s[0  ] in "2468ace" and s[-1] not in "02468ace":
        if s[0] != s[1] and s[1] != s[2] and s[2] != s[3] and s[3] != s[4]:
            c += 1
print(c)
