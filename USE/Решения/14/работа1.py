# from NumberSystems import *


# num = 3 * 2187 ** 2020 + 3 * 729 ** 2021 - 2 * 81 ** 2022 + 27 ** 2023 - 4 * 3 ** 2024 - 2029
# Num27 = convertDecimalToXns(num, 27)
# c = 0
# for d in Num27:
#     if d in 'abcdefghijklmnopqrstuvwxyz':
#         c += 1
# print(c)

# a = '0123456789abcdefghijklmnopqrstuvwxyz'

# maxs = 0
# for x in range(0, 20):
#     n1 = num(f'{a[x]}1{a[x]}2{a[x]}3{a[x]}4', 20)
#     for y in range(0, 5):
#         n2 = num(f'1{y}2{y}3{y}4{y}', 5)
#         num7iadd = (n1 - n2)
#         maxs = max(maxs, sum(map(int, list(convertDecimalToXns(int(num7iadd.Number, num7iadd.Base), 7)))))
# print(maxs)

# maxs = 0
# for x in range(20):
#     n = num(f'12{a[x]}34', 20)
#     iaddn = num(str(9**500), 10) - n
#     maxs = max(maxs, sum(map(int, list(convertDecimalToXns(int(iaddn.Number, iaddn.Base), 9)))))
# print(maxs)

# for n in range(1000):
#     if num('110', n) == num('39800', 10):
#         print(n)
#         break

# sumn = 0
# for n in range(2, 50):
#     if len(convertDecimalToXns(100, n)) == 3:
#         sumn += n
# print(sumn)