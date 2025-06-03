for A in range(1, 301):
    k = 0
    for x in range(1, 301):
        if ((x & 56 != 0) and (x & 40 == 0)) <= (x & A != 0):
            k += 1
    if k == 300:
        print(A)
        break
