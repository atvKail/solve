def divs(n: int) -> tuple[set[int], int]:
    from math import sqrt

    sums = 0
    dvs = set()
    for d in range(1, int(sqrt(n)) + 1):
        if n % d == 0 and d not in dvs:
            dvs.add(d)
            dvs.add(n // d)
            sums += d + n // d
    return dvs, sums


cnt = 0
for x in range(500000, 1000001):
    ddvs = divs(x)
    R = ddvs[1]

    if R % 10 == 2:
        print(x, R)
        cnt += 1
    if cnt >= 5:
        break
