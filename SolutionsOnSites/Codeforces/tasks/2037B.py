# def primfacs(n):
#     i = 2
#     primfac = [1, n]
#     while i * i <= n:
#         while n % i == 0:
#             primfac.append(i)
#             n = n / i
#         i = i + 1
#     if n > 1:
#         primfac.append(n)
#     return primfac


def main():
    import sys
    import math
    from collections import Counter

    input = sys.stdin.readline

    results = []
    t = int(input().strip())
    for _ in range(t):
        k = int(input())
        a = sorted(list(map(int, input().strip().split())))

        freq = Counter(a)
        prod = k - 2
        for d in range(1, math.isqrt(prod) + 1):
            if prod % d == 0:
                e = prod // d
                if d == e:
                    if freq[d] >= 2:
                        results.append(f"{d} {e}")
                        break
                else:
                    if freq[d] >= 1 and freq[e] >= 1:
                        results.append(f"{d} {e}")
                        break

    print("\n".join(results))


if __name__ == "__main__":
    main()

# Отправка не на pypy, pypy не проходит по времени, а python проходит