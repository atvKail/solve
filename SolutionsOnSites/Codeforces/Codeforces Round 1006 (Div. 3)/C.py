from math import log2, ceil
import sys


input = sys.stdin.readline

results = []
for _ in range(int(input())):
    n, x = map(int, input().split())

    if n == 1:
        print(x)
        continue

    m_max = 0
    for m in range(n, 0, -1):
        if m == 1:
            k = 0
        else:
            k = ceil(log2(m))
        R = 0 if k == 0 else (1 << k) - 1
        if (R & x) != R:
            continue
        if R == x:
            if m <= n:
                m_max = m
                break
        else:
            if m + 1 <= n:
                m_max = m
                break

    key = []
    for i in range(m_max):
        key.append(i)
    if m_max == 1:
        k = 0
    else:
        k = ceil(log2(m_max))
    R = 0 if k == 0 else (1 << k) - 1

    if R != x:
        key.append(x)
    key.extend([0] * (n - len(key)))
    results.append((" ".join(map(str, key))))
print("\n".join(results))
