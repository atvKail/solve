def process_number(n):
    binary_n = bin(n)[2:]

    digit_sum = sum(int(digit) for digit in binary_n)

    if digit_sum % 2 == 0:
        new_binary = "10" + binary_n[:-1] + "1"
    else:
        if len(binary_n) >= 2:
            new_binary = "1" + binary_n[:-2] + "10"
        else:
            new_binary = "1" + binary_n.zfill(2).replace(binary_n[-2:], "10")

    return int(new_binary, 2)


n = 1
while True:
    r = process_number(n)
    if r > 60:
        print(n)
        break
    n += 1
