numbers = list(map(int, open("USE/17/17_16383.txt").readlines()))

max_21 = max(
    num for num in numbers if 10000 <= abs(num) <= 99999 and abs(num) % 100 == 21
)

count_pairs = 0
max_sum = float("-inf")

for i in range(len(numbers) - 1):
    a, b = numbers[i], numbers[i + 1]

    a_condition = 10000 <= abs(a) <= 99999 and abs(a) % 100 == 21
    b_condition = 10000 <= abs(b) <= 99999 and abs(b) % 100 == 21

    if (a_condition != b_condition) and (a**2 + b**2 >= max_21**2):
        count_pairs += 1
        max_sum = max(max_sum, a + b)

print(count_pairs, max_sum)
# 74 103365
