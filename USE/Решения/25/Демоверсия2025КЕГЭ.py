import fnmatch
import heapq

# pattern = r"3?12?14*5"

# for x in range(1917, int(1e10), 1917):
#     if fnmatch.fnmatch(str(x), pattern):
#         print(x, x // 1917)


def fact(n: int) -> list:
    import math

    divs = []
    for x in range(2, int(math.sqrt(n)) + 1):
        if n % x == 0:
            divs.append(x)
            divs.append(n // x)
    return sorted(divs)


cnt = 0
result = ""
for n in range(800000, 100000000):
    divs = fact(n)
    if len(divs) > 1:
        if (divs[0] + divs[-1]) % 10 == 4:
            cnt += 1
            result += f"{n} {divs[0] + divs[-1]} \n"
    if cnt >= 5:
        break
print(result)
