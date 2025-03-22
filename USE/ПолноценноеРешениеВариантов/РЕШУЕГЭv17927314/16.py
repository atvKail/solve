# import sys

# sys.setrecursionlimit(6000)


# def f(a: int, b: int) -> int:
#     if not b:
#         return a
#     if a >= b > 0:
#         return f(a - b, b)
#     else:
#         return f(b, a)


# cnt = 0
# for n in range(123456798, 1234567885 + 1):
#     c1 = n // 15
#     n1 = n - c1 * 15
#     if f(n1, 15) == 1:
#         cnt += 1
# print(cnt) # Очень долго, фактически надо искать числа, что не имеют общих делителей с числом 15

dl3 = len(range(123456798, 1234567886, 3))
dl5 = len(range(123456800, 1234567886, 5))
dl15 = len(range(123456810, 1234567886, 15))
print(len(range(123456798, 1234567886)) - (dl5 + dl3) + dl15)
