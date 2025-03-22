n1 = 9**8
n2 = 3**8


def dts(n: int, base: int = 3) -> str:
    nsb = ""
    while n > 0:
        nsb += str(n % base)
        n //= base
    return nsb[::-1]


res = dts(n1 + n2 - 2)
print(res.count("2"))
