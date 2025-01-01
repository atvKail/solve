import re


pattern = re.compile(r"1\d3124.*6")

count = 0
n = 1983

while count < 2:
    if pattern.fullmatch(str(n)):
        print(n, n // 1983)
        count += 1
    n += 1983
