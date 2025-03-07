for x in range(17):
    num1 = f"1B4{x}6"
    num2 = f"1{x}2{x}"

    dnum1 = int(num1, 17)
    dnum2 = int(num2, 17)

    result = dnum1 + dnum2

    if result % 19 == 0:
        quotient = result // 19
        print(f"Наименьшее значение x: {x}")
        print(f"Частное от деления: {quotient}")
        break
