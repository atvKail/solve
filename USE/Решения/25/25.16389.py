import re


cnt = 0
pattern = re.compile(r"5\d2.*3\d3\d")
for idx, num in enumerate(range(98591, 10 ** 10, 98591)):
    if pattern.fullmatch(str(num)):
        print(num, idx + 1)
        cnt += 1
print(cnt)
