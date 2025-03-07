"""
cat "USE\Решения\27\ЗанятиеФОКС27заданиеОбработкаЧисловойПоследовательности\data\27a2.txt" | python "USE\Решения\27\ЗанятиеФОКС27заданиеОбработкаЧисловойПоследовательности\27_2.py"
"""

import sys


input = sys.stdin.readline

n = int(input().strip())
data = []
prefix = [0] * (2 * n + 1)

for idx in range(n):
    x = int(input().strip())
    prefix[idx + 1] = prefix[idx] + x
    data.append(x)

for i in range(n, 2 * n):
    prefix[i + 1] = prefix[i] + data[i - n]

rem_map = {}
max_sum = float("-inf")

for j in range(1, 2 * n + 1):
    curr_sum = prefix[j]
    curr_rem = curr_sum % 13
    curr_len = j % 13

    if (curr_rem, curr_len) in rem_map:
        for i, sum_i in rem_map[(curr_rem, curr_len)]:
            if j - i <= n:
                max_sum = max(max_sum, curr_sum - sum_i)
                break

    if (curr_rem, curr_len) not in rem_map:
        rem_map[(curr_rem, curr_len)] = []
    rem_map[(curr_rem, curr_len)].append((j, curr_sum))

    rem_map[(curr_rem, curr_len)] = [
        (i, sum_i) for i, sum_i in rem_map[(curr_rem, curr_len)] if j - i <= n
    ]


print(max_sum)
