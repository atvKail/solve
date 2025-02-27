# import sys


# def fmid(el, n, k, penl):
#     i = 0
#     cntinterval = 0
#     while i < n:
#         if penl[i] > el and s[i] == "R":
#             i += 1
#             continue
#         segfb = False
#         while i < n and not (penl[i] > el and s[i] == "R"):
#             if penl[i] > el and s[i] == "B":
#                 segfb = True
#             i += 1
#         if segfb:
#             cntinterval += 1
#     return cntinterval <= k


# input = sys.stdin.readline

# results = []
# t = int(input())
# for _ in range(t):
#     n, k = map(int, input().split())
#     s = input()
#     penl = list(map(int, input().split()))

#     l, r = 0, max(penl)
#     ans = r
#     while l <= r:
#         mid = (l + r) // 2
#         if fmid(mid, n, k, penl):
#             ans = mid
#             r = mid - 1
#         else:
#             l = mid + 1

#     results.append(str(ans))
# print("\n".join(results))  # tl на 4 тесте


import sys


input = sys.stdin.readline

t = int(input())
results = []
for _ in range(t):
    n, k = map(int, input().split())
    s = input().strip()
    penl = list(map(int, input().split()))

    l, r = 0, max(penl)
    ans = r
    while l <= r:
        mid = (l + r) // 2
        cnt = 0
        fnd = False
        for i in range(n):
            if penl[i] > mid:
                if s[i] == "R":
                    if fnd:
                        cnt += 1
                        fnd = False
                else:
                    fnd = True
        if fnd:
            cnt += 1
        if cnt <= k:
            ans = mid
            r = mid - 1
        else:
            l = mid + 1
    results.append(str(ans))
print("\n".join(results))
