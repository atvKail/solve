"""
cat "USE\Решения\24\Демоверсия2025КЕГЭ\data\24_17878.txt" | python "USE\Решения\24\Демоверсия2025КЕГЭ\24.py"
"""

import sys

input = sys.stdin.readline

# s = input().strip()

# n = len(s)
# max_len = 0
# digits = set("0123456789")
# nonzero = set("123456789")

# for start in range(n):
#     if s[start] not in digits:
#         continue
#     i = start
#     expect_operator = False
#     while i < n:
#         if not expect_operator:
#             if s[i] == "0":
#                 i += 1
#                 max_len = max(max_len, i - start)
#                 if i < n and s[i] in digits:
#                     break
#             else:
#                 if s[i] not in nonzero:
#                     break
#                 i += 1
#                 while i < n and s[i] in digits:
#                     i += 1
#                 max_len = max(max_len, i - start)
#             expect_operator = True
#         else:
#             if s[i] in "-*":
#                 i += 1
#                 if i < n and s[i] in digits:
#                     expect_operator = False
#                 else:
#                     break
#             else:
#                 break

# print(max_len)

s = input().strip()
n = len(s)
max_len = 0


digits = set("0123456789")
nonzero = set("123456789")

for start in range(n):
    if s[start] not in digits:
        continue
    i = start

    if s[i] == "0":
        num_val = 0
        i += 1

        if i < n and s[i] in digits:
            max_len = max(max_len, i - start)
            continue
    else:
        if s[i] not in nonzero:
            continue
        num_val = int(s[i])
        i += 1
        while i < n and s[i] in digits:
            num_val = num_val * 10 + int(s[i])
            i += 1

    current_value = num_val
    max_len = max(max_len, i - start)
    expect_operator = True

    while i < n:
        if expect_operator:
            if s[i] not in "-*":
                break
            op = s[i]
            i += 1

            if i >= n or s[i] not in digits:
                break

            if s[i] == "0":
                next_num = 0
                i += 1
                if i < n and s[i] in digits:
                    break
            else:
                if s[i] not in nonzero:
                    break
                next_num = int(s[i])
                i += 1
                while i < n and s[i] in digits:
                    next_num = next_num * 10 + int(s[i])
                    i += 1

            if op == "-":
                current_value = current_value - next_num
            else:
                current_value = current_value * next_num

            if current_value < 0:
                break

            max_len = max(max_len, i - start)
            expect_operator = True
        else:
            break

print(max_len)
