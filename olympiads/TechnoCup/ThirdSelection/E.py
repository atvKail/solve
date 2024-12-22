# import math


# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, int(math.sqrt(n)) + 1):
#         if n % i == 0:
#             return False
#     return True


# def sum_dgts_in_base(x, b):
#     ttl = 0
#     while x > 0:
#         ttl += x % b
#         x //= b
#     return ttl


# results = []
# for _ in range(int(input())):
#     x = int(input())
#     count = 0
#     for b in range(2, x + 1):
#         dgts_sum = sum_dgts_in_base(x, b)
#         diff = x - dgts_sum
#         if is_prime(diff):
#             count += 1
#     print(count)




# import math


# def sieve(limit):
#     is_prime = [True] * (limit + 1)
#     is_prime[0] = is_prime[1] = False
#     for i in range(2, int(math.sqrt(limit)) + 1):
#         if is_prime[i]:
#             for j in range(i * i, limit + 1, i):
#                 is_prime[j] = False
#     return is_prime


# def sum_dgts_in_base(x, b):
#     ttl = 0
#     while x > 0:
#         ttl += x % b
#         x //= b
#     return ttl


# t = int(input())
# tcases = [int(input()) for _ in range(t)]

# max_x = max(tcases)
# max_diff = max_x - 1

# is_primes = sieve(max_diff)

# for x in tcases:
#     count = 0
#     for b in range(2, x + 1):
#         dgts_sum = sum_dgts_in_base(x, b)
#         diff = x - dgts_sum
#         if diff > 1 and is_primes[diff]:
#             count += 1
#     print(count)

import math


def sieve(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(math.sqrt(limit)) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False
    return is_prime


def sum_dgts_in_base(x, b):
    ttl = 0
    while x > 0:
        ttl += x % b
        x //= b
    return ttl


t = int(input())
tcases = [int(input()) for _ in range(t)]

maxx = max(tcases)

is_primes = sieve(maxx)

for x in tcases:
    count = 0
    for b in range(2, x + 1):
        dgts_sum = sum_dgts_in_base(x, b)
        diff = x - dgts_sum
        if diff > 1 and is_primes[diff]:
            count += 1
    print(count)