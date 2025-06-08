from math import log2


s = int(-log2(26 + 10 + 470) // 1 * (-1))
v = 61 * 1024 * 8

l = v // (s * 2500)
print(l)
