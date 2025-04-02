def searchMaxMin(n: int) -> tuple:
    from math import sqrt

    prime = []

    def is_prime(de: int) -> bool:
        for p in prime:
            if de % p == 0:
                return 0
        return 1

    minm, maxm = 1e10, -1
    for d in range(2, int(sqrt(n)) + 1):
        if n % d == 0:
            if is_prime(d):
                while n % d == 0:
                    n //= d
                prime.append(d)
                maxm = max(maxm, d)
                minm = min(minm, d)
    if is_prime(n):
        maxm = max(n, maxm)
    # print(prime, n)
    return minm, maxm


cnt = 0
for n in range(610000, 610000 * 1000):
    if cnt == 3:
        break
    mi, mx = searchMaxMin(n)
    M = mx - mi
    if M % 87 == 21:
        print(n, M)
        cnt += 1

# Исравлено, выдаёт верный ответ, поспешил...