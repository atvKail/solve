"""
cat "USE\\ПолноценноеРешениеВариантов\\ВариантЕГЭФокфорд\\data\\24_3.txt" | python "USE\\ПолноценноеРешениеВариантов\\ВариантЕГЭФокфорд\\24.py"
"""

import sys


input = sys.stdin.readline

s = input()
n = len(s)
left = 0
count_z = 0
max_len = 0
for right in range(n):
    if s[right] == "Z":
        count_z += 1
    while count_z > 3:
        if s[left] == "Z":
            count_z -= 1
        left += 1
    if count_z == 3:
        current_len = right - left + 1
        if current_len > max_len:
            max_len = current_len
print(max_len)
