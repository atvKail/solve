operations = [lambda x: x + 1, lambda x: x * 2]

start, end = 1, 45


def f(x, f1, f2):
    if x == 45:
        return 1 and f1 and f2
    if x > 45:
        return 0
    sums = 0
    for op in operations:
        nx = op(x)
        if nx == 18:
            f1 = True
        if nx == 21:
            f2 = False
        sums += f(nx, f1, f2)
    return sums


print(f(start, False, True))
