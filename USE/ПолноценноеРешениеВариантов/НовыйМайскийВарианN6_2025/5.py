def f(n: int) -> int:
    binn = bin(n)[2:][::-1]
    while (binn[0] == '0'):
        binn = binn[1:]
    return int(binn if binn != '' else '0', 2)


for n in range(100, -1, -1):
    res = f(n)
    if res == 13:
        print(n)
        break
