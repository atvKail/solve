import re
from itertools import product


def is_valid(s):
    if s[0] == "0":
        return False
    if len(set(s)) != 7:
        return False
    for a, b in zip(s, s[1:]):
        if int(a) % 2 == int(b) % 2:
            return False
    return True


cnt = 0
c = 0
alph = "01234567"

for p in product(alph, repeat=7):
    p = "".join(p)
    if is_valid(p):
        cnt += 1
    c += 1

print(cnt)
print(c)

# import re
# from itertools import product

# pattern = re.compile(r"^(?!0)(?!.*(.).*\1)(?!.*(?:[0246]{2}|[1357]{2}))[0-7]{7}$")

# cnt = 0
# total = 0
# for p in product("01234567", repeat=7):
#     s = "".join(p)
#     total += 1
#     if pattern.match(s):
#         cnt += 1

# print(cnt)
# print(total)
