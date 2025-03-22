"""
cat "USE\ПолноценноеРешениеВариантов\РЕШУЕГЭv17927314\data\1_17.txt" | python "USE\ПолноценноеРешениеВариантов\РЕШУЕГЭv17927314\17.py"
"""

import sys

input = sys.stdin.read


data = list(map(int, input().strip().split()))
mx = max((x for x in data if x % 100 == 17), default=-1)

cnt = 0
for i in range(len(data) - 2):
    triplet = data[i : i + 3]
    c1 = sum(100 <= abs(x) <= 999 for x in triplet) == 1
    c2 = sum(triplet) < mx
    cnt += c1 and c2
print(cnt)
