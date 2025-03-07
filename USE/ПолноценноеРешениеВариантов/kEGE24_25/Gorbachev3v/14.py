for x in range(1, 3052):
    a = 4**151 + 7**283 + 6**82 - 5**x
    c = 0
    while a > 0:
        if a % 8 == 1:
            c += 1
        a = a // 8
    if c == 26:
        print(x)
