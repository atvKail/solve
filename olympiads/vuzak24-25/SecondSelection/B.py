n, m, t = map(int, input().split())
answer = 0
for a in range(1, n + 1):
    if t > a:
        bmin = (t + a) // (2 * a + 1)
    else:
        bmin = 1
    bmax = m
    if bmin <= bmax:
        answer += bmax - bmin + 1
print(answer)
