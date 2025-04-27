import sys

input = sys.stdin.readline


n = int(input())
a = list(map(int, input().split()))
if n == 0:
    print(0)
else:
    b = [1] * n
    for i in range(1, n):
        if a[i] > a[i - 1]:
            b[i] = b[i - 1] + 1
        elif a[i] == a[i - 1]:
            b[i] = b[i - 1]

    for i in range(n - 2, -1, -1):
        if a[i] > a[i + 1]:
            b[i] = max(b[i], b[i + 1] + 1)
        elif a[i] == a[i + 1]:
            b[i] = max(b[i], b[i + 1])
    print(sum(b))
