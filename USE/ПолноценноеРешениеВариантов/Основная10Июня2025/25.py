N = 1_324_727


def f(x: int) -> list[int]:
    from math import sqrt

    res = []
    for d in range(2, int(sqrt(x)) + 1):
        if x % d == 0:
            res.append(d)
            res.append(x // d)
    return res


x = N
cnt = 0
while cnt < 5:
    dpair = f(x)
    if len(dpair) == 2:
        df, ds = [f(d) for d in dpair]
        if len(df) == len(ds) == 0:
            print(x, max(dpair))
            cnt += 1
    x += 1
