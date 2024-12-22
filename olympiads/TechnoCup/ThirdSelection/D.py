# from collections import Counter


# def popcount(x):
#     return bin(x).count("1")


# n, b = map(int, input().split())
# a = list(map(int, input().split()))

# ans = 0

# for k in range(n):
#     ak = a[k]

#     # pair: ai + aj = ak и ai ⊕ aj = ak
#     cnt_pairs = Counter()
#     for i in range(k):
#         ai = a[i]
#         aj = ak - ai
#         if aj < 0 or aj >= (1 << b):
#             continue

#         if ai & aj == 0 and popcount(ai) + popcount(aj) == b:
#             ans += cnt_pairs[aj]

#         cnt_pairs[ai] += 1

# print(ans)


# def popcount(x):
#     return bin(x).count("1")


# n, b = map(int, input().split())
# a = list(map(int, input().split()))
# ans = 0
# cnt_global = [0] * (1 << b)

# for k in range(n):
#     ak = a[k]
#     cnt_pairs = [0] * (1 << b)

#     for i in range(k):
#         ai = a[i]
#         aj = ak - ai

#         if 0 <= aj < (1 << b):
#             if ai & aj == 0 and popcount(ai) + popcount(aj) == b:
#                 ans += cnt_pairs[aj]

#         cnt_pairs[ai] += 1

#     cnt_global[ak] += 1

# print(ans)


def popcount(x):
    return bin(x).count("1")


n, b = map(int, input().split())
a = list(map(int, input().split()))
ans = 0
cnt_global = [0] * (1 << b)
bit_counts = [popcount(x) for x in range(1 << b)]

for k in range(n):
    ak = a[k]
    cnt_pairs = [0] * (1 << b)

    for i in range(k):
        ai = a[i]
        aj = ak - ai

        if 0 <= aj < (1 << b):
            if ai & aj == 0 and bit_counts[ai] + bit_counts[aj] == b:
                ans += cnt_pairs[aj]

        cnt_pairs[ai] += 1

print(ans)
