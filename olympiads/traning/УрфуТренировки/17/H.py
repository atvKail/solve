def np_base3(n):
    if n == 0:
        return "0"
    digits = []
    while n:
        digits.append(str(n % 3))
        n //= 3
    return "".join(reversed(digits))


def solve(n):
    tern = list(map(int, list(np_base3(n))))
    length = len(tern)

    if 2 not in tern:
        return n

    pos = tern.index(2)

    while pos > 0 and tern[pos - 1] == 1:
        pos -= 1

    if pos == 0:
        tern = [1] + [0] * length
    else:
        tern[pos - 1] = 1
        for i in range(pos, length):
            tern[i] = 0

    res = 0
    for d in tern:
        res = res * 3 + d
    return res


results = []
for _ in range(int(input())):
    n = int(input())
    results.append(solve(n))
print(*results, sep="\n")
