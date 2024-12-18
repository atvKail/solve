"""
from sys import setrecursionlimit


setrecursionlimit(30000)
fact = lambda x, res=1: res if x < 1 else fact(x - 1, res * x)
comb = lambda n, k: fact(n) // (fact(n - k) * fact(k))

n = int(input())
rg = comb(n, 4) + comb(n, 2) + 1
print(rg)
"""

n = int(input())
print(int(-n * (n**3 - 6 * n**2 + 23 * n - 18) // 24 * -1 + 1))
