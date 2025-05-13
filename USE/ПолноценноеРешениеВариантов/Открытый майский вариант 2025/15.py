def to_base7(n: int) -> str:
    if n == 0:
        return "0"
    digits = []
    while n > 0:
        digits.append(str(n % 7))
        n //= 7
    return "".join(reversed(digits))


def find_max_x():
    A = 7**350 + 7**150
    max_x = None

    for x in range(2300, 0, -1):
        N = A - x
        s7 = to_base7(N)
        if s7.count("0") == 200:
            max_x = x
            break
    return max_x


result = find_max_x()
if result is not None:
    print("max x = ", result)
else:
    print(-1)
