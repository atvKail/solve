n = int(input())
h = list(map(int, input().split()))

S = sum(h)
T = S - (n - 1) * n // 2
q, r = divmod(T, n)

res = []
for i in range(1, n + 1):
    if i <= r:
        res.append(str(q + i))
    else:
        res.append(str(q + i - 1))

print(" ".join(res))
