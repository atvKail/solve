# def rec_permutations(el, lgth, curr_permutation=[], result=[]):
#     if len(curr_permutation) == lgth:
#         result.append(curr_permutation.copy())
#         return

#     for _, eln in enumerate(el):
#         new_permutation = curr_permutation + [eln]
#         rec_permutations(el, lgth, new_permutation, result)
#     return result


# n = int(input())
# s = int(input())

# ns = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

# prms = rec_permutations(ns, n)


# for p in prms:
#     nsum = 0
#     x, pps = 0, 0
#     for c in range(n):
#         x = p[c] * 10 ** (n - c - 1)
#         nsum += pps + x
#         pps = pps + x
#     if nsum == s:
#         print(pps)
#         break
# else:
#     print(-1)         # на целых 20 поинтов, вааау


# n = int(input())
# S = input()

# if not S.isdigit():
#     print(-1)
#     exit()

# digits = []
# remaining_sum = 0
# index = 0

# for i in range(n, 0, -1):
#     contribution = i * (10 ** (i - 1))
    
#     while index < len(S) and remaining_sum < contribution:
#         remaining_sum = remaining_sum * 10 + int(S[index])
#         index += 1

#     digit = remaining_sum // contribution
#     if digit < 0 or digit >= 10:
#         print(-1)
#         exit()
    
#     digits.append(str(digit))
#     remaining_sum -= digit * contribution

# if remaining_sum != 0 or index < len(S):
#     print(-1)
# else:
#     print(''.join(digits))    # 50 points


n = int(input())
s = input()

c = 0
sl = len(s) - n
for i in range(sl):
    c = 10 * c + int(s[i])

for i in range(n):
    c = 10 * c + int(s[sl + i])
    print(c // (n - i), end='')
    c %= (n - i)    # 100 points
