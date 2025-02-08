n = int(input())
a = list(map(int, input().split()))

result = []
suffmin = [0] * n
suffmin[-1] = a[-1]

for i in range(n - 2, -1, -1):
    suffmin[i] = min(a[i], suffmin[i + 1])

q = int(input())
for _ in range(q):
    l, x = map(int, input().split())
    cnt = 0
    curritems = x
    for i in range(l - 1, n):
        if curritems >= a[i]:
            cnt += 1
            curritems -= 1
        else:
            break
    result.append(cnt)

print("\n".join(map(str, result)))
