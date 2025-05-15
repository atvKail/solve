operations = [lambda x: x + 1, lambda x: x + 4, lambda x: x * 3]

end = 67


def f(x, p):
    if x >= 67 and p == 3:
        return 1
    elif p == 3 and x < 67:
        return 0
    elif p < 3 and x >= 67:
        return 0
    if p & 1 == 0:
        return all(f(op(x), p + 1) for op in operations)
    else:
        return any(f(op(x), p + 1) for op in operations)


for x in range(1, 67):
    if f(x, 1) == 1:
        print(x)
        break
