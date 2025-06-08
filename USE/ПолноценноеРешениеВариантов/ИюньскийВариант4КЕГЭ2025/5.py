def f(n: int) -> int:
    def dto3(x: int) -> str:
        dn = ""
        while x != 0:
            dn += str(x % 3)
            x //= 3
        return dn[::-1]

    dn = dto3(n)
    if n % 5 == 0:
        dn += dn[-2:]
    else:
        dn += dto3(n % 5 * 2)
    return int(dn, 3)


mx = -1
for i in range(1, 10000):
    x = f(i)
    mx = max(mx, x if x <= 514 else -1)
print(mx)
