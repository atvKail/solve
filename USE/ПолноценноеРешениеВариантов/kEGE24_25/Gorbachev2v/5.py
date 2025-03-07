def to_base9(n):
    if n == 0:
        return "0"
    digits = []
    while n:
        digits.append(str(n % 9))
        n //= 9
    return "".join(reversed(digits))


def transform(N):
    S = to_base9(N)

    s = sum(int(d) for d in S)
    if s % 2 == 0:
        new_str = S + "52"
    else:
        if len(S) >= 2:
            new_str = "73" + S[2:] + "44"
        else:
            new_str = "73" + "44"

    return int(new_str, 9)


target = 13950
N = 1
while True:
    R = transform(N)
    if R > target:
        print("Минимальное N =", N)
        print("Соответствующее R =", R)
        break
    N += 1
