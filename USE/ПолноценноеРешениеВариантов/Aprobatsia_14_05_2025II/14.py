def dto7(n: int) -> str:
    num = ''
    alph = "0123456"
    while n != 0:
        num += str(n % 7)
        n //= 7
    return num[::-1]


for x in range(2300, -1, -1):
    n = 7 ** 350 + 7 ** 150 - x
    if dto7(n).count('0') == 203:
        print(x)
        break
