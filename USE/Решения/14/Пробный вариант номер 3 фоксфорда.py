def to_decimal(number, base):
    return int(number, base)


base = 18

for x in range(base):
    num1 = f"143{x}4"
    num2 = f"1{x}315"

    decimal_num1 = to_decimal(num1, base)
    decimal_num2 = to_decimal(num2, base)

    total = decimal_num1 + decimal_num2

    if total % 17 == 0:
        quotient = total // 17
        print(f"x = {x}, Частное = {quotient}")
        break
