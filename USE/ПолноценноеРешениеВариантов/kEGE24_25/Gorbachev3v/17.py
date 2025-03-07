def is_good(x):
    return (x % 11 == 0) and (abs(x) % 10 == 3)

numbers = []
with open("USE\\ПолноценноеРешениеВариантов\\kEGE24_25\\Gorbachev3v\\17.txt", 'r', encoding=None) as f:
    for line in f:
        numbers.extend(map(int, line.split()))

count_triplets = 0
min_sum_of_triplet = None

for i in range(len(numbers) - 2):
    triple = numbers[i : i+3]
    good_count = sum(is_good(x) for x in triple)

    if good_count == 2:
        s = sum(triple)
        count_triplets += 1
        if min_sum_of_triplet is None or s < min_sum_of_triplet:
            min_sum_of_triplet = s

if count_triplets > 0:
    print(count_triplets, 2 * min_sum_of_triplet)
else:
    print(0, 0)
