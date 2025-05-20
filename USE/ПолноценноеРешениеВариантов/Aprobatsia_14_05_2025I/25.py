def has_valid_divisor(n):
    mdiv = None

    for d in range(1, int(n**0.5) + 1):
        if n % d == 0:
            if d != 7 and d != n and d % 10 == 7:
                if mdiv is None or d < mdiv:
                    mdiv = d

            if n // d != 7 and n // d != n and (n // d) % 10 == 7:
                if mdiv is None or n // d < mdiv:
                    mdiv = n // d
    return mdiv


ress = []
n = 800001

while len(ress) < 5:
    divisor = has_valid_divisor(n)
    if divisor is not None:
        ress.append((n, divisor))
    n += 1

print("Число | Делитель")
print("-" * 20)
for num, div in ress:
    print(f"{num} | {div}")
