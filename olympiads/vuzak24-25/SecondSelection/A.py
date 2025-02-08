n, m = map(int, input().split())
t = list(map(int, input().split()))

d, e = 0, 0
for ti in t:
    d = (d + ti) % m
    if not d:
        e += 1
print(e)
