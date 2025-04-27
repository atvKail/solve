import sys

input = sys.stdin.readline


L = int(input())
R = int(input())

res = L
k = 1
while (k + 1) * (k + 2) <= 2 * R:
    t = k * (k + 1) // 2
    b = k + 1

    a_min = L - t
    a_max = R - t

    q, r = divmod(a_min, b)
    lw = q + (1 if r > 0 else 0)

    hg = a_max // b
    if lw < 1:
        lw = 1
    if lw <= hg:
        res = min(res, lw)
        if res == 1:
            break
    k += 1
print(res)
