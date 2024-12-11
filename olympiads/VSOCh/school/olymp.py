# n = int(input())
# m = int(input())
# a = int(input())
# b = int(input())

# print(n * m + a * b - a * m - b * n) # task 1



# a, b, c, d = [int(input()) for _ in range(4)]
# if b + c == 0:
#     print(max(a, d))
# elif b - c == 0:
#     print(sum([a, b, c, d]))
# else:
#     print(1 + a + d + 2 * min(b, c))  # task 2



# def main():
#     d1, m1, y1, d2, m2, y2, n = [int(input()) for _ in range(7)]
#     l = [int(input()) for _ in range(n)]

#     if y1 == y2:
#         return f(d2, m2, l) - f(d1, m1, l) + 1

#     daysFY = sum(l[m1-1:]) - d1 + 1
#     daysLY = f(d2, m2, l)

#     daysFullY = 0
#     if y2 > y1 + 1:
#         daysFullY = (y2 - y1 - 1) * sum(l)

#     return daysFY + daysFullY + daysLY

# if __name__ == "__main__":
#     print(main()) # task 3



# n, l, k = [int(input()) for _ in range(3)]
# org = input()
# sorg = ''.join(sorted(org))
# cvalid = 0

# for _ in range(n):
#     curr = input()
#     scurr = ''.join(sorted(curr))
    
#     if sorg == scurr:
#         mt = sum(1 for j in range(l) if org[j] == curr[j])
#         if l - mt <= k:
#             cvalid += 1

# print(cvalid) # task 4



# import math
# from collections import Counter


# x = int(input())
# i = 2
# fcts = []
# n = x
# while i * i <= n:
#     while (n % i) == 0:
#         fcts.append(i)
#         n //= i
#     i += 1
# if n > 1:
#     fcts.append(n)
# count = Counter(fcts)
# n = 1
# for factor, power in count.items():
#     if power % 2 != 0:
#         n *= factor
# print(n)  # task 2


# def f(d, m, l):
#     return sum(l[:m-1]) + d   # task 5