import sys

input = sys.stdin.readline


res = 0
n = int(input())
for x in range(1, n // 2 + 1):
    S = n - x
    if S.bit_count() <= x:
        res += 1
print(res)
