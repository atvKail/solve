for A in range(200, 0, -1):
    res = []
    for x in range(200):
        for y in range(200):
            if (2 * x + y != 110) or (x < y) or (A < x):
                res.append(1)
            else:
                res.append(0)
    if all(res):
        print(A)
        break
