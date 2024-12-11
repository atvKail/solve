g, f = [int(input()) for _ in range(2)]

l, r = 1, 2 * 10**9

while l < r:
    n = (l + r) // 2
    ttg = n * g
    ttc = n * f + (n * (n - 1)) // 2

    if ttg < ttc:
        r = n
    else:
        l = n + 1

print(l)
