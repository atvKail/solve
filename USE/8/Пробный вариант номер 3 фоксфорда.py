from math import comb


n = 5

case1_positions = comb(n, 1)
case1_variants = 3**(n - 1)
case1_total = case1_positions * case1_variants


case2_positions = comb(n, 2)
case2_variants = 3**(n - 2)
case2_total = case2_positions * case2_variants

total_words = case1_total + case2_total

print(total_words)  