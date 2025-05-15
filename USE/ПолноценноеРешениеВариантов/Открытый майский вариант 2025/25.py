import math

def sum_divisors(n):
    s = 0
    r = int(math.isqrt(n))
    for i in range(1, r+1):
        if n % i == 0:
            s += i
            j = n // i
            if j != i:
                s += j
    return s

results = []
n = 500_001
while len(results) < 5:
    R = sum_divisors(n)
    if R % 10 == 6:
        results.append((n, R))
    n += 1

for num, R in results:
    print(f"{num}\t{R}")
