"""
cat "USE\Решения\24\Занятие в ЦДО\data\24.txt" | python "USE\Решения\24\Занятие в ЦДО\1.py"
"""

import sys


input = sys.stdin.readline


def check_syntax(a):
    x = True
    try:
        return eval(a)
    except SyntaxError:
        x = False
    finally:
        return x


s = input().strip()

replace_list = [
    ("**", " "),
    ("*-", " "),
    ("*", "-"),
    ("--", " "),
    ("C", " "),
    ("A", " "),
    ("D", " "),
    ("- ", " "),
    ("-B", 'B'),
    ("B-", " "),
    ("1B", "1 B"),
    ("2B", "2 B"),
    ("3B", "3 B"),
    ("4B", "4 B"),
    ("5B", "5 B"),
    ("6B", "6 B")
]

for x in replace_list:
    s = s.replace(*x)
s_list = s.split()
print(len(max(s_list, key=lambda x: len(x) if x[0] == 'B' else 0)))
