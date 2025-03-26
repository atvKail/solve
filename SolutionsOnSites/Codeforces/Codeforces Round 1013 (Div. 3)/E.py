import sys

input = sys.stdin.readline


def sieve(max_n):
    is_prime = [True] * (max_n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(max_n**0.5) + 1):
        if is_prime[i]:
            step = i
            for j in range(i * i, max_n + 1, step):
                is_prime[j] = False
    return is_prime


t = int(input().strip())
data = []
max_n = 0
for _ in range(t):
    n = int(input().strip())
    data.append(n)
    if n > max_n:
        max_n = n


is_prime = sieve(max_n)
prefix = [0] * (max_n + 1)
for i in range(1, max_n + 1):
    prefix[i] = prefix[i - 1] + (1 if is_prime[i] else 0)

results = []
for n in data:
    res = 0

    start = 2
    while start <= n:
        q = n // start

        end = n // q
        if end > n:
            end = n

        count = prefix[end] - prefix[start - 1]
        res += q * count
        start = end + 1
    results.append(str(res))

sys.stdout.write("\n".join(results))
