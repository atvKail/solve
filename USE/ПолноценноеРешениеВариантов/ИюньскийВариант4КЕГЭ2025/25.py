def sieve(n: int) -> list[int]:
    is_prime = [True] * (n + 1)
    is_prime[0:2] = [False, False]
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return [i for i, prime in enumerate(is_prime) if prime]


MAX_N = 987654

primes = sieve(MAX_N)
primesEnd17 = [p for p in primes if p != 17 and p % 100 == 17]

ress = []
for n in range(MAX_N - 1, 0, -1):
    for p in primesEnd17:
        if p >= n:
            continue
        if n % p == 0:
            ress.append((n, p))
            break
    if len(ress) >= 5:
        break
for n, p in ress:
    print(n, p)
