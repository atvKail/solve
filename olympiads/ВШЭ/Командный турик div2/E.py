import sys
from collections import Counter

input = sys.stdin.readline


n = int(input())
cnt = Counter()

for i in range(1, n + 1):
    s = input()
    key = "".join(sorted(s))
    cnt[key] += 1

ans = sum(c * (c - 1) // 2 for c in cnt.values())
print(ans)
