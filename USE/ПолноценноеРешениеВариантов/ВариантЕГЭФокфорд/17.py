# file = "USE\\ПолноценноеРешениеВариантов\\ВариантЕГЭФокфорд\\data\\17.txt"
"""
cat "USE\\ПолноценноеРешениеВариантов\\ВариантЕГЭФокфорд\\data\\17.txt" | python "USE\\ПолноценноеРешениеВариантов\\ВариантЕГЭФокфорд\\17.py"
"""

import sys
from heapq import heappush, heappop
import bisect


input = sys.stdin.readline

minel = 10001
p = None
data = []
while (x := input()) != "":
    n = int(x.strip())
    minel = min(minel, n)
    if p is None:
        p = n
        continue
    else:
        if (n % 10 == 5 and p % 10 != 5) or (n % 10 != 5 and p % 10 == 5):
            heappush(data, [(n + p) ** 2, (n, p)])
        p = n


data = data[bisect.bisect_right(data, minel**2, key=lambda x: x[0]) :]
print(f"{len(data)} \n {max(data, key=lambda x: x[0])}")