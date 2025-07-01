import math


def compute_M(x: int) -> int:
    n = x
    primed = set()
    d = 2
    while d * d <= n:
        if n % d == 0:
            primed.add(d)
            while n % d == 0:
                n //= d
        d += 1 if d == 2 else 2
    if n > 1:
        primed.add(n)

    primed.discard(x)
    if not primed:
        return 0
    return min(primed) + max(primed)


def is_palindrome(num: int) -> bool:
    s = str(num)
    return s == s[::-1]


N = 5_400_000
found = []
x = N + 1
while len(found) < 5:
    M = compute_M(x)
    if M > 60_000 and is_palindrome(M):
        found.append((x, M))
    x += 1

for x, m in found:
    print(x, m)
