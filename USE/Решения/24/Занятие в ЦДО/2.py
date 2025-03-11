"""
cat "USE\Решения\24\Занятие в ЦДО\data\24(1).txt" | python "USE\Решения\24\Занятие в ЦДО\2.py"
"""

import sys


input = sys.stdin.readline

s = input().strip()

replacement_list = [
    ("2", "1"),
    ("3", "1"),
    ("4", "1"),
    ("5", "1"),
    ("6", "1"),
    ("*", "-"),
    ("B", " "),
    ("C", " "),
    ("D", " "),
    ("1A", "1 A"),
    ("--", "- -"),
    ("AA", "A A"),
    ("-A", "- A"),
    ("A-", "A -")
]

for replcement in replacement_list:
    s = s.replace(*replcement)
s_list = s.split()
print(
    len(max(s_list, key=lambda x: len(x) if x[0] == "A" and x.count("A") == 1 else 0))
    - 1
)
