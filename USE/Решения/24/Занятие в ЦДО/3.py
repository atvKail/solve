"""
cat "USE\Решения\24\Занятие в ЦДО\data\demo_2025_24.txt" | python "USE\Решения\24\Занятие в ЦДО\3.py"
"""

import sys


input = sys.stdin.readline

s = input().strip()

s = s.replace("-", "*")
s = s.replace("*0*", "*5*")
while "**" in s:
    s = s.replace("**", "*x*")
s = s.replace("*0", "x")
s = s.replace("x0", "x")
a = s.split("x")
ml = -1
for i in a:
    if len(i) > 1:
        if i[0] == "*":
            i = i[1:]
        if i[-1] == "*":
            i = i[:-1]
        ml = max(ml, len(i))
print(ml)
