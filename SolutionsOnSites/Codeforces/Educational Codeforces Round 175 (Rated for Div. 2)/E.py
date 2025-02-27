import sys


input = sys.stdin.readline

n = int(input())
s = list(map(int, list(input().strip())))

ones = [0] * (n + 1)
for i in range(n):
    ones[i + 1] = ones[i] + s[i]

hzz = [False] * n
for i in range(n):
    if s[i] == 0 and s[(i + 1) % n] == 0:
        hzz[i] = True

result = 0
for l in range(n):
    for length in range(2, n + 1):
        r = l + length
        if r > n:
            break

        fzz = False
        for i in range(l, r - 1):
            if hzz[i % n]:
                fzz = True
                break
        if not fzz:
            continue

        onescnt = ones[r] - ones[l]
        if onescnt == 0:
            result += 1
        elif length % 4 == 3:
            result += 1

print(result)  # WA 10
