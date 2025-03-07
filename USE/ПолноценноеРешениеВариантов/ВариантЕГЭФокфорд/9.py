from collections import Counter
import sys


input = sys.stdin.readline


def check_row(row: list) -> bool:
    nums = list(map(int, row.split(";")))

    freq = Counter(nums)

    if len([count for count in freq.values() if count == 3]) != 1:
        return False

    repNums = [num for num, count in freq.items() if count == 3][0]

    unqNum = [num for num, count in freq.items() if count == 1]

    if len(unqNum) != 3:
        return False

    unqSUm = sum(unqNum)

    repAvg = repNums

    if unqSUm <= repAvg:
        return True

    return False


cnt = 0
with open(
    "USE\\ПолноценноеРешениеВариантов\\ВариантЕГЭФокфорд\\data\\9.csv", "r"
) as file:
    for line in file:
        if check_row(line.strip()):
            cnt += 1

print(cnt)
