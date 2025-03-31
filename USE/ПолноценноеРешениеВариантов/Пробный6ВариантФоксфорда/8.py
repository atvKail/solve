# def dto9(n : int) -> str:
#     d9 = ""
#     while n != 0:
#         d9 += str(n % 9)
#         n //= 9
#     return d9[::-1]


# cnt = 0
# for n in range(6561, 59049):
#     n9 = dto9(n)
#     if n9.count('0') == 1:
#         i = n9.find('0')
#         if (int(n9[(i - 1)]) & 1 != 0):
#             if i + 1 >= 5:
#                 cnt += 1 
#             elif (int(n9[(i + 1)]) & 1 != 0):
#                 cnt += 1
# print(cnt)

# # x = input()
# # i = int(input())
# # print((i - 1 ) % 5)
# # print(x, (int(x[(i - 1) % 5]) & 1 != 0) and (int(x[(i + 1) % 5]) & 1 != 0))