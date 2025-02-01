from  sys import setrecursionlimit


setrecursionlimit(30000)


## t1
# def f(n):
#     if n < 2:
#         return 1
#     return 2 * f(n - 1) if  n % 2 == 0 else 4 * n + f(n - 2)

# print(f(45))
## t2
# def f(n):
#     if n <= 2:
#         return 1
#     if n % 2 == 0:
#         return n * f(n - 1) + 2
#     else:
#         return 1 + f(n - 2) + f (n - 1)

# print(f(9))
## t3
# def f(n):
#     if n < 4:
#         return n - 1
#     else:
#         if n % 3 == 0:
#             return n + 2 * f(n - 1)
#         else:
#             return f(n - 2) + f(n - 3)

# print(sum(map(int, list(str(f(25))))))
## t4
# n = 36
# G = [1] * (n + 1)
# F = [1] * (n + 1)
# for i in range(2, 37):
#     F[n] = F[n - 1] - 2 * G[n - 1]
#     G[n] = F[n - 1] + G[n - 1] + n
# print(sum(map(int, list(str(G[36])))))
