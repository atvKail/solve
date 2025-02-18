def transform(N):
    b = bin(N)[2:]
    s = sum(int(digit) for digit in b)

    if s % 4 == 0:
        new_b = b + "01"
        new_b = "10" + new_b[2:]
    else:
        new_b = b + "1"
        new_b = "11" + new_b[1:]
    return int(new_b, 2)


target = 127
N = 1

while True:
    R = transform(N)
    if R >= target:
        print("Минимальное число N =", N, "→ R =", R)
        break
    N += 1
