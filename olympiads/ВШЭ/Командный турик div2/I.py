def f(x):
    new = 0
    for i in str(x):
        new += int(i)
    return new


l = int(input())
r = int(input())
nl, nr = l, r
ans = 0
for i in range(l, l + 10):
    x = i
    while len(str(x)) != 1:
        x = f(x)
    if x != 1:
        ans += x
    elif x == 1:
        nl = i
        break
for i in range(r, r - 10, -1):
    x = i
    while len(str(x)) != 1:
        x = f(x)
    if x != 9:
        ans += x
    elif x == 9:
        nr = i
        break
ans += (nr - nl + 1) // 9 * 45
print(ans)
